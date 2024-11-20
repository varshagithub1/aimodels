import streamlit as st
import requests

# Define your Synthesia API key here
SYNTHESIA_API_KEY = 'your_synthesia_api_key'  # Replace with your Synthesia API key
SYNTHESIA_API_URL = 'https://api.synthesia.io/v1/video/generate'  # Synthesia API endpoint

# Function to generate a video with Synthesia
def generate_synthesia_video(text, language="en", avatar="synthesia_avatar"):
    try:
        # Set up the request payload
        payload = {
            "text": text,
            "language": language,
            "avatar": avatar,
            "style": "default",  # You can adjust the style as per your requirements
        }

        headers = {
            'Authorization': f'Bearer {SYNTHESIA_API_KEY}',
            'Content-Type': 'application/json'
        }

        # Send the request to Synthesia API
        response = requests.post(SYNTHESIA_API_URL, json=payload, headers=headers)

        # Check for success
        if response.status_code == 200:
            video_url = response.json().get("video_url", "")
            return video_url
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI to accept input from the user
def main():
    st.title("Text-to-Video Generator with Synthesia")
    st.write("Generate a video using Synthesia's text-to-video API!")

    # User input for story or text
    input_text = st.text_area("Enter the text to convert into a video:", height=200)

    # Language and Avatar options
    language = st.selectbox("Select Language", ["en", "fr", "de", "es"])
    avatar = st.selectbox("Select Avatar", ["synthesia_avatar", "custom_avatar"])

    if st.button("Generate Video"):
        if input_text.strip():
            with st.spinner("Generating video..."):
                # Generate video from text using Synthesia
                video_url = generate_synthesia_video(input_text, language, avatar)
                
                # Display the video link
                if video_url.startswith("http"):
                    st.subheader("Video Generated Successfully!")
                    st.video(video_url)  # Display the video directly in Streamlit
                else:
                    st.error(video_url)  # Display error message
        else:
            st.warning("Please enter some text to generate a video.")

if __name__ == "__main__":
    main()
