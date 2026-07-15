import streamlit as st

st.header("2. PO Data", divider="blue")
st.caption(
    "Enter the Purchase Order(s) for the jobs covered by this CDF submission. "
    "For Service POs, ensure you enter the full number (e.g., S086762152)."
)

DEPARTMENTS = [
    "Paper - PM1",
    "Paper - PM2",
    "Power",
    "Fibers - Pulp",
    "Fibers - Woodyard",
    "Power - Caustic",
    "Power - Evaps",
    "Mill Wide",
]

# Allow multiple POs
num_pos = st.number_input("Number of POs to enter", min_value=1, max_value=10, value=1)

for i in range(int(num_pos)):
    with st.container(border=True):
        st.subheader(f"PO #{i + 1}")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.text_input("PO Number", key=f"po_number_{i}", placeholder="S0XXXXXXXX")
        with col2:
            st.text_input("PO Description", key=f"po_desc_{i}")
        with col3:
            st.selectbox("Department", DEPARTMENTS, key=f"po_dept_{i}")
