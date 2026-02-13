import pytest 
from app.utils.session_utils import *
import streamlit as st 

def test_init_session_no_quiz():
    """
    Test that init_session initializes all required session state variables when no quiz is provided.
    """
    init_session(quiz = None)
    
   
    assert st.session_state.feedback == None
    assert st.session_state.user == None
    assert st.session_state.score_saved == False
    assert st.session_state.result_export == None


