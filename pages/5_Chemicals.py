import streamlit as st

st.header("5. Chemical Usage", divider="blue")
st.caption(
    "Provide information on chemicals you will bring on-site."
)

num_chems = st.number_input("Number of chemicals to enter", min_value=0, max_value=20, value=1)

for i in range(int(num_chems)):
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_input("Product Common Name", key=f"chem_name_{i}")
        with col2:
            st.text_input("Manufacturer", key=f"chem_mfr_{i}")
        with col3:
            st.text_input("Product Technical Name", key=f"chem_tech_{i}")
