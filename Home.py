import streamlit as st
from utils.auth import login, logout

st.title("Gemba Walk App")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password")
else:
    st.write("Welcome to the Gemba Walk App!")
