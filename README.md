# l6-ifcs-sum2
This is a repo for the second summative assignment for the intensive foundations of computer science module in the L6 data science apprenticeship.

## Introduction

This project was developed within the context of the Department for Education (DfE), specifically reflecting the work of the Statistics Services Unit (SSU) operating alongside the Head of Profession for Statistics (HoP) office within the [Government Statistical Service (GSS)](https://analysisfunction.civilservice.gov.uk/government-statistical-service-and-statistician-group/). This environment involves the production, analysis, and dissemination of official education statistics, with close alignment to professional standards set by the GSS. Staff are expected to apply the UK Code of Practice for Statistics when producing and communicating data to ensure outputs are trustworthy, high quality, and serve the public good.

The quiz application is relevant to the DfE as understanding the Code of Practice is essential for analysts and statisticians working under the leadership of the HoP. Within the Statistics Services Unit, the Code underpins decisions about data quality, transparency, and communication. The quiz supports employer needs by providing an accessible learning resource that can be used for staff development, onboarding, and continuing professional development activities, helping reinforce professional standards in a practical way.

The project was delivered as a Minimum Viable Product (MVP) in order to focus on essential functionality while remaining achievable within time and resource constraints. The MVP includes core features such as multiple choice questions, user input, and feedback, ensuring the application delivers learning value without unnecessary complexity. This reflects common practice in public sector digital and analytical projects, where iterative development is encouraged.

The application has been developed using Streamlit in Python. The repository includes the source code, documentation, and instructions for running the application locally.


## Design Section

### GUI Design
- The application uses Streamlit to provide a web-based graphical user interface (GUI).
- The user journey is as follows:
  1. The user lands on the Home page, which provides an overview and navigation.
  2. The user accesses the "Test your knowledge" page to start the quiz.
  3. A form collects the user's first name, last name, and email, with validation for each field.
  4. The quiz presents one question at a time, with multiple-choice answers using radio buttons.
  5. Immediate feedback is given after each answer (success or error message).
  6. At the end, the user sees their score and can export their answers as a CSV file or restart the quiz.
- The design is simple and accessible, suitable for non-technical users.
- (Optionally, include Figma or prototyping screenshots/links here.)


### Functional Requirements
- The system shall allow users to start a quiz via the GUI.
- The system shall validate user answers and provide immediate feedback.
- The system shall store quiz results in a CSV file.
- The system shall allow administrators to export results.

### Non-Functional Requirements

- The application shall be usable by non-technical staff.
- The system shall respond to user actions within 2 seconds.
- The codebase shall follow PEP 8 conventions.
- The application shall handle invalid input gracefully.
- The app should be accessible and usable on standard web browsers.
- All user data is stored locally in CSV files; no external database is required.
- The app should handle errors gracefully and provide clear feedback to users.

### Tech Stack Outline
- **Languages:** Python 3
- **Framework:** Streamlit (for GUI)
- **Libraries:**
  - pandas (for CSV/question handling)
  - streamlit (for UI and session state)
  - csv, io, re (standard library for file and input handling)
- **Tools:**
  - Figma for prototyping
  - pytest (for testing)
- **Storage:**
  - Quiz questions: CSV file (`data/quiz_questions.csv`)
  - User scores: CSV file (`user_scores.csv`)

### Code Design Document
- The code is organized into modules for logic, forms, feedback, export, and session management.
- **Key Classes:**
  - `Question`: Represents a quiz question, possible answers, correct answer, and aspect/category.
  - `User`: Represents a quiz participant, tracks name, email, score, and answers.
  - `Quiz`: Manages the list of questions, current state, and answer logic.
- **Main Flow:**
  - The app initializes session state and loads questions from CSV.
  - User details are collected and validated.
  - The quiz logic presents questions, records answers, and updates scores.
  - Results are saved and can be exported.
- **Class Diagram (textual):**

```
User
 ├─ first_name: str
 ├─ last_name: str
 ├─ email: str
 ├─ score: int
 └─ answers: list
      └─ {question: Question, answer: str, correct: bool}

Question
 ├─ text: str
 ├─ possible_answers: list
 ├─ correct_answer: str
 └─ aspect: str

Quiz
 ├─ questions: list[Question]
 ├─ current_index: int
 ├─ from_csv(csv_path): Quiz
 ├─ current_question(): Question
 └─ answer_current(answer): (bool, Question)
```

- **Modules:**
  - `app/pages/`: Streamlit page scripts (Home, About, FAQs, Test your knowledge)
  - `app/utils/`: Logic for quiz, forms, feedback, export, and session state
  - `data/`: Quiz questions CSV
  - `tests/`: Unit tests for logic and utilities

## Development Section

This section explains the main parts of the application, with code blocks and descriptions to demonstrate how the system works.

### Main Application Flow

The application is structured as a Streamlit app with multiple pages. The main quiz logic is in `app/pages/Test your knowledge.py`:

```
import streamlit as st
from utils.export_utils import *
from utils.session_utils import *
from utils.feedback_utils import *
from utils.form_utils import *
from utils.quiz_logic import Quiz, User

init_session(quiz = Quiz.from_csv("data/quiz_questions.csv"))

st.title("Test your knowledge")

# Display feedback if present
if st.session_state.feedback is not None:
    msg_type, msg_content = st.session_state.feedback
    if msg_type == "success":
        st.success(msg_content)
    else:
        st.error(msg_content)
    st.session_state.feedback = None

# User details form
if st.session_state.user is None:
    user_form()

# Quiz logic
elif st.session_state.quiz.current_question() is not None:
    q = st.session_state.quiz.current_question()
    st.subheader(q.text)
    answer = st.radio("Choose an answer:", q.possible_answers)
    if st.button("Submit"):
        msg_type, msg_content = give_feedback(st.session_state.quiz, st.session_state.user, answer)
        st.session_state.feedback = (msg_type, msg_content)
        st.rerun()
    st.write(f"Score: {st.session_state.user.score}")

# Quiz finished
else:
    st.subheader("Quiz Finished!")
    st.write(f"Your final score is {st.session_state.user.score}/{len(st.session_state.quiz.questions)}")
    if not st.session_state.score_saved:
        write_user_scores(st.session_state.user, "user_scores.csv")
    st.session_state.score_saved = True
    csv_data = export_results(st.session_state.user)
    st.download_button(
        label = "Export my answers",
        data = csv_data,
        file_name = "COP_quiz_answers.csv",
        mime = "text/csv"
    )
    if st.button("Restart Quiz"):
        del st.session_state.quiz
        del st.session_state.user
        st.rerun()
```

This script manages the user journey: collecting user details, presenting questions, handling answers, providing feedback, and exporting results.

### Core Classes and Logic

#### `Question` Class
Defines a quiz question, possible answers, the correct answer, and its aspect/category.

```
class Question:
    def __init__(self, text, possible_answers, correct_answer, aspect):
        self.text = text
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer
        self.aspect = aspect

    def is_correct(self, answer):
        return answer == self.correct_answer
```

#### `User` Class
Tracks user details, score, and answers.

```
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.score = 0
        self.answers = []

    def record_answer(self, question, answer, correct):
        self.answers.append({"question": question, "answer": answer, "correct": correct})
        if correct:
            self.score += 1
```

#### `Quiz` Class
Manages the list of questions, current state, and answer logic.

```
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0

    @classmethod
    def from_csv(cls, csv_path):
        # Loads questions from a CSV file
        ...

    def current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        else:
            return None

    def answer_current(self, answer):
        question = self.current_question()
        correct = question.is_correct(answer)
        self.current_index += 1
        return correct, question
```

### Utility Modules

- `form_utils.py`: Handles user input forms and validation (e.g., name and email checks).
- `feedback_utils.py`: Provides feedback after each answer.
- `export_utils.py`: Handles saving user scores and exporting answers to CSV.
- `session_utils.py`: Manages Streamlit session state variables.

#### Example: User Form Validation
```
def validate_name(name):
    if len(name) <= 1:
        return False
    if not name.isalnum():
        return False
    return True

def validate_email(email):
    regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
    if re.fullmatch(regex, email):
        return True
    return False
```

### Data Storage
- Quiz questions are stored in `data/quiz_questions.csv`.
- User scores are appended to `user_scores.csv`.

### Testing
- The `tests/` directory contains unit tests for core logic, e.g., `test_quiz_logic.py` and `test_export_utils.py`.

This modular structure ensures the application is maintainable, testable, and easy to extend.

## Testing Section

### 1. Testing Strategy and Methodology

A systematic approach was taken to ensure the reliability and correctness of the application. The following methods were used:

- **Automated Unit Testing:**
  - Core logic modules (such as quiz logic, export utilities, and session management) are covered by automated unit tests using `pytest`.
  - Tests are located in the `tests/` directory and are run automatically in CI (Continuous Integration) using GitHub Actions.
  - Automated tests ensure that individual functions and classes behave as expected and help prevent regressions.

- **Manual Testing:**
  - The application was manually tested through the Streamlit GUI to verify the user journey, input validation, feedback, and data export features.
  - Manual tests focused on usability, error handling, and the overall user experience.

This combination of automated and manual testing provides both code-level assurance and real-world validation.

### 2. Outcomes of Application Testing

#### 2.1. Manual Test Outcomes

| Test Case Description                                 | Steps Taken                                      | Expected Result                | Actual Result   | Pass/Fail |
|------------------------------------------------------|--------------------------------------------------|-------------------------------|-----------------|-----------|
| Start quiz and submit valid user details              | Enter valid name and email, start quiz            | Quiz starts                    | Quiz starts     | Pass      |
| Submit invalid email                                 | Enter invalid email, submit form                  | Warning shown, cannot proceed  | Warning shown   | Pass      |
| Answer quiz questions                                | Select answers, submit each                      | Feedback after each answer     | Feedback shown  | Pass      |
| Complete quiz and export answers                     | Finish quiz, click export                        | CSV download prompt appears    | Prompt appears  | Pass      |
| Restart quiz                                         | Click restart after finishing                    | Quiz restarts, form resets     | Works as expected| Pass      |
| Submit empty form                                    | Leave fields blank, submit                       | Warning shown                  | Warning shown   | Pass      |
| Handle invalid input gracefully                      | Enter special characters in name/email            | Warning shown                  | Warning shown   | Pass      |

#### 2.2. Unit Testing Outcome

Automated unit tests were run using `pytest`. Below is an example screenshot of the tests running and passing:

![Unit Test Results](docs/unit_test_results.png)

- All core logic tests (quiz logic, export, session utils) passed successfully.
- Tests are re-run automatically on every code push via GitHub Actions CI.

If any test fails, details are shown in the CI logs and locally in the terminal, allowing for quick identification and resolution of issues.

## Documentation Section

### User Documentation

#### How to Use the Quiz Application
1. **Access the Application:**
   - Open the application in your web browser (typically via a provided Streamlit link or by running locally).
2. **Home Page:**
   - Read the introduction and user guide for an overview of the quiz and navigation instructions.
3. **Start the Quiz:**
   - Go to the "Test your knowledge" page.
   - Enter your first name, last name, and email address in the form. All fields are required and validated.
   - Click "Start Quiz" to begin.
4. **Answer Questions:**
   - For each question, select your answer and click "Submit".
   - Immediate feedback will be shown after each answer.
   - Your current score is displayed throughout the quiz.
5. **Finish and Export:**
   - At the end, your final score is shown.
   - You can download your answers as a CSV file for your records.
   - Click "Restart Quiz" to retake the quiz if desired.

#### Troubleshooting
- If you see a warning or error, check that all form fields are filled in correctly.
- If the application does not load, ensure you have a stable internet connection or contact your IT support.

### Technical Documentation

#### Running the Application Locally
1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd l6-ifcs-sum2
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Start the Application:**
   ```sh
   streamlit run app/Home.py
   ```
   - Use the Streamlit sidebar to navigate between pages.

#### Running Tests Locally
1. **Install Test Dependencies:**
   - Ensure `pytest` is installed (included in requirements or install via `pip install pytest`).
2. **Run All Tests:**
   ```sh
   pytest
   ```
   - Test files are located in the `tests/` directory.
   - Test results will be displayed in the terminal.

#### Code Structure Overview
- `app/pages/`: Streamlit page scripts (Home, About, FAQs, Test your knowledge)
- `app/utils/`: Core logic modules (quiz logic, forms, feedback, export, session state)
- `data/`: Quiz questions CSV file
- `tests/`: Unit tests for logic and utilities
- `user_scores.csv`: Stores quiz results
- `requirements.txt`: Python dependencies

#### Key Code Components
- **Quiz Logic:** Handles question loading, answer checking, and quiz progression (`quiz_logic.py`).
- **User Management:** Collects and validates user details (`form_utils.py`).
- **Feedback:** Provides immediate feedback after each answer (`feedback_utils.py`).
- **Export:** Saves and exports user results (`export_utils.py`).
- **Session State:** Manages user and quiz state across the app (`session_utils.py`).

For further technical details, see the comments and docstrings within each module.


## Evaluation Section

### What Went Well

The development of this project was a valuable learning experience, particularly in applying [Streamlit](https://streamlit.io/) to create an interactive and accessible web application. The modular structure of the codebase, with clear separation of concerns (logic, forms, feedback, export, and session management), made the project easier to maintain and extend. Leveraging [pandas](https://pandas.pydata.org/) for CSV handling streamlined data operations, and the use of Python’s standard library kept dependencies minimal. The quiz application met its core objectives as a Minimum Viable Product, providing a user-friendly interface, immediate feedback, and exportable results. Unit tests were implemented for key logic components, which helped ensure reliability and catch regressions early.

### What Could Have Been Improved

While the MVP approach allowed for timely delivery, there were areas where the project could be enhanced. The user interface, though functional, could benefit from more advanced design and accessibility features—potentially by incorporating more feedback from end users or using prototyping tools like [Figma](https://www.figma.com/). Error handling, while present, could be made more robust, especially for edge cases such as malformed CSV files or unexpected user input. Automated testing coverage could be expanded to include the GUI and integration tests, not just unit tests. Additionally, implementing persistent user authentication or a database backend (such as [SQLite](https://www.sqlite.org/index.html)) could improve scalability and data integrity for future versions. Finally, more comprehensive documentation and user guides would further support onboarding and maintenance.