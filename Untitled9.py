!pip install streamlit

!pip install scikit-learn

!pip install numpy
!pip install pandas

#Import the necessary libraries
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

#Load the iris dataset and assign the data and target variables
iris = load_iris()
X = iris.data
Y = iris.target

#Set up a Random Forest Classifier and fit the model
rf = RandomForestClassifier()
rf.fit(X, Y)

#Create a Streamlit app and add a title and header
st.title("Iris Flower Prediction App")
st.header("Enter the measurements of the iris flower:")

#Add input fields for sepal length, sepal width, petal length, and petal width
sepal_length = st.slider("Sepal length", float(X[:,0].min()), float(X[:,0].max()), float(X[:,0].mean()))
sepal_width = st.slider("Sepal width", float(X[:,1].min()), float(X[:,1].max()), float(X[:,1].mean()))
petal_length = st.slider("Petal length", float(X[:,2].min()), float(X[:,2].max()), float(X[:,2].mean()))
petal_width = st.slider("Petal width", float(X[:,3].min()), float(X[:,3].max()), float(X[:,3].mean()))

#Define a prediction button that takes in the input values and uses the classifier to predict the type of iris flower
if st.button("Predict"):
    prediction = rf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    species = iris.target_names[prediction[0]]
    st.write("The iris flower is a", species)
