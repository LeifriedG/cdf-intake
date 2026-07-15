import streamlit as st
import requests
import json

st.header("📨 Review & Submit", divider="green")
st.caption("Review your entries below and submit the CDF form.")

# --- Collect data from persistent session state ---
if "form_data" not in st.session_state:
    st.session_state["form_data"] = {}

fd = st.session_state["form_data"]

# General Info
general_info = {
    "company_name": fd.get("company_name", ""),
    "main_phone": fd.get("main_phone", ""),
    "main_fax": fd.get("main_fax", ""),
    "office_manager": fd.get("office_manager", ""),
    "main_email": fd.get("main_email", ""),
    "site_supt_name": fd.get("site_supt_name", ""),
    "site_supt_cell": fd.get("site_supt_cell", ""),
    "site_supt_email": fd.get("site_supt_email", ""),
    "ehs_name": fd.get("ehs_name", ""),
    "ehs_cell": fd.get("ehs_cell", ""),
    "ehs_email": fd.get("ehs_email", ""),
    "day_supt_name": fd.get("day_supt_name", ""),
    "day_supt_cell": fd.get("day_supt_cell", ""),
    "day_supt_email": fd.get("day_supt_email", ""),
    "night_supt_name": fd.get("night_supt_name", ""),
    "night_supt_cell": fd.get("night_supt_cell", ""),
    "night_supt_email": fd.get("night_supt_email", ""),
    "contact_1": fd.get("contact_1", ""),
    "contact_2": fd.get("contact_2", ""),
    "contact_3": fd.get("contact_3", ""),
    "contact_4": fd.get("contact_4", ""),
}

# PO Data
po_data = st.session_state.get("po_data", [])
po_data_clean = [po for po in po_data if po.get("po_number")]

# Man Power
manpower_df = st.session_state.get("manpower_data", None)
manpower_data = []
if manpower_df is not None:
    for _, row in manpower_df.iterrows():
        total = row.get("Total Workers & Supervisors", 0)
        if total and total > 0:
            manpower_data.append({
                "date": row["Date"],
                "shift": row["Shift"],
                "total_workers": int(total),
            })

# Equipment
equipment_data = [e for e in st.session_state.get("equipment_data", []) if e.get("how_many", 0) > 0]

# Chemicals
chemical_data = [c for c in st.session_state.get("chemical_data", []) if c.get("product_common_name")]

# --- Build full payload ---
payload = {
    "general_info": general_info,
    "po_data": po_data_clean,
    "manpower": manpower_data,
    "equipment": equipment_data,
    "chemicals": chemical_data,
}

# --- Display summary ---
company = general_info["company_name"] or "(not entered)"
st.subheader(f"Submission for: {company}")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("POs", len(po_data_clean))
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
