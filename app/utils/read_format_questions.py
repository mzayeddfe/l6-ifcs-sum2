import pandas as pd
import os

# Get the absolute path to the CSV file, regardless of where the script is run from
script_dir = os.path.dirname(os.path.abspath(__file__))
questions_file_path = os.path.join(script_dir,'..',  '..', 'data', 'quiz_questions.csv')

questions_bank = pd.read_csv(questions_file_path)

# Source - https://stackoverflow.com/a
# Posted by sudonym, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-28, License - CC BY-SA 4.0

questions_bank[['question', 'possible_answers', 'answer_indicator','aspect']] = questions_bank[['question', 'possible_answers', 'answer_indicator','aspect']] .astype(str)
# add as many column names as you like.


print(questions_bank.info())

def read_format_quiz_qs(data_file):
    print("hello")



