import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier 


@st.cache_data   #which loads the data into cache and when we againn run this over time
#it should not again load the dataset fully
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data,columns = iris.feature_names)
    df['species'] = iris.target
    return df,iris.target_names


df,target_names = load_data()

model = RandomForestClassifier()  
model.fit(df.iloc[:,:-1],df['species'])  #fit takes and independent event and dependent event


#the streamlit app should look like user has t0 see the 
#sidebar of what lengths of sepal length ,width and petal width,lenght
#would give the flower sample 
st.sidebar.title("Input features")
#keeping the lenght from min to max
sepal_length = st.sidebar.slider("sepal length", float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("sepal length", float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("sepal length", float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("sepal length", float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))


input_data = [[sepal_length,sepal_width,petal_length,petal_width]]


#prediction
prediction = model.predict(input_data)
prediction_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"the predicted species is: {prediction_species}")