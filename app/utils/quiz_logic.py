
import pandas as pd

class Question:
     def __init__(self, text, possible_answers, correct_answer, aspect):
        self.text = text
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer
        self.aspect = aspect

     def is_correct(self, answer):
        return answer == self.correct_answer


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.score = 0
        self.answers = []

    def record_answer(self, question, answer, correct):
        self.answers.append({"question": question,
                            "answer": answer,
                            "correct": correct})
        if correct:
            self.score += 1

class Quiz:
    def __init__(self,questions):
        self.questions = questions 
        self.current_index = 0

    @classmethod

    def from_csv(cls,csv_path):
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

        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        else:
            return None

    def answer_current(self,answer):
        question = self.current_question()
        correct = question.is_correct(answer)
        self.current_index += 1
        return correct, question
