import streamlit as st
import pickle
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

loaded_model = pickle.load(open('finalized_mode.pkl','rb'))
results = loaded_model.score(years,salary)
print(results)

def predict_salary(years,salary):
    input=np.array([[years]]).astype(np.int)
    prediction=finalized_mode.predict(input)
    pred='90:.{1}f'.format(prediction[0][0],2)
    print(type(pred))
    return float(pred)
