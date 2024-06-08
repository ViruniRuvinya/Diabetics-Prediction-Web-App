# Diabetics-Prediction-Web-App

## Overview
The diabetes prediction web application uses machine learning to predict the likelihood of diabetes based on user input health metrics. Streamlit is employed to create an interactive and user-friendly web interface, allowing for seamless input and real-time prediction display.

## Model Architecture

### 1.Data Collection
The model is trained on a dataset with various health attributes relevant to diabetes prediction, such as:

-*Pregnancies*

-*Glucose levels*

-*Blood pressure*

-*Skin thickness*

-*Insulin levels*

-*Body Mass Index (BMI)*

-*Diabetes pedigree function*

-*Age*

### 2.Data Preprocessing

Essential preprocessing steps include:

-Handling missing or inconsistent data

-Normalizing or scaling features for consistency

-Explanatory data analysis

-Splitting the dataset into training and testing sets

### 3.Model Selection

Various machine learning algorithms can be used, including:

-Logistic Regression

-Decision Trees

-Random Forest

-Support Vector Machines (SVM)


### 4.Model Training

The model is trained using the training dataset by

-Feeding input features to the model

-Optimizing model parameters to improve prediction accuracy

-Validating the model

### 5.Model Evaluation:

The trained model is evaluated using the test dataset, focusing on  the metric *accuracy_score*

### 6.Deployment with Streamlit

The trained model is integrated into a Streamlit web application, providing:

-A simple and interactive user interface for data input

-Real-time processing and prediction display

-Visualization of model results and insights

## User Interaction

Input: Users enter their health metrics through interactive widgets in the Streamlit interface.

Prediction: Upon submitting the inputs, Streamlit passes the data to the backend model, which processes it and generates a prediction.

Output: The prediction is displayed in the Streamlit app, indicating the likelihood of having diabetes.

## Technologies Used

Frontend: Streamlit for creating interactive web interfaces.

Backend: Python for handling model logic and processing.

Machine Learning: Libraries like Scikit-learn, numpy,Pandas,matplot and Scipy for developing and training the model.

Data Visualization: Streamlit components for visualizing data and prediction results.

