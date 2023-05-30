import streamlit as st
import speech_recognition as sr
from google.cloud import speech_v1p1beta1 as speech

# Function to transcribe speech using Google Cloud Speech-to-Text API
def transcribe_speech():
    # Configure speech recognition client
    client = speech.SpeechClient()

    # Start recording audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Say something!")
        audio = r.listen(source)

    # Transcribe the recorded audio using Google Cloud Speech-to-Text API
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    audio_data = speech.RecognitionAudio(content=audio.get_raw_data())
    response = client.recognize(config=config, audio=audio_data)

    # Extract the transcribed text from the response
    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript

    return text

# Main function
def main():
    st.title("Speech-Enabled Chatbot")

    # Get user input (text or speech)
    input_type = st.radio("Input Type", ("Text", "Speech"))
    if input_type == "Text":
        text_input = st.text_input("Enter your message")
    else:
        text_input = transcribe_speech()

    # Call chatbot algorithm to generate response
    response = chatbot(text_input)

    # Display the chatbot response
    st.write("Chatbot:", response)

# Run the app
if __name__ == "__main__":
    main()
