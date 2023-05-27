import streamlit as st
import speech_recognition as sr

def transcribe_speech(api, language):
    r = sr.Recognizer()
    
    if api == "Google Speech Recognition":
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 4000
        recognizer.pause_threshold = 0.6

        with sr.Microphone() as source:
            st.info("Speak now...")
            audio = recognizer.listen(source)
            st.info("Transcribing...")

        try:
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand you."
        except sr.RequestError:
            return "Sorry, there was an issue with the speech recognition service."

    elif api == "CMU Sphinx":
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 4000
        recognizer.pause_threshold = 0.6

        with sr.Microphone() as source:
            st.info("Speak now...")
            audio = recognizer.listen(source)
            st.info("Transcribing...")

        try:
            text = recognizer.recognize_sphinx(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand you."
        except sr.RequestError:
            return "Sorry, there was an issue with the speech recognition service."

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")
    
    available_apis = ["Google Speech Recognition", "CMU Sphinx"]
    api = st.selectbox("Select Speech Recognition API", available_apis)
    
    available_languages = ["en-US", "es-ES"]  # Add more languages as needed
    language = st.selectbox("Select Language", available_languages)
    
    if st.button("Start Recording"):
        text = transcribe_speech(api, language)
        st.write("Transcription:", text)

if __name__ == "__main__":
    main()
