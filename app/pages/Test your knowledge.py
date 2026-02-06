import streamlit as st
from utils.quiz_logic import *
from utils.ui_components import *
from utils.data_utils import *
import csv
import os

#load in data


with st.spinner("Loading quiz ..."):
    quiz_questions = load_questions()
# Initialise session state variables 

init_session_state(quiz_questions)
# Ensure score_saved is initialized
if "score_saved" not in st.session_state:
    st.session_state.score_saved = False
            

# Main quiz page 


st.title("Test your knowledge")

csv_file = "user_scores.csv"
fieldnames = ["first_name", "last_name","email", "score", "answers"]

# Show quiz finished screen
if st.session_state.quiz_finished:
    if not st.session_state.score_saved:
        file_exists = os.path.isfile(csv_file)
        with open(csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(st.session_state.user_data)
        st.session_state.score_saved = True
    st.subheader("Quiz finished!")
    st.write(f"Your final score is {st.session_state.score}/{len(st.session_state.questions_dict)}")
    restart_quiz_fragment()
# Show user form if quiz not started
elif st.session_state.quiz_started == False:
    # Reset score_saved so next quiz can be saved
    st.session_state.score_saved = False
    user_details_section()
# Show questions if quiz started and current_question is valid
elif st.session_state.quiz_started == True and st.session_state.current_question is not None:
    question_fragment()
    score_feedback_fragment()


