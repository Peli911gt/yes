import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

def main():
    st.title("Speech Recognition App")

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Get available APIs
    api_options = ["Google", "Wit.ai", "IBM Watson"]

    # User input for API selection
    api = st.selectbox("Select Speech Recognition API", api_options)

    # User input for language selection
    language = st.text_input("Enter the language you are speaking in")

    # Upload audio file
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

    if audio_file is not None:
        # Load audio file
        audio = AudioSegment.from_file(audio_file)

        # Convert audio to mono if it has multiple channels
        if audio.channels > 1:
            audio = audio.set_channels(1)

        # Save audio to a temporary file
        temp_file = "temp.wav"
        audio.export(temp_file, format="wav")

        # Transcribe speech
        text = transcribe_audio(temp_file, api, language)

        # Display the transcribed text
        st.text("Transcribed Text:")
        st.text(text)

        # Save transcribed text to a file
        save_to_file = st.button("Save to File")
        if save_to_file:
            filename = st.text_input("Enter the filename")
            if filename:
                save_transcribed_text(text, filename)
                st.success(f"Transcribed text saved to {filename}")

        # Delete the temporary audio file
        os.remove(temp_file)

def transcribe_audio(audio_file, api, language):
    # Open the audio file
    with sr.AudioFile(audio_file) as source:
        # Load audio data
        audio_data = recognizer.record(source)

        # Choose the appropriate API
        if api == "Google":
            text = recognizer.recognize_google(audio_data, language=language)
        elif api == "Wit.ai":
            wit_ai_api_key = "YOUR_WIT_AI_API_KEY"  # Replace with your Wit.ai API key
            text = recognizer.recognize_wit(audio_data, key=wit_ai_api_key)
        elif api == "IBM Watson":
            ibm_watson_api_key = "YOUR_IBM_WATSON_API_KEY"  # Replace with your IBM Watson API key
            ibm_watson_url = "YOUR_IBM_WATSON_URL"  # Replace with your IBM Watson API URL
            text = recognizer.recognize_ibm(audio_data, username=ibm_watson_api_key, password=ibm_watson_url)
        else:
            text = ""

    return text

def save_transcribed_text(text, filename):
    with open(filename, "w") as file:
        file.write(text)

if __name__ == "__main__":
    main()
