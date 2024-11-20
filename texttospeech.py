import streamlit as st
from gtts import gTTS

# Function to convert text to speech using gTTS
def text_to_speech_gtts(text, lang='en'):
    """
    Converts text to speech using gTTS and returns the audio content.
    :param text: Text to be converted to speech.
    :param lang: Language code for the speech (default: 'en').
    :return: Audio content as bytes.
    """
    try:
        # Generate speech
        tts = gTTS(text=text, lang=lang, slow=False)
        # Save to memory and return the audio content
        audio_file = "output.mp3"
        tts.save(audio_file)
        with open(audio_file, "rb") as audio:
            return audio.read()
    except Exception as e:
        return f"An error occurred during text-to-speech: {e}"

# Streamlit app
def main():
    st.title("Text-to-Speech with gTTS")
    st.write("Convert your text into speech using gTTS!")

    # Text input
    input_text = st.text_area("Enter text:", height=200)

    if st.button("Convert to Speech"):
        if input_text.strip():
            with st.spinner("Generating speech..."):
                # Convert the input text to speech using gTTS
                audio_content = text_to_speech_gtts(input_text)
                if isinstance(audio_content, bytes):
                    st.audio(audio_content, format="audio/mp3")
                else:
                    st.error(audio_content)
        else:
            st.warning("Please enter some text to convert to speech.")

if __name__ == "__main__":
    main()
