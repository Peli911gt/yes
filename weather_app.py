import requests
import json
import pandas as pd
import sqlite3
import speech_recognition as sr
import streamlit as st
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

conn = sqlite3.connect('weather_data.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS weather (Temperature REAL, Humidity REAL, WindSpeed REAL, WeatherDescription TEXT)''')

conn.commit()
conn.close()

# Retrieve weather data from OpenWeatherMap API
def get_weather_data(city):
    api_key = "4208acea354396147c3d0f2359ff47a9"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

# Preprocess weather data
def preprocess_data(data):
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather_description = data['weather'][0]['description']
    df = pd.DataFrame({'Temperature': [temperature], 'Humidity': [humidity], 'WindSpeed': [wind_speed], 'WeatherDescription': [weather_description]})
    return df

# Train XGBoost model
def train_model(X, y_encoded):
    model = xgb.XGBClassifier()
    model.fit(X, y_encoded)
    return model

# Store weather data in SQLite database
def store_data(df):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    for index, row in df.iterrows():
        temperature = row['Temperature']
        humidity = row['Humidity']
        wind_speed = row['WindSpeed']
        weather_description = row['WeatherDescription']
        c.execute("INSERT INTO weather VALUES (?, ?, ?, ?)", (temperature, humidity, wind_speed, weather_description))
    conn.commit()
    conn.close()

# Speech recognition
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening for cosmic whispers...")
        audio = r.listen(source)
        st.write("Processing the cosmic symphony...")
        try:
            text = r.recognize_google(audio)
            st.write("You whispered:", text)
            return text
        except sr.UnknownValueError:
            st.write("Apologies, I couldn't decipher the interstellar riddles.")
        except sr.RequestError:
            st.write("Uh-oh, cosmic interference is blocking my translation circuits.")

# Preprocess target variable
def preprocess_target(y):
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    return y_encoded, label_encoder

# Main function
def main():
    st.title("Cosmic Weather Oracle")
    st.write("Enter the name of the city you seek to predict:")
    city = st.text_input("City")
    
    if st.button("Invoke Celestial Insights"):
        data = get_weather_data(city)
        if 'message' in data:
            st.write("City not found in the cosmic map. Please enter a valid city name.")
        else:
            df = preprocess_data(data)
            X = df.drop(columns=['WeatherDescription'])  # Features (excluding Weather Description)
            y = df['WeatherDescription']  # Target variable (Weather Description)
            
            y_encoded, label_encoder = preprocess_target(y)
            
            model = train_model(X, y_encoded)
            prediction_labels = label_encoder.inverse_transform(model.predict(X))
            st.write("Cosmic Prediction:", prediction_labels)
            store_data(df)
    
    if st.button("Astro-Speech Recognition"):
        text = speech_to_text()
        if text:
            st.write("The stars whisper:", text)

if __name__ == '__main__':
    main()
