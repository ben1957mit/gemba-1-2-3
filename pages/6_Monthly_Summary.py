import streamlit as st
from utils.auth import require_login
from utils.branding import add_branding, PRIMARY_GREEN, PRIMARY_YELLOW, PRIMARY_RED, status_tag

require_login()
add_branding()

st.title("📅 Monthly Summary Review")

st.subheader("Topics to Review")
st.markdown(
    """
- Completed vs. open actions  
- Recurring issues  
- Safety trends  
- Productivity improvements  
- Training needs  
- Layout or process redesign opportunities  
"""
)

st.subheader("Deliverables")
st.markdown(
    """
- Monthly Gemba Report  
- Updated SOPs (if needed)  
- Improvement roadmap  
"""
)

st.subheader("Monthly Notes")
st.text_area("Summary notes for this month", height=250)

st.markdown("---")
st.markdown(
    f"{status_tag('Green', PRIMARY_GREEN)} = strong performance & stability<br>"
    f"{status_tag('Yellow', PRIMARY_YELLOW)} = watch closely, plan improvements<br>"
    f"{status_tag('Red', PRIMARY_RED)} = urgent focus required",
    unsafe_allow_html=True,
)
