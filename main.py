import os

import streamlit as st
from helpers import load_css

if "is_user_logged_in" not in st.session_state:
    st.session_state["is_user_logged_in"] = False


st.markdown(load_css("styles.css"), unsafe_allow_html=True)

login_page = st.Page(
    page="views/login.py",
    title="Login Page",
    icon=":material/login:",
    url_path="login",
)

home_page = st.Page(
    page="views/home.py",
    title="Home Page",
    icon=":material/home:",
    url_path="home"
)

if st.session_state['is_user_logged_in']:
    pg = st.navigation([home_page])
else:
    pg = st.navigation([login_page])

pg.run()