import streamlit as st
from datetime import date

st.header("4. Equipment (Rolling Stock)", divider="blue")
st.caption(
    "Enter information on the rolling stock / equipment you will bring on-site. "
    "Select the type from the dropdown; if 'Other', please specify in Comments."
)

EQUIPMENT_TYPES = [
    "Bobcats/Skid Steers",
    "Cranes (all sizes & types)",
    "Heavy/Specialty Trucks",
    "Hydroblasting Trucks/Trailers",
    "Lulls",
    "Passenger Vehicles",
    "Portable Generator",
    "Tool Truck",
    "UTV/Cart",
    "Vacuum Trucks",
    "Other",
]

# Dynamic number of equipment entries
num_items = st.number_input("Number of equipment entries", min_value=0, max_value=20, value=1)

for i in range(int(num_items)):
    with st.container(border=True):
        st.subheader(f"Equipment #{i + 1}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.selectbox("Type of Rolling Stock", EQUIPMENT_TYPES, key=f"equip_type_{i}")
            st.number_input("How Many?", min_value=0, step=1, key=f"equip_qty_{i}")
        with col2:
            st.date_input("Arrival Date", value=date.today(), key=f"equip_arrival_{i}")
            st.date_input("End Date", value=date.today(), key=f"equip_end_{i}")
        with col3:
            st.selectbox(
                "Gate Passes Requested?",
                ["Yes", "No"],
                key=f"equip_gate_req_{i}",
            )
            st.selectbox(
                "Gate Passes Approved?",
                ["Yes", "No"],
                key=f"equip_gate_appr_{i}",
            )
            st.text_input("Comments", key=f"equip_comments_{i}")
