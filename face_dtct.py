import streamlit as st
import numpy as np
from PIL import Image
import face_recognition
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

        # Convert image to RGB
        image_rgb = np.array(image.convert('RGB'))

        # Detect faces
        face_locations = face_recognition.face_locations(image_rgb, model="hog")

        # Get rectangle color from user
        rect_color = st.color_picker("Rectangle Color", "#ff0000")

        # Draw rectangles around the detected faces
        image_draw = image.copy()
        draw = ImageDraw.Draw(image_draw)
        for (top, right, bottom, left) in face_locations:
            draw.rectangle(((left, top), (right, bottom)), outline=rect_color, width=2)

        # Display the annotated image
        st.image(image_draw, caption='Annotated Image', use_column_width=True)

        # Save the annotated image
        save_button = st.button("Save Image")
        if save_button:
            image_draw.save("annotated_image.jpg")
            st.success("Image saved successfully.")

if __name__ == '__main__':
    main()
