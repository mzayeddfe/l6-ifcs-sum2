import streamlit as st
import re
from utils.quiz_logic import User

def validate_name(name):
    """
    Validate that the provided name is at least 2 characters and alphanumeric.
    Args:
        name (str): The name to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    if len(name) <= 1:
         return False
    if not name.isalnum():
         return False
    return True

def validate_email(email):
    """
    Validate that the provided email matches a standard email pattern.
    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
    if re.fullmatch(regex, email):
        return True
    return False

def user_form():
    """
    Display a Streamlit form for user details and validate input.
    On successful submission, stores a User object in session state.
    """

    with st.form("user_details"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Start Quiz")
        if submitted:
            if not (first and last and email):
                st.warning("Please fill in all fields.")
            elif not (validate_name(first)):
                st.warning("Please enter a valid first name")
            elif not (validate_name(last)):
                st.warning("Please enter a valid last name")
            elif not(validate_email(email)):
                st.warning("Please enter a valid email")

            else:
                st.session_state.user = User(first, last, email)
                st.rerun()