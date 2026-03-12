import streamlit as st
from utils.auth import require_login
from utils.branding import add_branding

require_login()
add_branding()

st.title("🗒️ Notes")

st.write("Use this space to capture general notes, ideas, and observations from your Gemba walks.")

st.text_area("Notes", height=300)
