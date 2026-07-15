import streamlit as st
import requests
import json

st.header("📨 Review & Submit", divider="green")
st.caption("Review your entries below and submit the CDF form.")

# --- Collect data from session state ---
def get_val(key, default=""):
    return st.session_state.get(key, default)

# General Info
general_info = {
    "company_name": get_val("Company Name"),
    "main_phone": get_val("Main Phone Number"),
    "main_fax": get_val("Main Fax Number"),
    "office_manager": get_val("Office Manager Name"),
    "main_email": get_val("Main/General Email"),
    "site_supt_name": get_val("site_supt_name"),
    "site_supt_cell": get_val("site_supt_cell"),
    "site_supt_email": get_val("site_supt_email"),
    "ehs_name": get_val("ehs_name"),
    "ehs_cell": get_val("ehs_cell"),
    "ehs_email": get_val("ehs_email"),
    "day_supt_name": get_val("day_supt_name"),
    "day_supt_cell": get_val("day_supt_cell"),
    "day_supt_email": get_val("day_supt_email"),
    "night_supt_name": get_val("night_supt_name"),
    "night_supt_cell": get_val("night_supt_cell"),
    "night_supt_email": get_val("night_supt_email"),
    "contact_1": get_val("contact_1"),
    "contact_2": get_val("contact_2"),
    "contact_3": get_val("contact_3"),
    "contact_4": get_val("contact_4"),
}

# PO Data
num_pos = int(get_val("Number of POs to enter", 1))
po_data = []
for i in range(num_pos):
    po_data.append({
        "po_number": get_val(f"po_number_{i}"),
        "po_description": get_val(f"po_desc_{i}"),
        "department": get_val(f"po_dept_{i}"),
    })

# Man Power
manpower_edits = get_val("manpower_editor", {})
manpower_data = []
if isinstance(manpower_edits, dict) and "edited_rows" in manpower_edits:
    for row_idx, changes in manpower_edits["edited_rows"].items():
        total = changes.get("Total Workers & Supervisors", 0)
        if total and total > 0:
            manpower_data.append({
                "row_index": int(row_idx),
                "total_workers": total,
            })

# Equipment
num_equip = int(get_val("Number of equipment entries", 1))
equipment_data = []
for i in range(num_equip):
    qty = get_val(f"equip_qty_{i}", 0)
    if qty and qty > 0:
        equipment_data.append({
            "type": get_val(f"equip_type_{i}"),
            "how_many": qty,
        })

# Chemicals
num_chems = int(get_val("Number of chemicals to enter", 1))
chemical_data = []
for i in range(num_chems):
    name = get_val(f"chem_name_{i}")
    if name:
        chemical_data.append({
            "product_common_name": name,
            "manufacturer": get_val(f"chem_mfr_{i}"),
            "product_technical_name": get_val(f"chem_tech_{i}"),
        })

# --- Build full payload ---
payload = {
    "general_info": general_info,
    "po_data": po_data,
    "manpower": manpower_data,
    "equipment": equipment_data,
    "chemicals": chemical_data,
}

# --- Display summary ---
company = general_info["company_name"] or "(not entered)"
st.subheader(f"Submission for: {company}")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("POs", len(po_data))
with col2:
    st.metric("Equipment Items", len(equipment_data))
with col3:
    st.metric("Chemicals", len(chemical_data))

with st.expander("📋 View full submission data"):
    st.json(payload)

# --- Submit ---
st.divider()

if not general_info["company_name"]:
    st.warning("⚠️ Please fill in at least the Company Name on the General Info page before submitting.")

webhook_url = st.secrets.get("power_automate", {}).get("webhook_url", "")

if not webhook_url:
    st.error(
        "⚠️ Power Automate webhook URL is not configured. "
        "Add it to `.streamlit/secrets.toml` under `[power_automate]`."
    )
else:
    if st.button("🚀 Submit CDF Form", type="primary", disabled=not general_info["company_name"]):
        with st.spinner("Submitting to Power Automate..."):
            try:
                response = requests.post(
                    webhook_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=30,
                )
                if response.status_code in (200, 202):
                    st.success("✅ CDF form submitted successfully!")
                    st.balloons()
                else:
                    st.error(f"❌ Submission failed (HTTP {response.status_code}): {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Connection error: {e}")
