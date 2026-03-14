import streamlit as st
from datetime import date, time
from utils.auth import require_login

require_login()

st.title("Daily Gemba Walk")

# --- Date and Shift ---
st.subheader("Date & Shift")
walk_date = st.date_input("Gemba Walk Date", value=date.today())
shift_start = st.time_input("Shift Start Time", value=time(6, 0))
shift_end = st.time_input("Shift End Time", value=time(14, 0))

# --- Walk Timing ---
st.subheader("Walk Timing")
walk_start = st.time_input("Walk Start Time", value=time(9, 0))
walk_end = st.time_input("Walk End Time", value=time(10, 0))

# --- Personnel ---
st.subheader("Personnel")
supervisor = st.text_input("Supervisor Name")
team_lead = st.text_input("Team Lead Name")

# --- Area Selection ---
st.subheader("Area Observed")
area = st.selectbox(
    "Select Area",
    ["Receiving", "Picking", "Packing", "Shipping", "Returns", "Inventory", "Safety Zone"]
)

# --- Issue Tracking ---
st.subheader("Issues & Observations")

issue_description = st.text_area("Describe the Issue or Observation")

severity = st.radio(
    "Severity Level",
    ["Low", "Medium", "High", "Critical"],
    index=0
)

corrective_action = st.text_area("Corrective Action Taken (if any)")

responsible_person = st.text_input("Responsible Person for Follow-up")

due_date = st.date_input("Follow-up Due Date", value=date.today())

# --- Completion Button ---
submitted = st.button("Save Daily Gemba Walk")

# --- Summary ---
if submitted:
    st.success("Daily Gemba Walk Saved")
    st.markdown("---")
    st.subheader("Summary")

    st.write("**Date:**", walk_date)
    st.write("**Shift:**", shift_start, "to", shift_end)
    st.write("**Walk:**", walk_start, "to", walk_end)
    st.write("**Supervisor:**", supervisor)
    st.write("**Team Lead:**", team_lead)
    st.write("**Area:**", area)
    st.write("**Issue:**", issue_description)
    st.write("**Severity:**", severity)
    st.write("**Corrective Action:**", corrective_action)
    st.write("**Responsible:**", responsible_person)
    st.write("**Due Date:**", due_date)
