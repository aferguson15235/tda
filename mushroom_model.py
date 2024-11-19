import streamlit as st
import numpy as np
import tensorflow as tf
import pickle
import pandas as pd

# Load the saved logistic regression model
model = pickle.load(open('log.pkl', 'rb')) 

# Load the existing data set
data = pd.read_csv('mushrooms.csv')

# Function to make predictions
def make_prediction(input_data):
    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame([input_data], columns=['class','cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'])
    
    # Add new data to existing database for one-hot encoding
    data.loc['new_data'] = input_data

    # One hot encoding of data
    one_hot_df = pd.get_dummies(data, columns=data.columns[1:], dtype=int)

    # Format encoded user input data as data frame
    input_df_encoded = pd.DataFrame([one_hot_df.iloc[-1,1:]], columns=one_hot_df.columns[1:])

    # Make the prediction using saved the neural network model
    prediction = model.predict(input_df_encoded)
    
    return prediction


# Streamlit UI
st.title('Poisonous Mushroom Predictor')

# Display an image
st.image('mushroom.jpg', use_container_width=True)

st.write(""" 
Please fill in the information below, and we'll predict if a mushroom is edible based on the data you provide.  
Note: All fields are important to give the most accurate prediction.
""")

# Collect input features from the user
cap_shape = st.selectbox(
    'What is the cap-shape?',
    ['b', 'c', 'x', 'f', 'k', 's'],
    help="bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s"
)

cap_surface = st.selectbox(
    'What is the cap-surface?',
    ['f','g','y','s'],
    help="fibrous=f,grooves=g,scaly=y,smooth=s"
)

cap_color = st.selectbox(
    'What is the cap-color?',
    ['n','b','c','g','r','p','u','e','w','y'],
    help="brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y"
)

bruises = st.selectbox(
    'Does it have bruises?',
    ['t','f'],
    help="bruises=t,no=f"
)

odor = st.selectbox(
    'What is the odor?',
    ['a','l','c','y','f','m','n','p','s'],
    help = 'almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s'
)

gill_attachment = st.selectbox(
    'What is the gill-attachment?',
    ['a','d','f','n'],
    help = 'attached=a,descending=d,free=f,notched=n'
)

gill_spacing = st.selectbox(
    'What is the gill-spacing?',
    ['c','w','d'],
    help = 'close=c,crowded=w,distant=d'
)

gill_size = st.selectbox(
    'What is the gill-size?',
    ['b','n'],
    help = 'broad=b,narrow=n'
)

gill_color = st.selectbox(
    'What is the gill-color?',
    ['k','n','b','h','g','r','o','p','u','e','w','y'],
    help = 'black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y'
)

stalk_shape = st.selectbox(
    'What is the stalk-shape?',
    ['e','t'],
    help = 'enlarging=e,tapering=t'
)

stalk_root = st.selectbox(
    'What is the stalk-root?',
    ['b','c','u','e','z','r','?'],
    help = 'bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?'
)

stalk_surface_above_ring = st.selectbox(
    'What is the stalk-surface-above-ring?',
    ['f','y','k','s'],
    help = 'fibrous=f,scaly=y,silky=k,smooth=s'
)

stalk_surface_below_ring = st.selectbox(
    'What is the stalk-surface-below-ring?',
    ['f','y','k','s'],
    help = 'fibrous=f,scaly=y,silky=k,smooth=s'
)

stalk_color_above_ring = st.selectbox(
    'What is the stalk-surface-above-ring?',
    ['n','b','c','g','o','p','e','w','y'],
    help = 'brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y'
)

stalk_color_below_ring = st.selectbox(
    'What is the stalk-surface-below-ring?',
    ['n','b','c','g','o','p','e','w','y'],
    help = 'brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y'
)

veil_type = st.selectbox(
    'What is the veil-type?',
    ['p'],
    help = 'partial=p'
)

veil_color = st.selectbox(
    'What is the veil-color?',
    ['n','o','w','y'],
    help = 'brown=n,orange=o,white=w,yellow=y'
)

ring_number = st.selectbox(
    'What is the ring-number?',
    ['n','o','t'],
    help = 'none=n,one=o,two=t'
)

ring_type = st.selectbox(
    'What is the ring-type?',
    ['e','f','l','n','p'],
    help = 'evanescent=e,flaring=f,large=l,none=n,pendant=p'
)

spore_print_color = st.selectbox(
    'What is the spore-print-color?',
    ['k','n','b','h','r','o','u','w','y'],
    help = 'black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y'
)

population = st.selectbox(
    'What is the population?',
    ['a','c','n','s','v','y'],
    help = 'abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y'
)

habitat = st.selectbox(
    'What is the habitat?',
    ['g','l','m','p','u','w','d'],
    help = 'grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d'
)

input_data = [1,
              cap_shape,
              cap_surface,
              cap_color,
              bruises,
              odor,
              gill_attachment,
              gill_spacing,
              gill_size,
              gill_color,
              stalk_shape,
              stalk_root,
              stalk_surface_above_ring,
              stalk_surface_below_ring,
              stalk_color_above_ring,
              stalk_color_below_ring,
              veil_type,
              veil_color,
              ring_number,
              ring_type,
              spore_print_color,
              population,
              habitat]


# Button to trigger prediction
if st.button('Predict'):
    prediction = make_prediction(input_data)
   
    
    # Setting threshold for probability output
    # if the prediction is > 0.5, classify as poisonous
    if prediction[0] > 0.5:
        st.write("The model predicts: **Poisonous**")
        st.write("It's not recommended to eat this mushroom.")
    else:
        st.write("The model predicts: **Edible**")
        st.write("The mushroom seems to be edible.")
