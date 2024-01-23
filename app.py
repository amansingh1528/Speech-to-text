import streamlit as st
import speech_recognition as sr

def main():
    st.title("Real-time Speech-to-Text Conversion")

    # Create a SpeechRecognition recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    microphone = sr.Microphone()

    # Flag to control the loop
    is_listening = False

    # Start the Streamlit app
    st.write("Speak into the microphone:")

    # Button to start the process
    start_button = st.button("Start Conversion")

    # Button to stop the process
    stop_button = st.button("Stop Conversion")

    if start_button:
        is_listening = True
        st.info("Listening...")

    if stop_button:
        is_listening = False
        st.warning("Stopped listening.")

    # Real-time speech-to-text conversion
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        while is_listening:
            try:
                audio_data = recognizer.listen(source, timeout=None)
                text = recognizer.recognize_google(audio_data)
                st.write("Text: ", text)
            except sr.UnknownValueError:
                st.warning("Could not understand audio.")
            except sr.RequestError as e:
                st.error(f"Error connecting to Google API: {e}")

if __name__ == "__main__":
    main()
