import requests

# API key for OpenWeatherMap
api_key = '75c302539fddd53d07ce2fcda119eddb'

# Base URL for the OpenWeatherMap API
base_url = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    # Construct the URL with the API key and city name
    url = f'{base_url}?q={city}&appid={api_key}'

    try:
        # Send the GET request to the API
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the weather data from the JSON response
            weather_data = response.json()
            return weather_data
        else:
            # Display an error message if the request was unsuccessful
            print(f'Error: {response.status_code} - {response.text}')
    except requests.exceptions.RequestException as e:
        # Display an error message if there was a network-related error
        print(f'Error: {e}')

# Example usage
city_name = 'London'
data = get_weather_data(city_name)
print(data)
def preprocess_weather_data(weather_data):
    # Check for missing values and handle them
    # For example, you can use pandas library to handle missing values
    # weather_data = weather_data.dropna()

    # Perform data transformation and feature engineering
    # For example, you can convert categorical variables to numerical using one-hot encoding
    # or extract additional features from existing data

    # Normalize numerical features
    # For example, you can use scikit-learn's MinMaxScaler or StandardScaler

    return preprocessed_data

# Example usage
preprocessed_data = preprocess_weather_data(data)
print(preprocessed_data)
import pandas as pd
import matplotlib.pyplot as plt

def explore_weather_data(weather_data):
    # Visualize temperature distribution
    plt.hist(weather_data['temperature'], bins=20)
    plt.xlabel('Temperature')
    plt.ylabel('Frequency')
    plt.title('Temperature Distribution')
    plt.show()

    # Calculate summary statistics
    summary_stats = weather_data.describe()
    print(summary_stats)

    # Analyze correlation between variables
    correlation_matrix = weather_data.corr()
    print(correlation_matrix)

# Example usage
explore_weather_data(preprocessed_data)
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the XGBoost model
model = xgb.XGBClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
import sqlite3

# Connect to the database
conn = sqlite3.connect('weather_data.db')

# Create a cursor
cursor = conn.cursor()

# Create the weather table
cursor.execute('''
    CREATE TABLE weather (
        city TEXT,
        date TEXT,
        temperature REAL,
        humidity INTEGER,
        wind_speed REAL
    )
''')

# Insert data into the table
for record in weather_data:
    cursor.execute('''
        INSERT INTO weather (city, date, temperature, humidity, wind_speed)
        VALUES (?, ?, ?, ?, ?)
    ''', (record['city'], record['date'], record['temperature'], record['humidity'], record['wind_speed']))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
import speech_recognition as sr
from chatterbot import ChatBot

# Initialize the chatbot
chatbot = ChatBot('WeatherBot')

# Set up the speech recognition system
recognizer = sr.Recognizer()

# Set up the microphone as the audio source
microphone = sr.Microphone()

# Loop to continuously listen for user input
while True:
    # Listen for user input through the microphone
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    # Convert speech to text using speech recognition
    try:
        text_input = recognizer.recognize_google(audio)
        print("User input:", text_input)
        
        # Generate chatbot response
        response = chatbot.get_response(text_input)
        print("Chatbot response:", response)
        
        # Convert chatbot response to speech using text-to-speech synthesis
        # Code for text-to-speech synthesis goes here
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
import streamlit as st
import speech_recognition as sr
from chatterbot import ChatBot

# Initialize the chatbot
chatbot = ChatBot('WeatherBot')

# Set up the speech recognition system
recognizer = sr.Recognizer()

# Set up the microphone as the audio source
microphone = sr.Microphone()

# Streamlit app layout
st.title('Weather Prediction App')
st.write('Enter your location or use speech recognition to ask for weather predictions.')

# User input
user_input = st.text_input('Location')

# Speech recognition
if st.button('Start Speech Recognition'):
    with microphone as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        text_input = recognizer.recognize_google(audio)
        user_input = text_input
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
    except sr.RequestError:
        st.write("Sorry, there was an error with the speech recognition service.")

# Generate weather prediction
prediction = generate_weather_prediction(user_input)

# Display weather prediction
st.subheader('Weather Prediction')
st.write(prediction)

# Generate chatbot response
response = chatbot.get_response(user_input)

# Display chatbot response
st.subheader('Chatbot Response')
st.write(response)
