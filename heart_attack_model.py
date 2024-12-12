import streamlit as st
import numpy as np
import tensorflow as tf
import pickle
import pandas as pd

# Load the saved decision tree model
model = pickle.load(open('decision_tree.pkl', 'rb')) 

# Load the saved scaler (StandardScaler)
scaler = pickle.load(open('sc.pkl', 'rb'))  

# Function to make predictions
def make_prediction(input_data):
    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame([input_data], columns=[
        'Age', 'Gender', 'Heart rate', 'Systolic blood pressure',
       'Diastolic blood pressure', 'Blood sugar', 'CK-MB', 'Troponin'
    ])
    
    # Output the user's input 
    st.write("### User Input:")

     # Display the input as a DataFrame
    st.dataframe(input_df) 
    
    # Apply the scaling transformation using the loaded scaler
    scaled_data = scaler.transform(input_df)  
    
    # Make the prediction using saved the neural network model
    prediction = model.predict(scaled_data)
    
    return prediction

# Streamlit UI
st.title('Heart Disease Prediction')

# Display an image
st.image('heart.png', use_container_width=True)

st.write(""" 
Please fill in the information below, and we'll predict if you might be at risk for a heart attack based on the data you provide.  
Note: All fields are important to give the most accurate prediction.
""")

# Collect input features from the user
age = st.number_input('Age', min_value=1, max_value=100, value=50, step=1, help="Enter your age in years.")

gender = st.selectbox(
    'Sex',
    ['Male', 'Female'],
    help="Select your gender: Male or Female."
)

heart_rate = st.number_input('Heart rate', min_value=1, max_value=1500, value=50, step=1, help="Enter your heart rate.")

systolic_blood_pressure = st.number_input('Systolic blood pressure', min_value=1, max_value=300, value=125, step=1, help="Enter your systolic blood pressure.")

diastolic_blood_pressure = st.number_input('Diastolic blood pressure', min_value=1, max_value=200, value=75, step=1, help="Enter your diastolic blood pressure.")

blood_sugar = st.number_input('Blood sugar', min_value=1, max_value=1000, value=100, step=1, help="Enter your blood sugar.")

ck_mb = st.number_input('Creatine kinase-MB', min_value=1, max_value=300, value=5, step=1, help="Enter your creatine kinase-MB.")

troponin = st.number_input('Troponin', min_value=0.0, max_value=10.0, value=0.5, step=0.01, help="Enter your troponin.")

# Convert inputs into appropriate format for prediction
input_data = [
    age,
    1 if gender == 'Male' else 0,
    heart_rate,
    systolic_blood_pressure,
    diastolic_blood_pressure,
    blood_sugar,
    ck_mb,
    troponin
]

# Button to trigger prediction
if st.button('Predict'):
    prediction = make_prediction(input_data)
   
    # Setting threshold for probability output
    # if the prediction is > 0.5, classify as risk
    if prediction[0] > 0.5:
        st.write("The model predicts: **Heart Attack Risk**")
        st.write("It's recommended to consult with a healthcare professional for further assessment.")
    else:
        st.write("The model predicts: **Low Heart Attack Risk**")
        st.write("You seem to be at a lower risk based on the provided information.")