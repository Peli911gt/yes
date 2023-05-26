import streamlit as st
import cv2
import numpy as np

# Function to detect faces and draw rectangles
def detect_faces(image, scaleFactor, minNeighbors, rect_color):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), rect_color, 2)

    return image

def main():
    # Title and instructions
    st.write("# Face Detection App")
    st.write("Upload an image and adjust the parameters to detect and visualize faces.")

    # Upload an image file
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = np.array(cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1))

        # Display the original image
        st.image(image, channels="BGR", caption="Original Image")

        # Adjust the parameters
        min_neighbors = st.slider("Adjust minNeighbors", 1, 10, 5)
        scale_factor = st.slider("Adjust scaleFactor", 1.1, 2.0, 1.2, step=0.1)
       cv2.rectangle(image, (x, y), (x + w, y + h), (int(rect_color[0]), int(rect_color[1]), int(rect_color[2])), 2)


        # Detect faces and draw rectangles
        result_image = detect_faces(image, scale_factor, min_neighbors, rect_color)

        # Display the result image with detected faces
        st.image(result_image, channels="BGR", caption="Result Image")

        # Save the result image
        if st.button("Save Image"):
            cv2.imwrite("result_image.jpg", result_image)
            st.write("Image saved successfully!")

if __name__ == "__main__":
    main()
