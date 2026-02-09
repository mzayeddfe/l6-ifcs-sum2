import csv
import streamlit as st
import io
def write_user_scores(user):
    with open("user_scores.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["first_name", "last_name", "email", "score"])
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "score":user.score
            })



def export_results(user):
    export_rows = []
    for ans in user.answers:
        export_rows.append({
            "question": ans["question"].text,
            "aspect": ans["question"].aspect,
            "your_answer": ans["answer"],
            "correct": ans["correct"]
        })
    
    #create csv in emory 
    output =io.StringIO()
    writer= csv.DictWriter(output,
    fieldnames=["question","aspect","your_answer","correct"])
    writer.writeheader()
    writer.writerows(export_rows)
    csv_data = output.getvalue()
    st.download_button(
        label = "Export my answers",
        data = csv_data,
        file_name = "COP_quiz_answers.csv",
        mime = "text/csv"
    )