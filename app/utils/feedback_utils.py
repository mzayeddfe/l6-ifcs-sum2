import streamlit as st
def give_feedback(quiz, user,answer):
    correct, question = quiz.answer_current(answer)
    user.record_answer(question, answer, correct)
    if correct:
        return  ("success", "Correct! 🎉")
    else:
       return ("error", f"Incorrect! The correct answer was: {question.correct_answer}")
    
