import cv2
import streamlit as st
import os
os.environ['LD_PRELOAD'] = '/usr/lib/x86_64-linux-gnu/libGL.so'

# Add instructions to the interface
st.write("# Face Detection App")
st.write("Upload an image and adjust the parameters to detect faces.")

# Load the Haar cascade xml file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Upload image file
uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read the image
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Adjustable parameters
    rect_color = st.color_picker("Rectangle Color", "#FF0000")
    min_neighbors = st.slider("minNeighbors", 1, 10, 5)
    scale_factor = st.slider("scaleFactor", 1.1, 2.0, 1.1)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), rect_color, 2)

    # Display the image with detected faces
    st.image(image, channels="BGR")

    # Save the image with detected faces
    if st.button("Save Image"):
        cv2.imwrite("detected_faces.jpg", image)
        st.success("Image saved successfully!")
