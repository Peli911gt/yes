import streamlit as st
import numpy as np
from PIL import Image
import cv2

def main():
    st.title("Face Detection App")

    # Add instructions
    st.write("Upload an image and click the 'Detect Faces' button to detect faces.")
    st.write("Adjust the parameters below to customize the face detection.")

    # Upload image file
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load image
        image = Image.open(uploaded_file)
        image_array = np.array(image)

        # Detect faces
        min_neighbors = st.slider("minNeighbors", min_value=1, max_value=10, value=5, step=1)
        scale_factor = st.slider("scaleFactor", min_value=1.1, max_value=2.0, value=1.5, step=0.1)

        # Create face cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Convert image to grayscale
        gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray_image, minNeighbors=min_neighbors, scaleFactor=scale_factor)

        # Get rectangle color from user
        rect_color = st.color_picker("Rectangle Color", "#ff0000")

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image_array, (x, y), (x+w, y+h), rect_color, 2)

        # Display the annotated image
        st.image(image_array, caption='Annotated Image', use_column_width=True)

        # Save the annotated image
        save_button = st.button("Save Image")
        if save_button:
            cv2.imwrite("annotated_image.jpg", image_array)
            st.success("Image saved successfully.")

if __name__ == '__main__':
    main()
