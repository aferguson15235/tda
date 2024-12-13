import streamlit as st
import numpy as np
import tensorflow as tf
import pickle
import pandas as pd

# Load the saved neural network model
model = tf.keras.models.load_model('heart_disease.keras')  

# Load the saved svm model
##model = pickle.load(open('svm.pkl', 'rb')) 

# Load the saved scaler (StandardScaler)
scaler = pickle.load(open('scaler.pkl', 'rb'))  

# Function to make predictions
def make_prediction(input_data):
    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame([input_data], columns=[
        'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction',
        'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 
        'smoking', 'time'
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
st.image('heart.png', use_column_width=True)

st.write(""" 
Please fill in the information below, and we'll predict if you might be at risk for heart disease based on the data you provide.  
Note: All fields are important to give the most accurate prediction.
""")

# Collect input features from the user
age = st.number_input('Age', min_value=1, max_value=100, value=50, step=1, help="Enter your age in years.")

anaemia = st.selectbox(
    'Do you have Anaemia?',
    ['Yes', 'No'],
    help="Select 'Yes' if you have Anaemia, 'No' if you don't."
)

creatinine_phosphokinase = st.number_input(
    'Creatinine Phosphokinase Level (in U/L)',
    min_value=0, max_value=1000, value=100, step=1,
    help="Enter your Creatinine Phosphokinase level. This is a blood test result."
)

diabetes = st.selectbox(
    'Do you have Diabetes?',
    ['Yes', 'No'],
    help="Select 'Yes' if you have Diabetes, 'No' if you don't."
)

ejection_fraction = st.number_input(
    'Ejection Fraction (percentage)',
    min_value=0, max_value=100, value=50, step=1,
    help="Enter your Ejection Fraction (a percentage indicating how well your heart is pumping blood)."
)

high_blood_pressure = st.selectbox(
    'Do you have High Blood Pressure?',
    ['Yes', 'No'],
    help="Select 'Yes' if you have High Blood Pressure, 'No' if you don't."
)

platelets = st.number_input(
    'Platelet Count (in thousands per µL)',
    min_value=0, max_value=1000000, value=200000, step=1000,
    help="Enter your platelet count. This is a measure of how well your blood can clot."
)

serum_creatinine = st.number_input(
    'Serum Creatinine Level (in mg/dL)',
    min_value=0.0, max_value=10.0, value=1.0, step=0.1,
    help="Enter your Serum Creatinine level. This indicates kidney function."
)

serum_sodium = st.number_input(
    'Serum Sodium Level (in mEq/L)',
    min_value=100.0, max_value=200.0, value=140.0, step=0.1,
    help="Enter your Serum Sodium level. Sodium is essential for fluid balance in your body."
)

sex = st.selectbox(
    'Sex',
    ['Male', 'Female'],
    help="Select your gender: Male or Female."
)

smoking = st.selectbox(
    'Do you smoke?',
    ['Yes', 'No'],
    help="Select 'Yes' if you smoke, 'No' if you don't."
)

time = st.number_input(
    'Follow-up Time (in days)',
    min_value=1, max_value=1000, value=100, step=1,
    help="Enter the follow-up time in days since the initial visit."
)

# Convert inputs into appropriate format for prediction
input_data = [
    age,
    1 if anaemia == 'Yes' else 0,
    creatinine_phosphokinase,
    1 if diabetes == 'Yes' else 0,
    ejection_fraction,
    1 if high_blood_pressure == 'Yes' else 0,
    platelets,
    serum_creatinine,
    serum_sodium,
    1 if sex == 'Male' else 0,
    1 if smoking == 'Yes' else 0,
    time
]

# Button to trigger prediction
if st.button('Predict'):
    prediction = make_prediction(input_data)
   
    
    # Setting threshold for probability output
    # if the prediction is > 0.5, classify as risk
    if prediction[0] > 0.5:
        st.write("The model predicts: **Heart Disease Risk**")
        st.write("It's recommended to consult with a healthcare professional for further assessment.")
    else:
        st.write("The model predicts: **No Heart Disease Risk**")
        st.write("You seem to be at a lower risk based on the provided information.")