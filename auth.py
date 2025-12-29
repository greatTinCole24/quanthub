import streamlit as st

def require_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔐 Login")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if password == st.secrets["APP_PASSWORD"]:
                st.session_state.logged_in = True
            else:
                st.error("Invalid password")

        st.stop()
