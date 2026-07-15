import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.header("3. Shift Man-Power", divider="blue")
st.caption(
    "Enter the TOTAL man-power loading (workers + supervisors) for each shift. "
    "Please enter only numbers — no text."
)

# Date range selection
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", value=date.today())
with col2:
    end_date = st.date_input("End Date", value=date.today() + timedelta(days=13))

if start_date > end_date:
    st.error("Start date must be before end date.")
    st.stop()

# Build editable dataframe
dates = pd.date_range(start=start_date, end=end_date)
rows = []
for d in dates:
    rows.append({"Date": d.strftime("%Y-%m-%d"), "Shift": "Day", "Total Workers & Supervisors": 0})
    rows.append({"Date": d.strftime("%Y-%m-%d"), "Shift": "Night", "Total Workers & Supervisors": 0})

df = pd.DataFrame(rows)

st.data_editor(
    df,
    column_config={
        "Date": st.column_config.TextColumn("Date", disabled=True),
        "Shift": st.column_config.TextColumn("Shift", disabled=True),
        "Total Workers & Supervisors": st.column_config.NumberColumn(
            "Total Workers & Supervisors",
            min_value=0,
            max_value=500,
            step=1,
        ),
    },
    use_container_width=True,
    hide_index=True,
    key="manpower_editor",
)
