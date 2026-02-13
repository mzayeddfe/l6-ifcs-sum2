
import streamlit as st
import csv
from utils.export_utils import *
from utils.session_utils import *
from utils.feedback_utils import *
from utils.form_utils import *
import pandas as pd

from utils.quiz_logic import Quiz, User


init_session(quiz = Quiz.from_csv("data/quiz_questions.csv"))

st.title("Test your knowledge")

# Display feedback if present
if st.session_state.feedback is not None:
    msg_type, msg_content = st.session_state.feedback
    if msg_type == "success":
        st.success(msg_content)
    else:
        st.error(msg_content)
    st.session_state.feedback = None

# User details form
if st.session_state.user is None:
  user_form()

# Quiz logic
elif st.session_state.quiz.current_question() is not None:
    q = st.session_state.quiz.current_question()
    st.subheader(q.text)
    answer = st.radio("Choose an answer:", q.possible_answers)
    if st.button("Submit"):
        msg_type, msg_content = give_feedback(st.session_state.quiz ,st.session_state.user,answer)
        st.session_state.feedback= (msg_type, msg_content)
        st.rerun()
    st.write(f"Score: {st.session_state.user.score}")

# Quiz finished
else:
    st.subheader("Quiz Finished!")
    st.write(f"Your final score is {st.session_state.user.score}/{len(st.session_state.quiz.questions)}")
    if not st.session_state.score_saved:
        write_user_scores(st.session_state.user, "user_scores.csv")
    st.session_state.score_saved = True
    csv_data = export_results(st.session_state.user)
    st.download_button(
        label = "Export my answers",
        data = csv_data,
        file_name = "COP_quiz_answers.csv",
        mime = "text/csv"
    )
    if st.button("Restart Quiz"):
        del st.session_state.quiz
        del st.session_state.user
        st.rerun()