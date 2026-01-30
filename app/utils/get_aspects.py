def get_aspects(data_file):
    from app.utils.read_format_questions import read_format_quiz_qs
    questions_file = read_format_quiz_qs(data_file)
    aspects = questions_file["aspect"]
    aspects = aspects.unique()
    return (aspects)