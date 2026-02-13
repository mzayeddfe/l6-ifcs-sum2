import tempfile
import csv
import os
from app.utils.quiz_logic import User, Question
from app.utils.export_utils import write_user_scores, export_results

def test_write_user_scores():
    """
    Test that write_user_scores correctly writes a user's score to a CSV file.
    """
    # Create a test user
    user = User("Test", "User", "test@example.com")
    user.score = 5

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='') as tmpfile:
        tmpfile_name = tmpfile.name

    # Patch the function to write to the temp file instead of the real one
    
    write_user_scores(user, file_name=tmpfile_name)

    # Read back the file and check contents
    with open(tmpfile_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["first_name"] == "Test"
        assert rows[0]["last_name"] == "User"
        assert rows[0]["email"] == "test@example.com"
        assert rows[0]["score"] == "5"

    # Clean up
    os.remove(tmpfile_name)


def test_export_results():
    """
    Test that export_results returns a CSV string containing the user's answers.
    """
    user = User("Test", "User", "test@example.com")
    q1 = Question(
        text="What is 1+1?",
        possible_answers=["1", "2", "3", "4"],
        correct_answer="2",
        aspect="maths"
    )
    q2 = Question(
        text="What is 2+2?",
        possible_answers=["1", "2", "3", "4"],
        correct_answer="4",
        aspect="maths"
    )

    user.record_answer(q1, "2", True)
    user.record_answer(q1, "3", False)

    csv_data = export_results(user)

    assert "What is 1+1?" in csv_data
    assert "True" in csv_data