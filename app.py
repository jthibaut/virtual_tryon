import streamlit as st
from PIL import Image
import os

st.title("Essayage Virtuel IA - Démo Overlay")

st.write("Téléversez une photo de vous, puis sélectionnez un vêtement à superposer.")

uploaded = st.file_uploader("Votre photo", type=["jpg","jpeg","png"])

# Liste des produits disponibles
product_dir = "PRODUCTS"
products = [f for f in os.listdir(product_dir) if f.lower().endswith(('.png','.jpg','.jpeg'))]

selected = st.selectbox("Choisissez un produit", ["Aucun"] + products)

if uploaded:
    user_img = Image.open(uploaded).convert("RGBA")
    st.image(user_img, caption="Votre image", use_column_width=True)

    if selected != "Aucun":
        prod_img = Image.open(os.path.join(product_dir, selected)).convert("RGBA")
        prod_img = prod_img.resize((user_img.width, user_img.height))
        combined = Image.alpha_composite(user_img, prod_img)
        st.image(combined, caption="Essayage virtuel", use_column_width=True)
else:
    st.info("Veuillez téléverser une image.")
