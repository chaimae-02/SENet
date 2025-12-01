import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet import preprocess_input
from PIL import Image
import os

# -------------------------
# 1) Charger le modèle
# -------------------------
MODEL_PATH = "best_model.keras"

if not os.path.exists(MODEL_PATH):
    st.error(f" Fichier modèle introuvable : {MODEL_PATH}")
    st.stop()

model = load_model(MODEL_PATH)

# -------------------------
# 2) Charger les noms des classes
# -------------------------
CLASS_DIR = "data_split/train"

if not os.path.exists(CLASS_DIR):
    st.error(f" Dossier classes introuvable : {CLASS_DIR}")
    st.stop()

class_names = sorted(os.listdir(CLASS_DIR))


# -------------------------
# 3) Fonction de prétraitement
# -------------------------
def preprocess_image(img):
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img)
    img = preprocess_input(img)   # IMPORTANT pour ResNet
    img = np.expand_dims(img, axis=0)
    return img


# -------------------------
# 4) Interface Streamlit
# -------------------------
st.title("🌿 Disease Classification App")
st.write("Upload an image of a leaf to classify the disease.")

uploaded_file = st.file_uploader("Choisir une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Afficher l’image
    image = Image.open(uploaded_file)
    st.image(image, caption="Image chargée", use_column_width=True)

    # Prétraitement
    x = preprocess_image(image)

    # Prédiction
    preds = model.predict(x)
    predicted_index = np.argmax(preds)
    predicted_name = class_names[predicted_index]

    st.subheader("✨ Prédiction")
    st.success(predicted_name)
