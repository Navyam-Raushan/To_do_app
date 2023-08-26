import streamlit as st
from PIL import Image

st.title("Grayscale image maker.")

# adding a new feature of browsing the file

uploaded_image = st.file_uploader("Upload Your Image")

# Need more control over the camera as it open directly

with st.expander("Start camera"):
    # Started the camera
    img_input = st.camera_input("Camera")

# starting conversion to grayscale
# if img is not taken then img_input is NONE
if img_input:
    # Created an image instance
    img = Image.open(img_input)

    # conversion into gray img with L algorithm
    gray_img = img.convert("L")

    # show the image
    st.image(gray_img)
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)


