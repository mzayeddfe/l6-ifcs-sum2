import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from app.utils.quiz_logic import read_format_quiz_qs

import pytest 

# test that the question dataset has 4 columns 

def test_col_count():
    questions_bank = read_format_quiz_qs("quiz_questions.csv")
    num_cols = len(questions_bank.columns)
    assert num_cols == 4

# test that the data type in all the columns are strings 


def test_data_type():
    questions_bank = read_format_quiz_qs("quiz_questions.csv")
    for col, dtype in questions_bank.dtypes.items():
        assert dtype == "object"

# check the number of questions
def test_num_questions():
    questions_bank = read_format_quiz_qs("quiz_questions.csv")
    unique_qs = len(questions_bank["question"].unique())
    assert unique_qs  == 12
