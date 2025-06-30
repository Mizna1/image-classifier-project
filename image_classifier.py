import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.applications import MobileNetV2

st.title("📷 Image Classifier Project")
st.write("Upload an image. The AI model will identify what's in it using deep learning!")

@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Classifying..."):
        try:
            img_resized = image.resize((224, 224))
            img_array = np.array(img_resized)
            img_batch = np.expand_dims(img_array, axis=0)
            img_preprocessed = preprocess_input(img_batch)

            predictions = model.predict(img_preprocessed)
            decoded = decode_predictions(predictions, top=3)[0]

            st.success("Done!")
            st.write("### Predictions:")
            for i, (imagenetID, label, prob) in enumerate(decoded):
                st.write(f"**{i+1}. {label}** — {prob*100:.2f}%")

        except Exception as e:
            st.error(f"Something went wrong during prediction: {e}")
