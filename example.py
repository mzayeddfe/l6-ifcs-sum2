import streamlit as st
from app.utils.create_questions_dict import create_questions_dict

# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = create_questions_dict("quiz_questions.csv")


if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = None

@st.fragment
def question_fragment():
    """
        Fragment to display a question and capture the user's response.
    """
    question_data = st.session_state.questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1}/{len(st.session_state.questions)}")
    st.write(question_data['question'])

    selected_option = st.radio('Choose an answer: ', question_data['possible_answers'])
    if st.button('Submit'):
        if selected_option == question_data['correct_answer']:
            st.session_state.feedback = ('success', 'Correct! 🎉')
            st.session_state.score += 1
        else:
            st.session_state.feedback = ("error", f"Wrong! The correct answer was: {question_data['correct_answer']}")

        if st.session_state.current_question + 1 < len(st.session_state.questions):
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.current_question = None
            st.rerun()

@st.fragment
def feedback_fragment():
    """
    Fragment to display feedback messages.
    """
    if st.session_state.feedback:
        msg_type, msg_content = st.session_state.feedback
        if msg_type == "success":
            st.success(msg_content)
        elif msg_type == "error":
            st.error(msg_content)
        st.session_state.feedback = None

@st.fragment
def score_fragment():
    """
        Fragment to display the user’s current score.
    """
    st.metric('Current Score', st.session_state.score)

@st.fragment
def restart_quiz_fragment():
    """
        Fragment to restart the quiz.
    """
    if st.button('Restart Quiz'):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.feedback = None
        st.rerun()

# Main application
st.title('Interactive Quiz App')

feedback_fragment()

if st.session_state.current_question is not None:
    score_fragment()
    question_fragment()
else:
    st.subheader('Quiz Finished! 🎉')
    st.write(f"Your final score is {st.session_state.score}/{len(st.session_state.questions)}.")
    restart_quiz_fragment()