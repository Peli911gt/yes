import streamlit as st
import sounddevice as sd
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

    # Transcribe speech
    text = transcribe_speech(api, language)

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

def transcribe_speech(api, language):
    fs = 44100  # Sample rate
    duration = 5  # Recording duration in seconds

    with sd.rec(int(duration * fs), samplerate=fs, channels=1, blocking=True):
        st.text("Listening...")

        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

    st.text("Transcribing...")
    text = recognizer.transcribe(audio[:, 0], fs, api, language)

    return text

def save_transcribed_text(text, filename):
    with open(filename, "w") as file:
        file.write(text)

if __name__ == "__main__":
    main()
