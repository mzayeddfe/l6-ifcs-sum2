import streamlit as st
import pandas as pd 
st.title("Explore Education Statistics API Data Checker")
st.header("Background")
st.markdown("This app is to be used for prelimniary checks on datasets to see if they meet the Explore Education Statistics (EES) API standards.")
st.header("Step 1 - Primary data checks")
st.markdown("Before starting this process, it is advisable to check that your datasets pass the primary EES data checks." \
"You can do this by visiting the [EES data screener](https://rsconnect/rsc/dfe-published-data-qa/). " \
"Please note, this screener is only available for internal use in the Department for Education.")
st.header("Upload your data")

ees_data_path = st.file_uploader("Upload EES data CSV", type="csv")
if ees_data_path is not None:
    ees_data = pd.read_csv(ees_data_path)
    # ...rest of your code...
else:
    st.warning("Please upload a CSV file.")

ees_meta_data_path =st.file_uploader('Upload the metadata to your CSV data file', type="csv")

if ees_meta_data_path is not None:
    ees_meta_data = pd.read_csv(ees_meta_data_path)
    st.markdown(ees_meta_data)
    # ...rest of your code...
else:
    st.warning("Please upload a CSV file.")
#read in data 



st.header("API Data Standards Reports")
st.header("Data summary")

st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)
st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')