# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models


heart_disease_model = pickle.load(open('C:/Users/shawl/OneDrive/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))
diabetes_model = pickle.load(open('C:/Users/shawl/OneDrive/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav','rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('MediForcast',
                          
                          ['Home','Heart Disease Prediction','Diabetes Prediction','Pneumonia Prediction','Liver Disease Prediction','Breast Cancer Prediction'],
                          icons=['house-door-fill','heart-pulse-fill','droplet-fill','virus','clipboard2-pulse-fill','prescription2'],
                          default_index=0)
    
    #Home Page
if (selected == 'Home'):
    
        #page tittle 
    st.title('MediForcast : A disease prediction system')
    
    st.write("Welcome to MediForcast, your reliable health prediction system powered by machine learning. This platform is designed to help you predict the likelihood of suffering from various diseases based on your attributes. With the assistance of cutting-edge algorithms and a user-friendly interface, you can make informed decisions about your health and well-being.")

# Disease Prediction
    st.write("This system can predict multiple diseases, including heart disease and diabetes, using advanced machine learning techniques. You can input specific attribute values, such as age, blood pressure, cholesterol levels, and more, and our system will provide you with a prediction regarding your risk of developing the disease. This early insight can empower you to take preventive measures and consult with healthcare professionals.")

# How to Use
    st.write("Using this prediction system is easy:")
    st.write("- Select the disease you want to predict.")
    st.write("- Input your attribute values in the provided fields.")
    st.write("- Click the 'Test' button to receive your disease prediction.")
    st.write("- The system will show whether you have the disease or not.")

# Health Tips
    st.write("In addition to disease prediction, caring about your overall well-being, here are some general health tips :")
    st.write("- Maintain a balanced diet rich in fruits, vegetables, and whole grains.")
    st.write("- Engage in regular physical activity to keep your body and mind active.")
    st.write("- Get enough sleep to ensure proper rest and rejuvenation.")
    st.write("- Stay hydrated by drinking an adequate amount of water daily.")
    st.write("- Manage stress through relaxation techniques, hobbies, and spending time with loved ones.")
    st.write("- Regular health check-ups are essential for early detection and prevention.")

# Disclaimer
    st.write("Please note that these predictions are based on algorithms and available data. They are not a substitute for professional medical advice. Always consult a healthcare professional for accurate diagnosis and personalized recommendations.")

# Footer
    st.write("Thank you for choosing MediForcast to empower your health journey. Get started by exploring our prediction capabilities and gaining valuable health insights.")

   
    
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    #Pneumonia Prediction Page
if (selected == 'Pneumonia Prediction'):
    
        #page tittle 
    st.title('Needed to develop.')
    
    
#Pneumonia Prediction Page
if (selected == 'Liver Disease Prediction'):
    
        #page tittle 
    st.title('Needed to develop.')
    
#Pneumonia Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
        #page tittle 
    st.title('Needed to develop.')
