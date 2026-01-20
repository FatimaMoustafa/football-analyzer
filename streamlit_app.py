import streamlit as st
import cv2
import tempfile
import os
from src.pipeline import run_pipeline
import json

st.title("AI Football Analyzer")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    st.text("Original Video:")
    
    video_bytes = open(video_path, 'rb').read()
    st.video(video_bytes)

    if st.button("Analyze"):
        st.text("Analysis started...")

        output_video_path = "outputs/videos/output.mp4"

        video_out, json_out = run_pipeline(video_path, output_video_path)

        st.text("Analysis finished!")

        st.text("Output Video:")
        st.video(video_out)

        
        with open(json_out, "r") as f:
            data = json.load(f)
        st.write("Tracks JSON:")
        st.json(data)

