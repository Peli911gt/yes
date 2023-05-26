import cv2
import numpy as np
import streamlit as st

# Function to detect faces
def detect_faces(image, scaleFactor, minNeighbors):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
    return faces

# Streamlit app
def main():
    st.title("Face Detection App")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    # Instructions
    st.write("Instructions:")
    st.write("1. Upload an image using the 'Upload an image' button.")
    st.write("2. Adjust the parameters for face detection.")
    st.write("3. Click the 'Detect Faces' button to detect faces in the image.")
    st.write("4. Adjust the 'Scale Factor' and 'Min Neighbors' sliders to improve the face detection results.")
    st.write("5. Choose the color of the rectangles using the 'Rectangle Color' color picker.")
    st.write("6. Click the 'Save Image' button to save the image with the detected faces.")

    if uploaded_file is not None:
        image = cv2.imread(uploaded_file.name)
        st.image(image, channels="BGR")

        # Parameters for face detection
        scaleFactor = st.slider("Scale Factor", 1.1, 3.0, 1.2, 0.1)
        minNeighbors = st.slider("Min Neighbors", 1, 10, 5)

        # Choose the color of the rectangles
        rect_color = st.color_picker("Rectangle Color", "#FF0000")

        # Detect faces
        faces = detect_faces(image, scaleFactor, minNeighbors)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), tuple(int(rect_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)), 2)

        st.image(image, channels="BGR")

        # Save image
        if st.button("Save Image"):
            cv2.imwrite("result.jpg", image)
            st.success("Image saved successfully.")

if __name__ == "__main__":
    main()
