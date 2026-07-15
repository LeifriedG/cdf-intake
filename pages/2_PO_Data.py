import streamlit as st

# Initialize persistent storage
if "form_data" not in st.session_state:
    st.session_state["form_data"] = {}
if "po_data" not in st.session_state:
    st.session_state["po_data"] = []

fd = st.session_state["form_data"]

st.header("2. PO Data", divider="blue")
st.caption(
    "Enter the Purchase Order(s) for the jobs covered by this CDF submission. "
    "For Service POs, ensure you enter the full number (e.g., S086762152)."
)

# Allow multiple POs
num_pos = st.number_input("Number of POs to enter", min_value=1, max_value=10, value=fd.get("num_pos", 1))
fd["num_pos"] = num_pos

# Ensure po_data list is big enough
while len(st.session_state["po_data"]) < int(num_pos):
    st.session_state["po_data"].append({"po_number": ""})

for i in range(int(num_pos)):
    po = st.session_state["po_data"][i]
    with st.container(border=True):
        po["po_number"] = st.text_input(f"PO #{i + 1}", value=po.get("po_number", ""), key=f"po_number_{i}", placeholder="S0XXXXXXXX")
