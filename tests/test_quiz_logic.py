import pytest
from app.utils.quiz_logic import *

# test different classes in the quiz logic work as expected 

#testing the question class 

def test_question_is_correct():
    q = Question(
        text = "What is 1+1?",
        possible_answers = ["1","2","3","4"],
        correct_answer = "2",
        aspect = "maths"
    )

    assert q.is_correct("2") is True
    assert q.is_correct("4") is False

#test user class 

def test_user_record_answer():
    user_info = User(
        first_name = "John",
        last_name = "Doe",
        email = "john.doe@gmail.com"
    )

    q = Question(
        text="What is 1+1?",
        possible_answers=["1", "2", "3", "4"],
        correct_answer="2",
        aspect="maths"
    )

    #test for correct answers
    user_info.record_answer(q,"2",True)
    assert user_info.score == 1
    assert user_info.answers[-1]["answer"]=="2"
    assert user_info.answers[-1]["correct"] is True

    # test for incorrect answers
    user_info.record_answer(q,"1", False)
    assert user_info.score == 1
    assert user_info.answers[-1]["answer"] == "1"
    assert user_info.answers[-1]["correct"] is False
        

def test_quiz_from_csv():
    csv_path = "data/quiz_questions.csv"

    result=Quiz.from_csv(csv_path)

    assert isinstance(result, Quiz)
    assert len(result.questions)>0


def test_quiz_current_question():
    csv_path = "data/quiz_questions.csv"

    quiz=Quiz.from_csv(csv_path)
    quiz.current_index= 5
    expected_question = quiz.questions[5]
    assert quiz.current_question() == expected_question



def test_answer_current():
    quiz = Quiz.from_csv("data/quiz_questions.csv")
    quiz.current_index = 0
    question = quiz.current_question()
    correct_answer = question.correct_answer
    wrong_answer = [a for a in question.possible_answers if a != correct_answer][0]

    # Test correct answer
    was_correct, returned_question = quiz.answer_current(correct_answer)
    assert was_correct is True
    assert returned_question == question
    assert quiz.current_index == 1

    # Test incorrect answer
    question2 = quiz.current_question()
    was_correct2, returned_question2 = quiz.answer_current(wrong_answer)
    assert was_correct2 is False
    assert returned_question2 == question2
    assert quiz.current_index == 2

    
