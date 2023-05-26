import streamlit as st
import numpy as np
from PIL import Image
import dlib

# Load the pre-trained face detector from dlib
face_detector = dlib.get_frontal_face_detector()

# Function to detect faces in an image
def detect_faces(image):
    # Convert the image to grayscale
    gray = np.array(image.convert("L"))

    # Detect faces using the dlib face detector
    faces = face_detector(gray)

    return faces

# Streamlit app
def main():
    st.title("Face Detection App")
    st.write("Upload an image and detect faces!")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Detect faces in the image
        faces = detect_faces(image)

        if len(faces) > 0:
            st.write(f"Number of faces detected: {len(faces)}")

            # Draw rectangles around the detected faces
            image_with_faces = np.array(image)
            for face in faces:
                left = face.left()
                top = face.top()
                right = face.right()
                bottom = face.bottom()
                cv2.rectangle(image_with_faces, (left, top), (right, bottom), (255, 0, 0), 2)

            st.image(image_with_faces, caption="Faces Detected", use_column_width=True)

            # Save image with detected faces
            save_button = st.button("Save Image with Detected Faces")
            if save_button:
                image_with_faces_pil = Image.fromarray(image_with_faces)
                image_with_faces_pil.save("image_with_faces.jpg")
                st.write("Image with detected faces saved successfully!")

        else:
            st.write("No faces detected in the image.")

# Run the app
if __name__ == "__main__":
    main()
