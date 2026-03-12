import streamlit as st
import pandas as pd
from utils.data import load_csv, save_csv, ISSUE_FILE, FEEDBACK_FILE
from utils.auth import require_login
from utils.branding import add_branding, PRIMARY_RED, PRIMARY_YELLOW, PRIMARY_GREEN, status_tag

require_login()
add_branding()

st.title("📝 Action Tracking")

issue_cols = ["Date", "Area", "Issue Observed", "Owner", "Priority", "Due Date", "Status"]
feedback_cols = ["Date", "Employee", "Area", "Feedback", "Action Taken"]

issues = load_csv(ISSUE_FILE, issue_cols)
feedback = load_csv(FEEDBACK_FILE, feedback_cols)

st.subheader("Issue Log")

if "Priority" in issues.columns:
    pass
else:
    issues["Priority"] = ""

priority_help = (
    f"{status_tag('High', PRIMARY_RED)} = urgent, "
    f"{status_tag('Medium', PRIMARY_YELLOW)} = important, "
    f"{status_tag('Low', PRIMARY_GREEN)} = normal"
)
st.markdown(priority_help, unsafe_allow_html=True)

edited_issues = st.data_editor(
    issues,
    num_rows="dynamic",
    key="issues_editor",
)

col1, col2 = st.columns(2)
with col1:
    if st.button("💾 Save Issues"):
        save_csv(edited_issues, ISSUE_FILE)
        st.success("Issues saved.")
with col2:
    st.download_button(
        "⬇️ Download Issues CSV",
        edited_issues.to_csv(index=False),
        file_name="issues.csv",
        mime="text/csv",
    )

st.markdown("---")

st.subheader("Employee Feedback Log")
edited_feedback = st.data_editor(
    feedback,
    num_rows="dynamic",
    key="feedback_editor",
)

col3, col4 = st.columns(2)
with col3:
    if st.button("💾 Save Feedback"):
        save_csv(edited_feedback, FEEDBACK_FILE)
        st.success("Feedback saved.")
with col4:
    st.download_button(
        "⬇️ Download Feedback CSV",
        edited_feedback.to_csv(index=False),
        file_name="feedback.csv",
        mime="text/csv",
    )
