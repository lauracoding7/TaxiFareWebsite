import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

'''
# WELCOME TO TAXI FARE 🚕
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

date = st.date_input(
    "Please specify the date.")

time = st.time_input(
    "Please specify the time.")

pickup_longitude = st.text_input('Please specify the pickup longitude.', "-73.8803331")


pickup_latitude= st.text_input('Please specify the pickup latitude.', "40.7614327")

dropoff_longitude = st.text_input('Please specify the dropoff longitude.', "-73.9798156")

dropoff_latitude= st.text_input('Please specify the dropoff latitude.', "-73.9798156")

count = st.number_input('Please specify the number of passengers.', min_value=1, max_value=10, step=1, value=1)


# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''


# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

#2. Let's build a dictionary containing the parameters for our API...


# https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2   

url = 'https://taxifare.lewagon.ai/predict'

combined = datetime.datetime.combine(date, time)

params = {
    "pickup_datetime": combined,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": count
    }

#3. Let's call our API using the `requests` package...

response = requests.get(url, params=params)
#response.json()

def get_map_data():

    return pd.DataFrame(
        {
        'lat' : [float(pickup_latitude), float(dropoff_latitude)],
        'lon' : [float(pickup_longitude), float(dropoff_longitude)]
        }
    )

df = get_map_data()

st.map(df)

if st.button('prediction'):
    st.write(response.json()["fare"])
    


#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
#'''