import nltk
import streamlit as st
import speech_recognition as sr
import sounddevice as sd
import numpy as np

def transcribe_speech():
    r = sr.Recognizer()
    fs = 44100
    duration = 5  # Adjust the duration as needed

    with sd.rec(int(duration * fs), samplerate=fs, channels=1):
        st.write("Speak something...")
        sd.wait()

    try:
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        audio = np.squeeze(audio)
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
        return ""
    except sr.RequestError:
        st.write("Sorry, there was an issue with the speech recognition service.")
        return ""

def chatbot(input_text):
    # Your chatbot algorithm implementation
    # Use the input_text to generate a response
    response = "Your chatbot response"
    return response

def main():
    st.title("Speech-enabled Chatbot")

    input_type = st.radio("Input Type", ("Text", "Speech"))

    if input_type == "Text":
        text_input = st.text_input("User Input", "")
        if st.button("Send"):
            response = chatbot(text_input)
            st.write("Response:", response)
    else:
        if st.button("Start Recording"):
            text_input = transcribe_speech()
            if text_input:
                response = chatbot(text_input)
                st.write("Response:", response)

if __name__ == "__main__":
    main()
