import streamlit as st
import cv2
import numpy as np

def detect_faces(image, scale_factor, min_neighbors, rect_color):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scale_factor, min_neighbors)
    for (x, y, w, h) in faces:
        bgr_color = tuple(int(rect_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        cv2.rectangle(image, (x, y), (x + w, y + h), bgr_color, 2)
    return image

def main():
    st.title("Face Detection App")
    st.write("Please upload an image.")
    image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        image = np.array(bytearray(image_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        scale_factor = st.slider("Scale Factor", min_value=1.1, max_value=3.0, step=0.1, value=1.2)
        min_neighbors = st.slider("Min Neighbors", min_value=1, max_value=10, step=1, value=5)
        rect_color = st.color_picker("Rectangle Color", value="#FF0000")

        if st.button("Detect Faces"):
            result_image = detect_faces(image, scale_factor, min_neighbors, rect_color)
            st.image(result_image, channels="BGR")

            save_option = st.checkbox("Save Image")
            if save_option:
                cv2.imwrite("result_image.jpg", result_image)
                st.success("Image saved successfully.")

if __name__ == "__main__":
    main()
