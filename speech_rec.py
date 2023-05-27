import streamlit as st
from pydub import AudioSegment
import pyspeech

def main():
    st.title("Speech Recognition App")

    # Initialize the speech recognizer
    recognizer = pyspeech.SpeechRecognizer()

    # Get available APIs
    api_options = recognizer.get_available_apis()

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

        # Transcribe speech
        text = recognizer.transcribe(audio.get_array_of_samples(), audio.frame_rate, api, language)

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

def save_transcribed_text(text, filename):
    with open(filename, "w") as file:
        file.write(text)

if __name__ == "__main__":
    main()
