st.write("Welcome to the Face Detection App!")
st.write("Please upload an image and adjust the parameters to detect faces.")
# Save the image with detected faces
cv2.imwrite("output.jpg", image)
st.write("Image saved successfully!")
# Allow the user to choose the color
rect_color = st.color_picker("Rectangle Color", "#FF# Allow the user to adjust the scaleFactor parameter
scale_factor = st.slider("scaleFactor", min_value=1.1, max_value=2.0, value=1.2, step=0.1)
0000")
# Allow the user to adjust the minNeighbors parameter
min_neighbors = st.slider("minNeighbors", min_value=1, max_value=10, value=3, step=1)
