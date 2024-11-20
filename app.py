import streamlit as st
import cohere

# Initialize Cohere client
API_KEY = "lIZp2slejVX3NPMsfFF1nXFNV5nT2oozR1yY19iy"  # Replace with your actual API key
co = cohere.Client(API_KEY)

# Function to summarize text
def summarize_text(text, length='medium'):
    """
    Summarize text using Cohere's API.

    :param text: The input text to summarize
    :param length: The desired summary length ('short', 'medium', 'long')
    :return: The summarized text or an error message
    """
    try:
        response = co.summarize(
            text=text,
            length=length,  # Options: 'short', 'medium', 'long'
            format='paragraph',  # Options: 'paragraph', 'bullets'
            extractiveness='medium',  # Options: 'low', 'medium', 'high'
            temperature=0.5  # Controls creativity
        )
        return response.summary
    except Exception as e:  # Catch all exceptions
        return f"An error occurred: {e}"

# Streamlit app
def main():
    st.title("Text Summarization App")
    st.write("Powered by Cohere API and Streamlit")
    
    # Text input
    input_text = st.text_area("Enter text to summarize:", height=200)
    
    # Summary length selector
    summary_length = st.radio(
        "Select summary length:",
        options=['short', 'medium', 'long'],
        index=1
    )
    
    if st.button("Summarize"):
        if input_text.strip():
            with st.spinner("Generating summary..."):
                summary = summarize_text(input_text, length=summary_length)
                st.subheader("Summary:")
                st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
