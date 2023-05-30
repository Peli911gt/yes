import streamlit as st
import speech_recognition as sr

def chatbot(input_text):
    # Simple chatbot logic for demonstration
    if input_text.lower() == "hello":
        response = "Hi there!"
    else:
        response = "I'm sorry, I didn't understand that."

    return response

def transcribe_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand audio."
    except sr.RequestError:
        return "Sorry, there was an issue with the speech recognition service."

def main():
    st.title("Speech-Enabled Chatbot")

    # Get user input (speech or text)
    option = st.radio("Input Type", ("Text", "Speech"))

    if option == "Text":
        text_input = st.text_input("Enter your message", "")
    elif option == "Speech":
        text_input = transcribe_speech()

    # Process user input and generate response
    if text_input:
        response = chatbot(text_input)
        st.write("Chatbot:", response)

# Run the app
if __name__ == "__main__":
    main()
