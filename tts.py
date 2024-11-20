import streamlit as st
import requests

# Set up ElevenLabs API
API_KEY = "sk_3ab51a98593b06d6551ad836ea64757385ddcc5074d50872"  # Replace with your ElevenLabs API key
BASE_URL = "https://api.elevenlabs.io/v1"

# Function to convert text to speech using ElevenLabs API
def text_to_speech_elevenlabs(text, voice="Rachel"):
    """
    Converts text to speech using ElevenLabs API.
    :param text: Text to convert to speech.
    :param voice: Voice name (optional, default is "Rachel").
    :return: Audio content or error message.
    """
    try:
        # Set up headers and payload for the request
        headers = {
            "Content-Type": "application/json",
            "xi-api-key": API_KEY,
        }

        # Get available voices from the API
        voices_response = requests.get(f"{BASE_URL}/voices", headers=headers)
        if voices_response.status_code != 200:
            return None, "Error fetching available voices."

        voices = voices_response.json().get("voices", [])
        voice_id = next((v["voice_id"] for v in voices if v["name"] == voice), None)
        if not voice_id:
            return None, f"Voice '{voice}' not found."

        # Prepare the payload for the TTS request
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8
            }
        }

        # Make the request to ElevenLabs' Text-to-Speech API
        tts_response = requests.post(f"{BASE_URL}/text-to-speech/{voice_id}", json=payload, headers=headers)
        
        if tts_response.status_code == 200:
            return tts_response.content, None
        else:
            return None, f"Error during TTS: {tts_response.text}"
    
    except Exception as e:
        return None, f"An error occurred: {e}"

# Streamlit app to interact with the user
def main():
    st.title("Text to Speech with ElevenLabs")
    st.write("Enter some text, select a voice, and hear the speech!")

    # Text input for user
    text_input = st.text_area("Enter text to convert to speech:", height=150)

    # Voice selection dropdown
    voice_name = st.selectbox("Select a voice:", ["Rachel", "Antoni", "Bella", "Domi", "Elli", "Josh"])

    # Button to generate speech
    if st.button("Generate Speech"):
        if text_input.strip():
            with st.spinner("Generating speech..."):
                audio_content, error = text_to_speech_elevenlabs(text_input, voice=voice_name)
                if audio_content:
                    st.audio(audio_content, format="audio/mpeg")
                else:
                    st.error(error)
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()
