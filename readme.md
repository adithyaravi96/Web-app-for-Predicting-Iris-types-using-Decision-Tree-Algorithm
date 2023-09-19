# Iris Flower Species Prediction App

## Demo Video :
## Screenshot :


This web application uses a Decision Tree Classifier to predict the species of Iris flowers based on user-input sepal and petal measurements.


## Getting Started

### Prerequisites

Before running the app, ensure you have the required dependencies installed:

- Python 3.x
- Streamlit
- NumPy
- Joblib (for model loading)
- scikit learn library 

You can install the necessary packages using `pip`:

```bash
pip install streamlit numpy joblib

## Installation

# 1.Clone this repository to your local machine:
git clone https://github.com/your-username/iris-flower-prediction-app.git

# 2.Change to the project directory
cd iris-flower-prediction-app

#3.Run the Streamlit app
streamlit run iris_app.py

# The app should open in your default web browser

##Usage
1.Use the sidebar sliders to input sepal and petal measurements (in centimeters).

2.Click the "Predict" button to obtain the predicted Iris flower species.

3.The predicted species will be displayed in a text box with custom styling.

##Model
The app uses a Decision Tree Classifier model trained on the famous Iris dataset.

Model File: iris_classifier_model.joblib
Model Training Code: train_model.ipynb
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
GRIP Internship team
Iris Dataset
Streamlit Community and Documentation

