import streamlit as st
import pandas as pd
import numpy as np

from PyPDF2 import PdfReader
import io

st.title("Hello Guyzz !!")

#For the text box
name=st.text_input("Enter your name:")

#For the slider 
age=st.slider("Select your age:",0,100,25)
#min , max, start age

st.write(f"Your age is {age}")

#For selection box
options=['Python','Java','C++',"JavaScript"]
choices=st.selectbox("Choose your favourite language: ", options)
st.write(f"You selected {choices}.")

if name:
    st.write(f"Hello, {name}")


data={
    "Name":["John","Jane","Jack","Jill"],
    "Age":[28,24,35,40],
    "City":["New york","Los Angeles","Chicago","Houston"]
}

df=pd.DataFrame(data)
df.to_csv('Sample.csv')

st.write(df)

#TO upload file
upload_file = st.file_uploader("Choose a CSV or PDF file", type=['csv', 'pdf'])

if upload_file is not None:
    if upload_file.type == 'text/csv':
        df = pd.read_csv(upload_file)
        st.write(df)
    elif upload_file.type == 'application/pdf':
        pdf_reader = PdfReader(io.BytesIO(upload_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            print('/n')
        st.write(text)
    else:
        st.error("Unsupported file type")
    