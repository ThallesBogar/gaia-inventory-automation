import os

import streamlit as st

from helpers import get_input_label

_, center_col, _ = st.columns([2,5,1])

with center_col:
    login_form_container = st.container(
        key='login-container'
    )

    with login_form_container:
        column = st.columns(1)[0]

        with column:
            login_logo_image_path = os.path.join(os.getcwd(), 'assets', 'img', 'login-page-logo.png')
            st.image(image=login_logo_image_path, use_container_width=True)
            st.markdown("<div></div>", unsafe_allow_html=True)

            username_input_label = get_input_label('Username', 'account_circle')
            st.markdown(username_input_label, unsafe_allow_html=True)
            username = st.text_input(label="null", key='username-input', placeholder='Digite o seu e-mail...', label_visibility='hidden')

            password_input_label = get_input_label('Password', 'key')
            st.markdown(password_input_label, unsafe_allow_html=True)
            password = st.text_input(label="null", key='password-input', type='password', placeholder='Digite a sua senha...', label_visibility='hidden')

            login_button = st.button(label='Login', type='primary', key='login-button')

            if login_button:
                st.session_state["is_user_logged_in"] = True
                st.rerun()