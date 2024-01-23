# Real-time Speech-to-Text Conversion with Streamlit

This is a simple Streamlit app that performs real-time speech-to-text conversion using the SpeechRecognition library. The app allows users to start and stop the conversion process with dedicated buttons.

## Installation

To run this application, you need to have Python installed. Then, install the required dependencies by running:

## How to Use

1. Install the required libraries:

    ```bash
    pip install pyaudio SpeechRecognition streamlit
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run your_app_name.py
    ```

Replace `your_app_name.py` with the name of your Python script.

3. Open your web browser and go to `http://localhost:8501` to interact with the app.

## Features

- **Start Conversion:** Click the "Start Conversion" button to initiate the speech-to-text conversion process.

- **Stop Conversion:** Click the "Stop Conversion" button to stop the conversion process at any time.

## Dependencies

- Streamlit
- SpeechRecognition

## Notes

- Make sure to speak into the microphone when the app is in the listening state.

- Adjust microphone sensitivity if needed by modifying the `recognizer.adjust_for_ambient_noise` method.

- If there are issues with understanding the audio, check for errors in the console and ensure a stable internet connection for Google API requests.

## Acknowledgments

This app uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library for speech recognition and [Streamlit](https://streamlit.io/) for creating the web interface.

## Author

[Aman Singh Chauhan]
