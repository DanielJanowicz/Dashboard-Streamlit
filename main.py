# Importing packages
import pandas as pd
import streamlit as st

# Loading dataset
registry_df = pd.read_csv('https://github.com/DanielJanowicz/Data_Generator/blob/main/datasets/follow_up.csv')

# Creating a dashboard header
st.header('Patient Follow-Up')

# Creating a caption
st.caption('Patient follow-up recorded within the last year')

# Displaying the dataframe
if st.checkbox('Hospital 03 Follow-Up'):
    st.dataframe(registry_df)

# Creating a barchart
st.subheader('Display of Patients Primary Hospital')
hosp_num = registry_df['Hospital_Code'].value_counts()
st.bar_chart(hosp_num)
st.caption('Visual provides insight of the number of patients per hospital')

# Creating a line chart
st.subheader('Displaying the Date of Last Contact')
last_contact = registry_df['Last_Contact']
st.line_chart(last_contact)
st.caption('Visual provides insight of the date of last contact')

# Creating a code block
