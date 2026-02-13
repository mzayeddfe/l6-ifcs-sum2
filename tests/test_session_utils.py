import pytest 
from app.utils.session_utils import *
import streamlit as st 

def test_init_session_no_quiz():
    
    init_session(quiz = None)
    
    assert "quiz" in st.session_state 
    assert "user" in st.session_state 
    assert "feedback" in st.session_state
    assert st.session_state.feedback == None
    assert st.session_state.user == None
    assert st.session_state.score_saved == False
    assert st.session_state.result_export == None


