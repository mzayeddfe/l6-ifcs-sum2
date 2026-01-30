# function to read and format quiz data from CSV file
def read_format_quiz_qs(data_file):
    """
    Reads a CSV file containing quiz questions and formats the data for further processing.
    The function constructs the absolute path to the CSV file located in the 'data' directory,
    reads the file into a pandas DataFrame, and ensures that the columns 'question',
    'possible_answers', 'answer_indicator', and 'aspect' are of string type.
    Args:
        data_file (str): The name of the CSV file containing the quiz questions.
    Returns:
        pandas.DataFrame: A DataFrame containing the formatted quiz questions.
    """
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

# function to put questions data into a dictionary for easier processing 
def create_questions_dict(data_file):
    """
    Reads quiz question data from the specified file, processes it, and returns a list of dictionaries,
    each representing a unique question with its possible answers and correct answer(s).
    Args:
        data_file (str): Path to the data file containing quiz questions.
    Returns:
        list[dict]: A list of dictionaries, where each dictionary has the following keys:
            - "question" (str): The question text.
            - "possible_answers" (np.ndarray or list): The possible answers for the question.
            - "correct_answer" (np.ndarray or list): The correct answer(s) for the question.
    Note:
        This function relies on the external function `read_format_quiz_qs` to read and format the quiz questions.
    """
    # read in the data 
    #from utils.read_format_questions import read_format_quiz_qs

    questions_bank = read_format_quiz_qs(data_file)

    # breakdown the data to its different parts in a dictionary 

    # get unique question first 

    unique_questions =questions_bank["question"].unique()

    # get answers for each question 
    questions_dict_list = []

    for question in unique_questions:
        # get the aspect 

        aspect = questions_bank[questions_bank["question"]== question]
        aspect = aspect["aspect"].unique()

        #get possible answers 

        possible_answers =  questions_bank[questions_bank["question"]== question]
        possible_answers = possible_answers["possible_answers"].unique()

        # get correct answer

        correct_answer =  questions_bank[questions_bank["question"]== question]
        correct_answer = correct_answer[correct_answer["answer_indicator"]=="c"]
        correct_answer = correct_answer["possible_answers"].unique()

        questions_dict = { "question" : question,
                          "possible_answers": possible_answers,
                          "correct_answer": correct_answer}
        
        # append results 
        questions_dict_list.append(questions_dict)
    return (questions_dict_list)


def assess_answer(selected_answer, question_data):
    """
    Evaluates the user's selected answer against the correct answer for a quiz question.

    Args:
        selected_answer (str): The answer selected by the user.
        question_data (dict): A dictionary containing question details, including the key "correct_answer".

    Returns:
        tuple: A tuple containing:
            - A tuple (status, message):
                - status (str): "success" if the answer is correct, "error" otherwise.
                - message (str): Feedback message indicating correctness and, if incorrect, the correct answer.
            - int: 1 if the answer is correct, 0 otherwise.
    """
    # if the answer submitted is correct, give an indicative feedback message and add 1 to the score
    if selected_answer == question_data["correct_answer"]:
        return ("success", "Correct! 🎉"), 1
    # otherwise, give feedback that the answer was incorrect and provide the correct answer    
    else:
        return ("error", f"Incorrect! The correct answer was: {question_data['correct_answer']}"), 0

def reset_quiz_state(session_state):
    """
    Resets the quiz-related state variables in the provided session_state object.

    Parameters:
        session_state: An object (typically a Streamlit session state) containing quiz state variables.
            - current_question: Index of the current question.
            - score: User's current score.
            - feedback: Feedback message for the last answered question.
            - selected_answer: The answer selected by the user for the current question.

    This function sets the quiz state to its initial values, preparing for a new quiz session.
    """
    session_state.current_question = None
    session_state.score = 0
    session_state.feedback = None
    session_state.selected_answer = None
    session_state.quiz_started = False