

import streamlit as st
import csv
from utils.export_utils import *
from utils.session_utils import *
from utils.feedback_utils import *
from utils.form_utils import *
import pandas as pd

from utils.quiz_logic import Quiz, User

# Initialize session state variables and load quiz questions from CSV
init_session(quiz = Quiz.from_csv("data/quiz_questions.csv"))

st.title("Test your knowledge")

# Show branding image in sidebar
st.sidebar.image("images/duck_guidance.png")

# Display feedback message if present in session state
if st.session_state.feedback is not None:
    msg_type, msg_content = st.session_state.feedback
    # Show success or error message based on feedback type
    if msg_type == "success":
        st.success(msg_content)
    else:
        st.error(msg_content)
    # Clear feedback after displaying so it doesn't persist
    st.session_state.feedback = None

# If user details are not yet provided, show the user form
if st.session_state.user is None:
    user_form()

# If quiz is ongoing, display the current question and answer options
elif st.session_state.quiz.current_question() is not None:
    q = st.session_state.quiz.current_question()
    st.subheader(q.text)
    # Show possible answers as radio buttons
    answer = st.radio("Choose an answer:", q.possible_answers)
    if st.button("Submit"):
        # Evaluate answer and update feedback in session state
        msg_type, msg_content = give_feedback(st.session_state.quiz, st.session_state.user, answer)
        st.session_state.feedback = (msg_type, msg_content)
        # Rerun to update UI and move to next question
        st.rerun()
    # Show current score after each question
    st.write(f"Score: {st.session_state.user.score}")

# If quiz is finished, display results and export options
else:
    st.subheader("Quiz Finished!")
    total = len(st.session_state.quiz.questions)
    score = st.session_state.user.score
    percent = (score / total) * 100 if total > 0 else 0
    st.write(f"Your final score is {score}/{total}")
    # Show pass/fail message based on score percentage
    if percent >= 80:
        st.success(f"Congratulations! You passed the quiz with {percent:.0f}% correct.")
    else:
        st.error(f"You did not pass. You scored {percent:.0f}%. Try again to improve your score!")
    # Save user score to CSV only once
    if not st.session_state.score_saved:
        write_user_scores(st.session_state.user, "user_scores.csv")
    st.session_state.score_saved = True
    # Prepare CSV data for download
    csv_data = export_results(st.session_state.user)
    st.download_button(
        label = "Export my answers",
        data = csv_data,
        file_name = "COP_quiz_answers.csv",
        mime = "text/csv"
    )
    # Allow user to restart the quiz by clearing session state
    if st.button("Restart Quiz"):
        del st.session_state.quiz
        del st.session_state.user
        st.rerun()