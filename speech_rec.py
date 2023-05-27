import streamlit as st
import speech_recognition as sr


def transcribe_speech(api, language, recognizer, audio_text):
    try:
        if api == "Google Cloud Speech-to-Text":
            text = recognizer.recognize_google_cloud(audio_text)
        elif api == "Wit.ai":
            text = recognizer.recognize_wit(audio_text, key=WIT_API_KEY)
        elif api == "IBM Watson":
            text = recognizer.recognize_ibm(audio_text, username=IBM_USERNAME, password=IBM_PASSWORD)
        elif api == "Microsoft Azure Speech Service":
            text = recognizer.recognize_azure(audio_text, key=AZURE_API_KEY)
        elif api == "Mozilla DeepSpeech":
            text = recognizer.recognize_deepspeech(audio_text)
        else:
            text = "Invalid API selection"
    except sr.UnknownValueError:
        text = "Unable to recognize speech"
    except sr.RequestError as e:
        text = f"Error occurred during transcription: {str(e)}"
    
    return text


def save_text(text):
    with open("transcription.txt", "w") as file:
        file.write(text)
    st.write("Transcription saved to file.")


def main():
    st.title("Speech Recognition App")
    st.write("Select Speech Recognition API:")
    api = st.selectbox("API", ["Google Cloud Speech-to-Text", "Wit.ai", "IBM Watson", "Microsoft Azure Speech Service", "Mozilla DeepSpeech"])
    
    language = st.text_input("Language", "")

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    if st.button("Start Recording"):
        with microphone as source:
            audio_text = recognizer.listen(source)

        text = transcribe_speech(api, language, recognizer, audio_text)
        st.write("Transcription:", text)

        if st.button("Save Transcription"):
            save_text(text)

        if st.button("Pause"):
            recognizer.pause_threshold = 999999999

        if st.button("Resume"):
            recognizer.pause_threshold = 0.8


if __name__ == "__main__":
    main()
