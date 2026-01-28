import streamlit as st


st.set_page_config(
    page_title="Code of practice knowledge checker",
    page_icon= "📖"
)

st.title("Code of practice knowledge checker")

# page content 

st.markdown("## User guide")


st.markdown("This is an app to test your knowledge on the code of practice for statistics. " \
"This app contains a test to check your knowledge, information about the code of statistics, " \
"frequently asked questions and resources to help.")

st.markdown("### How can I take the quiz?")

st.markdown("""You can take the quiz by clicking the “Start” button below or accessing it through the side navigation. Then work  your way through the 
           questions and find out your score.""")

st.markdown("## Where can I find more information?")

st.markdown("""
            -  Find out more about the code of practice using the “About this quiz” page.
            -  Find out frequently asked questions and their answers in the FAQs
            """)
st.sidebar.success("Select a page to show")
