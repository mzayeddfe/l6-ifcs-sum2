

def read_format_quiz_qs(data_file):
    import pandas as pd
    import os

    # Get the absolute path to the CSV file, regardless of where the script is run from
    script_dir = os.path.dirname(os.path.abspath(__file__))
    questions_file_path = os.path.join(script_dir,'..',  '..', 'data', data_file)
    questions_file_path = os.path.abspath(questions_file_path)
    #print(questions_file_path)

    questions_bank = pd.read_csv(questions_file_path)

    questions_bank[['question', 'possible_answers', 'answer_indicator','aspect']] = questions_bank[['question', 'possible_answers', 'answer_indicator','aspect']] .astype(str)
    
    return(questions_bank)


'''questions_bank = read_format_quiz_qs("quiz_questions.csv")

print(questions_bank.info())

#read_format_quiz_qs("quiz_questions.csv")'''