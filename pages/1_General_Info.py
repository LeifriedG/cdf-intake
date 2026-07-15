import streamlit as st

# Initialize persistent storage
if "form_data" not in st.session_state:
    st.session_state["form_data"] = {}

fd = st.session_state["form_data"]

st.header("1. General Info", divider="blue")
st.caption("Enter your company's general contact information below.")

# --- Company Name ---
fd["company_name"] = st.text_input(
    "Company Name", value=fd.get("company_name", ""),
    placeholder="e.g., Industrial Electrical Services, Inc."
)

st.divider()

# --- Contact Information ---
col1, col2 = st.columns(2)

with col1:
    fd["main_phone"] = st.text_input("Main Phone Number", value=fd.get("main_phone", ""))
    fd["main_fax"] = st.text_input("Main Fax Number", value=fd.get("main_fax", ""))
    fd["office_manager"] = st.text_input("Office Manager Name", value=fd.get("office_manager", ""))
    fd["main_email"] = st.text_input("Main/General Email", value=fd.get("main_email", ""))

with col2:
    st.markdown("**Site Superintendent**")
    fd["site_supt_name"] = st.text_input("Name", value=fd.get("site_supt_name", ""), key="site_supt_name")
    fd["site_supt_cell"] = st.text_input("Cell Phone", value=fd.get("site_supt_cell", ""), key="site_supt_cell")
    fd["site_supt_email"] = st.text_input("Email", value=fd.get("site_supt_email", ""), key="site_supt_email")

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.markdown("**EHS Specialist**")
    fd["ehs_name"] = st.text_input("Name", value=fd.get("ehs_name", ""), key="ehs_name")
    fd["ehs_cell"] = st.text_input("Cell Phone", value=fd.get("ehs_cell", ""), key="ehs_cell")
    fd["ehs_email"] = st.text_input("Email", value=fd.get("ehs_email", ""), key="ehs_email")

with col4:
    st.markdown("**Day Superintendent**")
    fd["day_supt_name"] = st.text_input("Name", value=fd.get("day_supt_name", ""), key="day_supt_name")
    fd["day_supt_cell"] = st.text_input("Cell Phone", value=fd.get("day_supt_cell", ""), key="day_supt_cell")
    fd["day_supt_email"] = st.text_input("Email", value=fd.get("day_supt_email", ""), key="day_supt_email")

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.markdown("**Night Superintendent**")
    fd["night_supt_name"] = st.text_input("Name", value=fd.get("night_supt_name", ""), key="night_supt_name")
    fd["night_supt_cell"] = st.text_input("Cell Phone", value=fd.get("night_supt_cell", ""), key="night_supt_cell")
    fd["night_supt_email"] = st.text_input("Email", value=fd.get("night_supt_email", ""), key="night_supt_email")

with col6:
    st.markdown("**Mill Main Contacts**")
    fd["contact_1"] = st.text_input("Main IP Contact 1", value=fd.get("contact_1", ""), key="contact_1")
    fd["contact_2"] = st.text_input("Main IP Contact 2", value=fd.get("contact_2", ""), key="contact_2")
    fd["contact_3"] = st.text_input("Main IP Contact 3", value=fd.get("contact_3", ""), key="contact_3")
    fd["contact_4"] = st.text_input("Main IP Contact 4", value=fd.get("contact_4", ""), key="contact_4")
