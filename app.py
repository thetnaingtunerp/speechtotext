import io
import speech_recognition as sr
import streamlit as st

st.set_page_config(page_title="WAV Speech-to-Text", page_icon="🎙️")
st.title("Speech to Text (.wav)")

uploaded_file = st.file_uploader("Upload a WAV audio file", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Transcribe"):
        recognizer = sr.Recognizer()
        # UploadedFile is file-like (BytesIO subclass); read bytes into sr.AudioFile
        with sr.AudioFile(io.BytesIO(uploaded_file.getvalue())) as source:
            audio_data = recognizer.record(source)

        try:
            # Uses Google Web Speech API (requires internet; swap for Whisper/Vosk for offline)
            text = recognizer.recognize_google(audio_data)
            st.subheader("Transcript")
            st.write(text)
        except sr.UnknownValueError:
            st.warning("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Speech recognition service error: {e}")
