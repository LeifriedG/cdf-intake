import streamlit as st

st.header("5. Chemical Usage", divider="blue")
st.caption(
    "Provide information on chemicals you will bring on-site. "
    "Please attach SDS forms in your submission email."
)

# Dynamic number of chemical entries
num_chems = st.number_input("Number of chemicals to enter", min_value=0, max_value=20, value=1)

for i in range(int(num_chems)):
    with st.container(border=True):
        st.subheader(f"Chemical #{i + 1}")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Product Common Name", key=f"chem_name_{i}")
            st.text_input("Manufacturer", key=f"chem_mfr_{i}")
            st.text_input("Product Technical Name", key=f"chem_tech_{i}")
        with col2:
            st.selectbox("SDS Attached in Email?", ["Yes", "No"], key=f"chem_sds_{i}")
            st.selectbox("Used at Mill Before?", ["Yes", "No"], key=f"chem_used_{i}")
            st.selectbox("Communicated to Mill Contact?", ["Yes", "No"], key=f"chem_comm_{i}")

        col3, col4 = st.columns(2)
        with col3:
            st.number_input("Quantity Amount", min_value=0.0, step=0.1, key=f"chem_qty_{i}")
        with col4:
            st.text_input(
                "Unit of Measure",
                key=f"chem_unit_{i}",
                placeholder="gallons, pounds, etc.",
            )
