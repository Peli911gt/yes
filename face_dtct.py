import streamlit as st
import cv2
import numpy as np

# Add instructions to the interface
st.write("# Face Detection App")
st.write("Upload an image and adjust the parameters to detect faces.")

# File uploader for image selection
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded
if uploaded_file is not None:
    # Read the uploaded image
    image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Display the uploaded image
    st.image(image, channels="BGR", caption="Uploaded Image")

    # Parameters for face detection
    min_neighbors = st.slider("minNeighbors", 1, 10, 5)
    scale_factor = st.slider("scaleFactor", 1.1, 2.0, 1.5)

    # Detect faces in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, minNeighbors=min_neighbors, scaleFactor=scale_factor)

    # Draw rectangles around the detected faces
    rect_color = st.color_picker("Rectangle Color", "#FF0000")
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), rect_color, 2)

    # Display the image with detected faces
    st.image(image, channels="BGR", caption="Detected Faces")

    # Save the image with detected faces
    save_image = st.button("Save Image")
    if save_image:
        cv2.imwrite("detected_faces.jpg", image)
        st.write("Image saved successfully.")

# Display the instructions
st.markdown("## Instructions")
st.write("- Upload an image using the file uploader.")
st.write("- Adjust the 'minNeighbors' and 'scaleFactor' sliders to control face detection.")
st.write("- Choose the color of the rectangles using the color picker.")
st.write("- Click on 'Save Image' to save the image with detected faces.")

