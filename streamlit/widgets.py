import streamlit as st
import pandas as pd

st.title("streamlit text input")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello {name}")

#to use a slidder
age = st.slider("select your age:",0,100,25)

st.write(f"your age is {age}")

#we can also create  select boxes

options = ['python','java','c++','javascript']
choice = st.selectbox("choose your favorite language:",options)
st.write(f"you selected {choice}.")


data = {
    'Name':['john','jane','jake','jill'],
    'Age':[28,24,35,40],
    'city':['New york','los Angeles','chicago','houston']

}

df = pd.DataFrame(data)
df.to_csv('sample.csv')
st.write(df)

#uploading files
uploaded_file = st.file_uploader("choose a CSV file",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

