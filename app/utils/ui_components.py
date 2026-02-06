import streamlit as st



def user_details_section():
    
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

# start feedback fragment 


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

 

def score_fragment():
    """
    Fragment to display the user's score 
    """

    st.metric("Current score", st.session_state.score)


def score_feedback_fragment():
    """
    Fragment to put feedback and score side by side in columns
    """
    feedback_col,score_col = st.columns(2)
    with feedback_col: 
        feedback_fragment()
    with score_col: 
        score_fragment()


