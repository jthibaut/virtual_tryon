import streamlit as st
from PIL import Image
import os

#### Main ####
st.title("Virtual Try-On")

uploaded_file = st.file_uploader("Télécharge ta photo", type=["png", "jpg", "jpeg"])
product_choice = st.selectbox("Choisis un vêtement", PRODUCTS)

if uploaded_file:
    user_img = Image.open(uploaded_file)
    st.image(user_img, caption="Ta photo", use_column_width=True)

if product_choice:
    product_img = Image.open(os.path.join(product_dir, product_choice))
    st.image(product_img, caption="Vêtement", use_column_width=True)

if uploaded_file and product_choice:
    st.subheader("Résultat")

    result = simple_tryon(user_img, product_img)
    st.image(result, caption="Essayage virtuel", use_column_width=True)

#### Redimensionne le vêtement et le place automatiquement dans la zone haute du corps ####

def simple_tryon(user_img, product_img):
    user = user_img.convert("RGBA")
    product = product_img.convert("RGBA")

    # Redimensionner le produit en fonction de la largeur du corps
    new_width = int(user.width * 0.5)
    scale = new_width / product.width
    new_height = int(product.height * scale)

    product = product.resize((new_width, new_height))

    # Position approximative du torse : 30% de la hauteur
    position = (int(user.width * 0.25), int(user.height * 0.30))

    # Collage
    user.paste(product, position, product)

    return user
