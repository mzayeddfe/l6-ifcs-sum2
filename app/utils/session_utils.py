import streamlit as st

def init_session(quiz = None):
    # Initialize feedback in session state if not present
    if "quiz" not in st.session_state and quiz is not None:
        st.session_state.quiz= quiz
    
    if  "feedback" not in st.session_state:
        st.session_state.feedback = None

    if "user" not in st.session_state:
        st.session_state.user = None


    if "score_saved" not in st.session_state:
        st.session_state.score_saved = False

    if "result_export" not in st.session_state:
        st.session_state.result_export = None