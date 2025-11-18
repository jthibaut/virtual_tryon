import streamlit as st
from PIL import Image
import os

# Dossier contenant les vêtements
product_dir = "PRODUCTS"

# Liste des fichiers images dans le dossier
products = [f for f in os.listdir(product_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

st.title("Virtual Try-On")

# Fonction simple de collage
def simple_tryon(user_img, product_img):
    user = user_img.convert("RGBA")
    product = product_img.convert("RGBA")

    # Redimensionner le produit (50% de la taille du corps)
    new_width = int(user.width * 0.5)
    scale = new_width / product.width
    new_height = int(product.height * scale)

    product = product.resize((new_width, new_height))

    # Position approximative sur le torse
    position = (int(user.width * 0.25), int(user.height * 0.30))

    # Collage avec transparence
    user.paste(product, position, product)

    return user

# Upload utilisateur
uploaded_file = st.file_uploader("Télécharge ta photo", type=["png", "jpg", "jpeg"])

# Sélection du vêtement
product_choice = st.selectbox("Choisis un vêtement", products)

if uploaded_file:
    user_img = Image.open(uploaded_file)
    st.image(user_img, caption="Ta photo", use_column_width=True)

# Prévisualisation du vêtement
if product_choice:
    product_img = Image.open(os.path.join(product_dir, product_choice))
    st.image(product_img, caption="Vêtement", use_column_width=True)

# Résultat
if uploaded_file and product_choice:
    st.subheader("Résultat de l'essayage")

    result = simple_tryon(user_img, product_img)
    st.image(result, caption="Essayage virtuel", use_column_width=True)
