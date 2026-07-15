import streamlit as st

st.header("1. General Info", divider="blue")
st.caption("Enter your company's general contact information below.")

# --- Company Name ---
company_name = st.text_input("Company Name", placeholder="e.g., Industrial Electrical Services, Inc.")

st.divider()

# --- Contact Information ---
col1, col2 = st.columns(2)

with col1:
    main_phone = st.text_input("Main Phone Number")
    main_fax = st.text_input("Main Fax Number")
    office_manager = st.text_input("Office Manager Name")
    main_email = st.text_input("Main/General Email")

with col2:
    st.markdown("**Site Superintendent**")
    site_supt_name = st.text_input("Name", key="site_supt_name")
    site_supt_cell = st.text_input("Cell Phone", key="site_supt_cell")
    site_supt_email = st.text_input("Email", key="site_supt_email")

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.markdown("**EHS Specialist**")
    ehs_name = st.text_input("Name", key="ehs_name")
    ehs_cell = st.text_input("Cell Phone", key="ehs_cell")
    ehs_email = st.text_input("Email", key="ehs_email")

with col4:
    st.markdown("**Day Superintendent**")
    day_supt_name = st.text_input("Name", key="day_supt_name")
    day_supt_cell = st.text_input("Cell Phone", key="day_supt_cell")
    day_supt_email = st.text_input("Email", key="day_supt_email")

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.markdown("**Night Superintendent**")
    night_supt_name = st.text_input("Name", key="night_supt_name")
    night_supt_cell = st.text_input("Cell Phone", key="night_supt_cell")
    night_supt_email = st.text_input("Email", key="night_supt_email")

with col6:
    st.markdown("**Mill Main Contacts**")
    contact_1 = st.text_input("Main IP Contact 1", key="contact_1")
    contact_2 = st.text_input("Main IP Contact 2", key="contact_2")
    contact_3 = st.text_input("Main IP Contact 3", key="contact_3")
    contact_4 = st.text_input("Main IP Contact 4", key="contact_4")
