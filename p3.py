import streamlit as st
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO

st.set_page_config(page_title="Object Detection & Tracking")

st.title("🎯 Object Detection & Tracking ")


@st.cache_resource
def load_model():
    model = YOLO("yolov8n.pt")  
    return model

model = load_model()


st.subheader("📂 Upload Video")
video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

use_webcam = st.checkbox("Use Webcam")


def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

       
        results = model.track(frame, persist=True)

        annotated_frame = results[0].plot()

      
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

        stframe.image(annotated_frame, channels="RGB")

    cap.release()



if st.button("🚀 Start Detection"):

    if use_webcam:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model.track(frame, persist=True)
            annotated_frame = results[0].plot()

            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            stframe.image(annotated_frame, channels="RGB")

        cap.release()

    elif video_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        process_video(tfile.name)

    else:
        st.error("Please upload a video or enable webcam!")