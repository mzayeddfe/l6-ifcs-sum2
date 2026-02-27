
import streamlit as st

# Set page configuration for title and icon
st.set_page_config(page_title="Contact Us", page_icon="📧")

# Main page title
st.title("Contact Us")

# Show branding image in sidebar
st.sidebar.image("images/duck_guidance.png")

# Display contact instructions and support email
st.markdown("""
If you have questions, feedback, or need support regarding the Code of Practice Quiz app, please reach out using the mailbox below:

**Email:** [statistics.development@education.gov.uk](mailto:statistics.development@education.gov.uk)
            
We aim to respond within 3 working days.

""")
