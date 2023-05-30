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
