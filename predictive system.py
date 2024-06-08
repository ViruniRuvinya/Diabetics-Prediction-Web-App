# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the model
loaded_model=pickle.load(open('C:/Users/HP/Desktop/New folder/ML tutorials/diabetics_data/diabetic_prediction_trained_mode.sav','rb'))

input_data=(6,148,72,35,0,33.6,0.627,50)

#changing input data to numpy array
input_data_asarray=np.asarray(input_data)

#reshape data
reshaped_data=input_data_asarray.reshape(1,-1)

#standardize the reshaped data
#std_data=scaler.transform(reshaped_data)

prediction=loaded_model.predict(reshaped_data)
print(prediction)

if (prediction[0]==1):
  print('The person is diabetic')
else:
  print('The person is not diabetic')
