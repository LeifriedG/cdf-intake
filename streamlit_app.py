import streamlit as st

st.set_page_config(
    page_title="CDF Intake Form",
    page_icon="📋",
    layout="wide",
)

# --- Sidebar navigation ---
pages = {
    "📋 CDF Intake Form": [
        st.Page("pages/1_General_Info.py", title="1. General Info", icon="🏢"),
        st.Page("pages/2_PO_Data.py", title="2. PO Data", icon="📄"),
        st.Page("pages/3_Man_Power.py", title="3. Man Power", icon="👷"),
        st.Page("pages/4_Equipment.py", title="4. Equipment", icon="🚜"),
        st.Page("pages/5_Chemicals.py", title="5. Chemicals", icon="🧪"),
        st.Page("pages/6_Submit.py", title="Submit", icon="📨"),
    ],
}

nav = st.navigation(pages)
nav.run()

