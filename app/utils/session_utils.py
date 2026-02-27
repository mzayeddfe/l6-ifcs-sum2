import streamlit as st


def init_session(quiz = None):
    """
    Initialize Streamlit session state variables for the quiz application.
    Args:
        quiz (Quiz, optional): The quiz instance to store in session state.
    Returns:
        None
    """
    # Add quiz object to session state if not already present
    if "quiz" not in st.session_state and quiz is not None:
        st.session_state.quiz = quiz
    # Initialize feedback message state
    if "feedback" not in st.session_state:
        st.session_state.feedback = None
    # Initialize user object state
    if "user" not in st.session_state:
        st.session_state.user = None
    # Track if score has been saved to CSV
    if "score_saved" not in st.session_state:
        st.session_state.score_saved = False
    # Store exported results for download
    if "result_export" not in st.session_state:
        st.session_state.result_export = None
