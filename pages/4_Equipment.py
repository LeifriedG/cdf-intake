import streamlit as st

st.header("4. Equipment (Rolling Stock)", divider="blue")
st.caption(
    "Enter the type and quantity of rolling stock / equipment you will bring on-site."
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

num_items = st.number_input("Number of equipment entries", min_value=0, max_value=20, value=1)

for i in range(int(num_items)):
    with st.container(border=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.selectbox("Type of Rolling Stock", EQUIPMENT_TYPES, key=f"equip_type_{i}")
        with col2:
            st.number_input("How Many?", min_value=0, step=1, key=f"equip_qty_{i}")
