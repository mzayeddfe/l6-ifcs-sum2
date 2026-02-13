
import pandas as pd

class Question:
    """
    Represents a quiz question with possible answers and the correct answer.
    """
    def __init__(self, text, possible_answers, correct_answer, aspect):
        """
        Initialize a Question instance.
        Args:
            text (str): The question text.
            possible_answers (list): List of possible answers.
            correct_answer (str): The correct answer.
            aspect (str): The aspect/category of the question.
        """
        self.text = text
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer
        self.aspect = aspect

    def is_correct(self, answer):
        """
        Check if the provided answer is correct.
        Args:
            answer (str): The answer to check.
        Returns:
            bool: True if correct, False otherwise.
        """
        return answer == self.correct_answer


class User:
    """
    Represents a user taking the quiz, tracking their details and answers.
    """
    def __init__(self, first_name, last_name, email):
        """
        Initialize a User instance.
        Args:
            first_name (str): User's first name.
            last_name (str): User's last name.
            email (str): User's email address.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.score = 0
        self.answers = []

    def record_answer(self, question, answer, correct):
        """
        Record an answer for the user and update score if correct.
        Args:
            question (Question): The question answered.
            answer (str): The user's answer.
            correct (bool): Whether the answer was correct.
        """
        self.answers.append({"question": question,
                            "answer": answer,
                            "correct": correct})
        if correct:
            self.score += 1

class Quiz:
    """
    Manages the quiz, including questions, current state, and answer logic.
    """
    def __init__(self,questions):
        """
        Initialize a Quiz instance.
        Args:
            questions (list): List of Question objects.
        """
        self.questions = questions 
        self.current_index = 0

    @classmethod

    def from_csv(cls,csv_path):
        """
        Create a Quiz instance from a CSV file of questions.
        Args:
            csv_path (str): Path to the CSV file.
        Returns:
            Quiz: An instance of the Quiz class.
        """
        df = pd.read_csv(csv_path)
        questions = []
        for q_text in df["question"].unique():
            q_df = df[df["question"]== q_text]
            possible_answers = list(q_df["possible_answers"])
            correct_answer = q_df[q_df["answer_indicator"]== "c"]['possible_answers'].iloc[0]
            aspect= q_df["aspect"].iloc[0]
            questions.append(Question(q_text,possible_answers,correct_answer, aspect))
        return cls(questions)
    
    def current_question(self):
        """
        Get the current question in the quiz.
        Returns:
            Question or None: The current Question object or None if finished.
        """

        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        else:
            return None

    def answer_current(self,answer):
        """
        Answer the current question and advance the quiz.
        Args:
            answer (str): The answer provided by the user.
        Returns:
            tuple: (bool, Question) indicating if correct and the question object.
        """
        question = self.current_question()
        correct = question.is_correct(answer)
        self.current_index += 1
        return correct, question
