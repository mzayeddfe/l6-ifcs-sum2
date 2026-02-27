import csv
import streamlit as st
import io

def write_user_scores(user, file_name):
    """
    Append a user's score and details to a CSV file.
    Args:
        user (User): The user whose score is being recorded.
        file_name (str): The path to the CSV file.
    """
    try:
        # Open the CSV file in append mode
        with open(file_name, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["first_name", "last_name", "email", "score"])
            # Write header if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
            # Write user details and score as a new row
            writer.writerow({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "score": user.score
            })
    except Exception as e:
        # Show error in Streamlit if writing fails
        st.error(f"An unexpected error occurred: {e}")




def export_results(user):
    """
    Export a user's quiz answers as a CSV string.
    Args:
        user (User): The user whose answers are being exported.
    Returns:
        str: CSV data as a string.
    """
    # Try to export user answers to CSV string, handle errors gracefully
    try:
        export_rows = []
        # Loop through each answer and prepare row for CSV
        for ans in user.answers:
            export_rows.append({
                "question": ans["question"].text,  # Get question text
                "aspect": ans["question"].aspect,  # Get question aspect/category
                "your_answer": ans["answer"],      # User's answer
                "correct": ans["correct"]           # Whether answer was correct
            })
        # Create CSV in memory using StringIO
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=["question", "aspect", "your_answer", "correct"])
        writer.writeheader()
        writer.writerows(export_rows)
        # Return CSV data as string
        return output.getvalue()
    except Exception as e:
        # Return empty string if export fails
        return ""
        