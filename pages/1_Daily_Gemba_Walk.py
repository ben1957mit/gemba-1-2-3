import streamlit as st
from utils.auth import require_login
from utils.branding import add_branding, PRIMARY_GREEN

require_login()
add_branding()

st.title("📅 Daily Gemba Walk Schedule")

st.subheader("Purpose")
st.write("Observe real-time warehouse operations, ensure safety compliance, identify waste, and engage employees.")

st.subheader("Daily Time Block")
st.write("**Start Time:** 8:30 AM")
st.write("**Duration:** 20–30 minutes")
st.write("**Participants:** Supervisor, Manager, or CI Lead")

st.subheader("Daily Focus Areas")
st.markdown(
    """
- **Monday:** Receiving & Unloading  
- **Tuesday:** Put-Away & Storage  
- **Wednesday:** Picking Operations  
- **Thursday:** Packing & Quality Control  
- **Friday:** Shipping & Staging  
"""
)

st.subheader("Daily Checklist")
st.markdown(
    f"<div style='background:{PRIMARY_GREEN}20; padding:8px; border-radius:4px;'>"
    "Check off items as you walk the floor.</div>",
    unsafe_allow_html=True,
)

checklist_items = [
    "Verify work is performed according to SOPs",
    "Check for safety hazards (aisles, equipment, PPE)",
    "Observe workflow for delays or bottlenecks",
    "Confirm inventory labeling and bin accuracy",
    "Engage employees with improvement questions",
    "Document issues and assign follow-up actions",
]

for item in checklist_items:
    st.checkbox(item)
