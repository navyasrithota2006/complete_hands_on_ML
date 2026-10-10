import streamlit as st
import numpy as np
import pandas as pd

#title of the application
st.title("Hello Streamlit")

#display a simple text
st.write("This is a simple text")

#create simple data frame
df = pd.DataFrame({
    'first_column':[1,2,3,4],
    'second_column':[10,20,30,40]
})

#display the dataframe
st.write("here is the dataframe")
st.write(df)

#create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns = ['a','b','c']
)
st.line_chart(chart_data)