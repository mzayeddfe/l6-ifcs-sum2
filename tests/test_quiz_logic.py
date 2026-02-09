import pytest
from app.utils.quiz_logic import Question

def test_question_is_correct():
    q = Question(
        text = "What is 1+1?",
        possible_answers = ["1","2","3","4"],
        correct_answer = "2",
        aspect = "maths"
    )

    assert q.is_correct("2") is True
    assert q.is_correct("4") is False

    