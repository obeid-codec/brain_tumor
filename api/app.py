# Library imports
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
from io import BytesIO

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Loading the Model
MODEL = tf.keras.models.load_model("saved_models/tumor.h5")

# Name of Classes
CLASS_NAMES = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# Setting Title of App
st.title("Brain Tumor Prediction")
st.markdown("Upload an image of the Brain MRI")

# Uploading the Brain MRI image
BrMri_image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Predict')

# On predict button click
# On predict button click
if submit:
    if BrMri_image is not None:
        # Open the image using PIL
        img = Image.open(BrMri_image)

        # Convert the image to RGB if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize the image to 512x512 pixels.
        img = img.resize((512, 512))

        # Convert the PIL image to a NumPy array
        image = np.array(img)

        # Displaying the resized image
        st.image(image,
                 use_column_width=True)

        # Preparing the image for prediction
        img_batch = np.expand_dims(image, axis=0)

        # Make Prediction
        predictions = MODEL.predict(img_batch)

        # Output prediction
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])

        if confidence < 0.8:
            st.error("Upload a right image of Brain MRI")
        else:

            st.title(
                f"The Brain MRI shows it has {predicted_class} with confidence {confidence * 100:.2f} %")
