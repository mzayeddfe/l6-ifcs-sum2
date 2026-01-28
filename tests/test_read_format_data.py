from app.utils.read_format_questions import read_format_quiz_qs

import pytest 

# test that the question dataset has 4 columns 

def test_check_col_count():
    questions_bank = read_format_quiz_qs("quiz_questions.csv")
    num_cols = len(questions_bank.columns)
    assert num_cols == 4

# test that the data type in all the columns are strings 

# check the number of questions

