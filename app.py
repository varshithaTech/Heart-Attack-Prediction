# importing necessary packages 
import numpy as np 
from pandas import options 
import streamlit as st
import pandas as pd
import pickle 
from sklearn.preprocessing import StandardScaler # to fit the model and predict

# load the file 
# \\ is used to avoid unicode errors 
with open('heartattack (1).pkl','rb') as file:
    model = pickle.load(file)
  
# taking a variable and transforming the dta and storing it in the x_test
def predict(data):
    scale = StandardScaler()
    x_test = scale.fit_transform(data)
    
    # predicting the test data
    prediction = model.predict(x_test)
    return prediction
# this function has header and dataset 
# two containers are used for header
def main():
     header = st.container() # acts like head tag 
     dataset = st.container()  # acts like body tag 
     
     with header:
          st.title('Heart Disease Prediction')
          st.text('Predict the person if a person has heart disease or not ')
          
     with dataset:
          st.header("Data Input")
          st.text("Provides following information")
          age = st.number_input('Age',min_value=0,step=1) # give the dataset input 
          sex=st.selectbox('Sex',['Female','Male'])
          cp = st.selectbox("Chest Pain Type", ["Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptotic"])
          # resting blood pressure rate 
          trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, step=1)
          chol = st.number_input("Cholesterol (mg/dl)", min_value=0, step=1)
          fps = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
          restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
          thalachh = st.number_input("Maximum Heart Rate Achieved", min_value=0, step=1)
          exng = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
          caa = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, step=1)
          # Map categorical variables to numerical values
          sex = 1 if sex =='Male' else 0
          cp_mapping = {'Typical Angina':0,'Atypical Angina':1,'Non-Anginal Pain':2,'Asymptotic':3}
          cp = cp_mapping[cp]
          
          fps = 1 if fps == 'True' else 0
          restecg_mapping = {'Normal':0,'ST-T wave abnormality':1,'Left ventricular hypertrophy':2}
          restecg = restecg_mapping[restecg]
          exng = 1 if exng == 'Yes' else 0
          # Create input data dictionary
          input_data =  {
              'age': age,
              'sex': sex,
              'cp': cp,
              'trestbps': trestbps,
              'chol': chol,
              'fps': fps,
              'restecg': restecg,
              'thalachh': thalachh,
              'exng': exng,
              'caa': caa
          }
          # calling all the datas 
          #convert input data to dataframe
          df = pd.DataFrame(data=[input_data])
          # predict button
          if st.button('predict'):
              prediction = predict(df)
              # if the value comes to 0 the person has a heart disease 
              if prediction [0] == 1:
                  st.success('You have a heart disease Please consult the Doctor')
              else:
                  st.success('You Didnt Have A Heart Disease')

if __name__ == '__main__':
    main()
                  