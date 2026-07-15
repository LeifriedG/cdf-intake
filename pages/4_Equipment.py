import streamlit as st

# Initialize persistent storage
if "form_data" not in st.session_state:
    st.session_state["form_data"] = {}
if "equipment_data" not in st.session_state:
    st.session_state["equipment_data"] = []

fd = st.session_state["form_data"]

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

# Dynamic number of equipment entries
num_items = st.number_input("Number of equipment entries", min_value=0, max_value=20, value=fd.get("num_equip", 1))
fd["num_equip"] = num_items

# Ensure list is big enough
while len(st.session_state["equipment_data"]) < int(num_items):
    st.session_state["equipment_data"].append({"type": EQUIPMENT_TYPES[0], "how_many": 0})

for i in range(int(num_items)):
    equip = st.session_state["equipment_data"][i]
    with st.container(border=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            type_idx = EQUIPMENT_TYPES.index(equip["type"]) if equip.get("type") in EQUIPMENT_TYPES else 0
            equip["type"] = st.selectbox("Type of Rolling Stock", EQUIPMENT_TYPES, index=type_idx, key=f"equip_type_{i}")
        with col2:
            equip["how_many"] = st.number_input("How Many?", min_value=0, step=1, value=equip.get("how_many", 0), key=f"equip_qty_{i}")
