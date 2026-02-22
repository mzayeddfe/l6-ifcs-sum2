import streamlit as st

st.set_page_config(
	page_title="Code of Practice Quiz",
	page_icon="📖"
)

st.title("Code of Practice Quiz")

# --- Table of Contents ---
st.markdown("""
## Table of Contents
- [User Guide](#user-guide)
- [About the Code of Practice](#about-the-code-of-practice)
- [Frequently Asked Questions](#frequently-asked-questions)
""")

# --- User Guide Section ---

st.markdown("## User Guide")
st.markdown("""
Welcome to the Code of Practice Quiz app! This tool helps you test your knowledge of the UK Code of Practice for Statistics. The app includes:
- An interactive quiz to check your understanding
- Information about the Code of Practice
- Frequently asked questions and helpful resources

### How to Take the Quiz
To start the quiz, select the “Test your knowledge” page from the sidebar. Answer each question and see your score update as you progress. At the end, you can export your answers as a CSV file.

### Where to Find More Information
- Learn more about the Code of Practice in the section below.
- See answers to common questions in the FAQ section.

### Troubleshooting
If you encounter any issues (such as the app not loading or form validation errors), check your internet connection and ensure all fields are filled in correctly. For further help, contact your IT support.

### Privacy Notice
This app is currently not deployed and is only run locally for demonstration or development purposes. No user information (such as your name, email, or quiz answers) will be stored or shared. Your privacy is fully protected, and no data is retained after you close the app.
""")

# --- About the Code of Practice Section ---
st.markdown("## About the Code of Practice")
st.markdown("""The Code of Practice for Statistics is a set of standards and principles designed to ensure that official statistics published in the UK are trustworthy, high quality, and valuable to everyone who uses them. 
This applies to anyone from decision-makers and analysts to members of the public.""")

st.markdown("### What is the Code of Practice?")
st.markdown("""The Code sets out how statistics should be produced and communicated so they serve the public good. 

It was created under UK law and maintained by the Office for Statistics Regulation, part of the UK Statistics Authority. 

When producers follow the Code, users can be confident that the statistics are reliable, transparent and free from inappropriate influence.

While the Code applies formally to official statistics produced by government bodies, its core ideas can be helpful for anyone working with data and statistics, for example, journalists or researchers.""")

st.markdown("### Why the Code Matters")
st.markdown("""The Code exists to strengthen trust in statistics by promoting:

-   Trustworthiness – users can be confident in who produced the statistics and how decisions were made.
-   Quality – statistics are based on suitable data and sound methods.
-   Value – statistics meet user needs and are accessible and useful.

By following these principles, statistics help inform better decision-making, support public accountability, and reduce confusion or misuse of data.""")

st.markdown("### Who Uses It?")
st.markdown("""The Code is officially required for organisations producing National Statistics, such as the Department for Education. 
This includes public bodies, analysts, communicators and anyone who wants to demonstrate good data practice.""")

st.markdown("### How to Find Out More")
st.markdown("""If you want to explore the Code in more detail or learn how it’s applied:
-   Visit [the official Code of Practice for Statistics site](https://code.statisticsauthority.gov.uk/).
""")

# --- FAQ Section ---
st.markdown("# Frequently Asked Questions")

st.markdown("## Who is this quiz for?")
st.markdown("""This quiz is designed for civil servants especially in the Department for Education to ensure they understand the Code of Practice.

It can also be used anyone who is interested in data and statistics including:
-   Students and learners exploring statistics
-   Analysts and researchers seeking to test their knowledge
-   Members of the Government Statistical Service (GSS) refreshing their understanding""")

st.markdown("## How does this quiz relate to the Government Statistical Service (GSS)?")
st.markdown("""The GSS is the professional network for statisticians across UK government. Many roles within the GSS require familiarity with the Code. This quiz can help:
-   Prepare for GSS assessments
-   Refresh knowledge before official training or CPD activities
-   Understand practical scenarios where the Code applies""")

st.markdown("## What is a “badged” statistician and why does it matter?")
st.markdown("""Within the GSS, some roles require individuals to be “badged”, meaning they’ve been formally assessed as meeting professional standards in statistical practice.
Being badged:
-   Demonstrates professional competence
-   Shows you understand how to apply the Code in real-world contexts
-   May be linked to career progression within the GSS""")
