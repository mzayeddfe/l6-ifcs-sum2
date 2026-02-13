import streamlit as st
def give_feedback(quiz, user,answer):
    """
    Evaluate the user's answer, update their record, and return feedback message.
    Args:
        quiz (Quiz): The current quiz instance.
        user (User): The user taking the quiz.
        answer (str): The answer provided by the user.
    Returns:
        tuple: (str, str) feedback type and message.
    """
    correct, question = quiz.answer_current(answer)
    user.record_answer(question, answer, correct)
    if correct:
        return  ("success", "Correct! 🎉")
    else:
       return ("error", f"Incorrect! The correct answer was: {question.correct_answer}")
    
