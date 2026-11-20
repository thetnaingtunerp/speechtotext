import io
import speech_recognition as sr
import streamlit as st

st.set_page_config(page_title="Myanmar Speech-to-Text", page_icon="🎙️")
st.title("Myanmar Speech-to-Text (.wav)")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Transcribe (မြန်မာဘာသာ)"):
        recognizer = sr.Recognizer()
        with sr.AudioFile(io.BytesIO(uploaded_file.getvalue())) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="my-MM")
            st.subheader("Transcript")
            st.write(text)
        except sr.UnknownValueError:
            st.warning("အသံကို နားမလည်နိုင်ပါ (Could not understand the audio).")
        except sr.RequestError as e:
            st.error(f"Service error: {e}")
