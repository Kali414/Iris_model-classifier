import streamlit as st
import numpy as np
import pandas as pd


#Title of the application
st.title("Hello Streamlit")

#Display a simple text
st.write("This is a simple text..")

#Create a simple Dataframe

df=pd.DataFrame({
    'first column':[1,2,3,4,5],
    'second column':[2,4,6,8,10]
})

st.write('Here is the dataframe')
st.write(df)

#Create a line chart
st.write("Here is line chart.")
chart_data=pd.DataFrame(
    np.random.rand(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

