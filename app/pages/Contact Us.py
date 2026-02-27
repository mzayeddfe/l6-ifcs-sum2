import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon="📧")

st.title("Contact Us")

st.sidebar.image("images/duck_guidance.png")

st.markdown("""
If you have questions, feedback, or need support regarding the Code of Practice Quiz app, please reach out using the mailbox below:

**Email:** [statistics.development@education.gov.uk](mailto:statistics.development@education.gov.uk)
            
We aim to respond within 3 working days.


---

Alternatively, you can submit your query using the form below:
""")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        if not name or not email or not message:
            st.error("Please fill in all fields before submitting.")
        else:
            st.success("Thank you for your message! We will get back to you soon.")
