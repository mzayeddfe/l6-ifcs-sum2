import streamlit as st
from utils.quiz_logic import create_questions_dict, assess_answer, reset_quiz_state
import csv
import os
# Initialise session state variables 

# initialize session for the user details
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False
if "user_details" not in st.session_state:
    st.session_state.user_details = None

# initialize session for user details to store and export

if "user_data" not in st.session_state:
    st.session_state["user_data"] = {
        "first_name": "",
        "last_name":"",
        "email": "",
       # "answers": [],
        "score": 0
    }
csv_file = "user_scores.csv"
fieldnames = ["first_name", "last_name","email", "score", "answers"]

# initialize variables for the quiz 
# initialize questions dict

if "questions_dict" not in st.session_state:
    st.session_state.questions_dict = create_questions_dict("quiz_questions.csv")

# Initialise current question 

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# initialise score 

if "score" not in st.session_state:
    st.session_state.score = 0

# initialise feedback 

if "feedback" not in st.session_state: 
    st.session_state.feedback = None 

@st.fragment()

def user_fragment():

    first_name_col, last_name_col= st.columns(2)
    with first_name_col: 
        first_name_input =st.text_input("First Name")
    with last_name_col: 
        last_name_input =st.text_input("Last Name")

    user_email = st.text_input("Email address")

    #updating the details to store them

    st.session_state["user_data"]["first_name"] = first_name_input
    st.session_state["user_data"]["last_name"] = last_name_input
    st.session_state["user_data"]["email"] = user_email



    if st.button("Start quiz!"):
        if len(first_name_input) == 0 or len(last_name_input) == 0 or len(user_email) == 0:
            st.warning("Please fill in all fields to start the quiz.")
            st.session_state.quiz_started = False
        else:
            st.session_state.quiz_started = True
            st.session_state.current_question = 0
            st.session_state.quiz_finished = False
            st.rerun()

# Use fragments for functions for  different sections of the quiz session 

@st.fragment

def question_fragment():
    """
    Use this fragment to display a question and capture the user's response 
    """

    if st.session_state.quiz_started == True and st.session_state.current_question is not None:
        # put a gap between the header and the questions 
        gap = st.markdown("\n")
        current_q = st.session_state.current_question
        # Guard: only access if current_q is a valid integer
        if isinstance(current_q, int) and 0 <= current_q < len(st.session_state.questions_dict):
            question_data = st.session_state.questions_dict[current_q]
            # display question
            st.write(question_data["question"])

            # display answer options as radio buttons
            selected_answer = st.radio("Choose an answer: ", question_data["possible_answers"])
            st.session_state.selected_answer = selected_answer

            # create a submit button with if statements for answer assessment
            if st.button("Submit"):
                feedback, score_update = assess_answer(selected_answer, question_data)
                st.session_state.feedback = feedback
                st.session_state.score += score_update
                st.session_state["user_data"]["score"] = st.session_state.score

                # If there are more questions remaining, increment the current question index
                if st.session_state.current_question + 1 < len(st.session_state.questions_dict):
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    # End the quiz by setting quiz_finished True and current_question to None
                    st.session_state.quiz_started = False
                    st.session_state.current_question = None
                    st.session_state.quiz_finished = True
                    st.rerun()
        else:
            st.session_state.quiz_started = False
            st.session_state.current_question = None
            
# start feedback fragment 

@st.fragment

def feedback_fragment():
    """
    Fragment to display feedback messages to users as they progress through the quiz
    """
    if st.session_state.feedback:
        msg_type, msg_content = st.session_state.feedback
        if msg_type == "success":
            st.success(msg_content)
        else:
            st.error(msg_content)
        st.session_state.feedback = None

@st.fragment 

def score_fragment():
    """
    Fragment to display the user's score 
    """

    st.metric("Current score", st.session_state.score)

@st.fragment 

def score_feedback_fragment():
    """
    Fragment to put feedback and score side by side in columns
    """
    feedback_col,score_col = st.columns(2)
    with feedback_col: 
        feedback_fragment()
    with score_col: 
        score_fragment()

@st.fragment 

def restart_quiz_fragment():
    """
    Fragment to restart the quiz
    """

    if st.button("Restart Quiz"):
        reset_quiz_state(st.session_state)
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.session_state.quiz_finished = False
        st.rerun()
    
# Main quiz page 


st.title("Test your knowledge")

# Show quiz finished screen
if st.session_state.quiz_finished:
    # Check if file exists to write header
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(st.session_state.user_data)
    st.subheader("Quiz finished!")
    st.write(f"Your final score is {st.session_state.score}/{len(st.session_state.questions_dict)}")
    restart_quiz_fragment()
# Show user form if quiz not started
elif st.session_state.quiz_started == False:
    user_fragment()
# Show questions if quiz started and current_question is valid
elif st.session_state.quiz_started == True and st.session_state.current_question is not None:
    question_fragment()
    score_feedback_fragment()


