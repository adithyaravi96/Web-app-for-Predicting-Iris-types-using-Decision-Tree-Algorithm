
import streamlit as st
import numpy as np
import joblib
# Load the saved model
clf = joblib.load('E://hand digit recog//Prediction using decision tree\iris_classifier_model.joblib')

st.title('Iris Flower Species Prediction')
st.write('This web app uses a Decision Tree Classifier to predict the species of Iris flowers.')

# Sidebar for user input
st.sidebar.header('Input Features')

# Create input fields for sepal and petal measurements
sepal_length = st.sidebar.slider('Sepal Length (cm)', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sepal_width = st.sidebar.slider('Sepal Width (cm)', min_value=0.0, max_value=10.0, value=3.5, step=0.1)
petal_length = st.sidebar.slider('Petal Length (cm)', min_value=0.0, max_value=10.0, value=1.5, step=0.1)
petal_width = st.sidebar.slider('Petal Width (cm)', min_value=0.0, max_value=10.0, value=0.2, step=0.1)

# Create a feature vector from user input
user_input = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, -1)

# Make predictions
prediction = clf.predict(user_input)
predicted_class = prediction[0]

# Define class labels
class_labels = ['setosa', 'versicolor', 'virginica']

# Display the predicted class

st.subheader('Predicted Iris Species:')
st.markdown(f'<div style="font-size: 24px; color: yellow;">{predicted_class}</div>', unsafe_allow_html=True)

