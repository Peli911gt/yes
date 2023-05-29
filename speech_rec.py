import streamlit as st
import speech_recognition as sr

def transcribe_speech(audio_file, api, language):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Read the entire audio file
            
        # Select the speech recognition API based on user input
        if api == 'Google':
            transcribed_text = recognizer.recognize_google(audio, language=language)
        elif api == 'Wit.ai':
            wit_ai_api_key = 'YOUR_WIT_AI_API_KEY'  # Replace with your Wit.ai API key
            transcribed_text = recognizer.recognize_wit(audio, key=wit_ai_api_key)
        elif api == 'IBM Watson':
            ibm_username = 'YOUR_IBM_USERNAME'  # Replace with your IBM Watson username
            ibm_password = 'YOUR_IBM_PASSWORD'  # Replace with your IBM Watson password
            transcribed_text = recognizer.recognize_ibm(audio, username=ibm_username, password=ibm_password, language=language)
        else:
            raise ValueError('Invalid speech recognition API selected')
        
        return transcribed_text
    except sr.UnknownValueError:
        raise ValueError('Speech recognition could not understand audio')
    except sr.RequestError:
        raise ValueError('Could not connect to the speech recognition service')

def main():
    st.title('Speech to Text Transcription')

    # File upload
    st.subheader('Upload an audio file:')
    audio_file = st.file_uploader('Choose an audio file', type=['wav', 'Native FLAC','AIFF/AIFF-C'])

    if audio_file:
        # Speech recognition API selection
        st.subheader('Speech Recognition API:')
        api_options = ['Google', 'Wit.ai', 'IBM Watson']
        api = st.selectbox('Select an API', api_options)

        # Language selection
        st.subheader('Language:')
        language = st.text_input('Enter the language code (e.g., en-US)')

        # Transcribe speech
        if st.button('Transcribe'):
            try:
                transcribed_text = transcribe_speech(audio_file, api, language)
                st.success('Transcription Successful:')
                st.text_area('Transcribed Text', value=transcribed_text, height=200)

                # Save to file
                if st.button('Save Transcription'):
                    save_text_to_file(transcribed_text)
                    st.success('Transcribed text saved to file')
            except ValueError as e:
                st.error(str(e))

if __name__ == '__main__':
    main()
