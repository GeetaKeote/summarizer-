import streamlit as st
from video_summarize import generate_summary

st.title("Video Transcript Summarizer")

# Input field for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")

if st.button("Generate Summary"):
    if youtube_url:
        # Generate summary
        summary = generate_summary(youtube_url)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter a valid YouTube URL.")

# No need for main() here, Streamlit automatically runs code within the script
