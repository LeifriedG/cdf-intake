import streamlit as st

# Initialize persistent storage
if "form_data" not in st.session_state:
    st.session_state["form_data"] = {}
if "chemical_data" not in st.session_state:
    st.session_state["chemical_data"] = []

fd = st.session_state["form_data"]

st.header("5. Chemical Usage", divider="blue")
st.caption(
    "Provide information on chemicals you will bring on-site."
)

# Dynamic number of chemical entries
num_chems = st.number_input("Number of chemicals to enter", min_value=0, max_value=20, value=fd.get("num_chems", 1))
fd["num_chems"] = num_chems

# Ensure list is big enough
while len(st.session_state["chemical_data"]) < int(num_chems):
    st.session_state["chemical_data"].append({"product_common_name": "", "manufacturer": "", "product_technical_name": ""})

for i in range(int(num_chems)):
    chem = st.session_state["chemical_data"][i]
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            chem["product_common_name"] = st.text_input("Product Common Name", value=chem.get("product_common_name", ""), key=f"chem_name_{i}")
        with col2:
            chem["manufacturer"] = st.text_input("Manufacturer", value=chem.get("manufacturer", ""), key=f"chem_mfr_{i}")
        with col3:
            chem["product_technical_name"] = st.text_input("Product Technical Name", value=chem.get("product_technical_name", ""), key=f"chem_tech_{i}")
