import streamlit as st
import pandas as pd
import yaml
from pathlib import Path

st.header("3. Shift Man-Power", divider="blue")
st.caption(
    "Enter the TOTAL man-power loading (workers + supervisors) for each shift. "
    "Please enter only numbers — no text."
)

# Load date range from config
config_path = Path(__file__).parent.parent / "config.yaml"
with open(config_path) as f:
    config = yaml.safe_load(f)

start_date = config["manpower"]["start_date"]
end_date = config["manpower"]["end_date"]

st.info(f"📅 Outage period: **{start_date}** to **{end_date}**")

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
