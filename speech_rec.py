import streamlit as st
import speech_recognition as sr

def transcribe_speech(api, language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        if st.button("Pause Recording"):
            source.pause()
            st.info("Recording paused.")
            st.button("Resume Recording")
            source.resume()
            st.info("Recording resumed...")
        audio_text = r.listen(source)
        st.info("Transcribing...")
        try:
            if api == "Google Speech Recognition":
                text = r.recognize_google(audio_text, language=language)
            elif api == "Sphinx":
                text = r.recognize_sphinx(audio_text, language=language)
            # Add more speech recognition APIs here
            
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand your speech."
        except sr.RequestError as e:
            return f"Error: {str(e)}"

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")
    
    api_options = ["Google Speech Recognition", "Sphinx"]
    api = st.selectbox("Select Speech Recognition API", api_options)
    
    language_options = ["en-US", "en-GB", "es-ES"] # Add more language options
    language = st.selectbox("Select Language", language_options)
    
    if st.button("Start Recording"):
        text = transcribe_speech(api, language)
        st.write("Transcription:", text)
        
        if st.button("Save Transcription"):
            with open("transcription.txt", "w") as file:
                file.write(text)
            st.success("Transcription saved to transcription.txt")
    
if __name__ == "__main__":
    main()
