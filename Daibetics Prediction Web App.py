# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:46:03 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model=pickle.load(open('D:\ML\diabetics_data/diabetic_prediction_trained_mode.sav','rb'))

#creating a function
def diabetics_prediction(input_data):

    #changing input data to numpy array
    input_data_asarray=np.asarray(input_data)

    #reshape data
    reshaped_data=input_data_asarray.reshape(1,-1)

    #standardize the reshaped data
    #std_data=scaler.transform(reshaped_data)

    prediction=loaded_model.predict(reshaped_data)
    print(prediction)

    if (prediction[0]==1):
      return 'The person is diabetic'
    else:
      return 'The person is not diabetic'
    
def main():
    #giving a title
    st.title('Diabetics Prediction Web APP')
    
    #getting tje input data from the user
    Pregnancies =st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure level')
    SkinThickness=st.text_input('Skin Thickness value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DPF value')
    Age =st.text_input('Age')
    
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetics Test Result'):
        diagnosis=diabetics_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__== '__main__':
    main()
    
    
        
