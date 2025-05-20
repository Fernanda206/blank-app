import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

import unicodedata

paginas= ["Guía de uso (Inicio)", "Clasificar desechos", "Ver guía de clasificación", "Ver ideas de reciclaje"]
pagina= pagina = st.sidebar.selectbox("Selecciona una página", paginas)


if pagina== "Guía de uso (Inicio)":
    st.image(r"C:\Users\CompuFire\OneDrive\Documents\U FER\ecocode.png" )
    st.title("Bienvenido a EcoCode")
    st.write("Bienvenido usuario al programa de reciclaje")
    st.write("Puedes seleccionar la opción que desees ejecutar del menú lateral izquierdo")
    st.markdown("""
- Opciones a seleccionar:
    - Clasificar desechos: Opcion para ingresar el nombre de un desecho y el programa te indicará cual es el contenedor correcto para desecharlo.
    - Ver guía de clasificación: El programa te mostrará una guía para que puedas utilizarla al clasificar desechos.
    - Ver ideas de reciclaje: El programa te dará la opción de ingresar un desecho y te mostrará ideas para reutilizarlo.
""")

elif pagina== "Clasificar desechos":
    col1, col2, col3 = st.columns([1, 1, 2])

    with col3:
        st.image(r"C:\Users\CompuFire\OneDrive\Documents\U FER\ecocode.png", width=200)
        

# Diccionario base de clasificación
clasificar={
    "papel": "azul",
    "carton": "azul",
    "revista": "azul",
    "vidrio": "verde",
    "botella de vidrio": "verde",
    "frasco": "verde",
    "plastico": "amarillo",
    "botella de plastico": "amarillo",
    "bolsa de plastico": "amarillo",
    "resto de comida": "naranja",
    "cascara": "naranja",
    "pan": "naranja",
    "jeringa": "rojo",
    "gasa": "rojo",
    "panal": "gris",
    "esponja sucia": "gris",
    "carton sucio": "gris"
    }

def normalizar(texto):
    # Convierte a minúsculas y elimina tildes
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto
# Agregamos más desechos normalizados
for item in {
    "cascara de platano", "cascara de manzana", "cascara de naranja", "cascara de pera",
    "pan", "pasteles", "huesos pequenos", "posos de cafe", "bolsas de te usadas",
    "cascara de huevo", "restos de comida", "flores marchitas"
}:
    clasificar[normalizar(item)] = "naranja"

for item in {
    "botellas de vidrio", "tarros de vidrio", "vasos de vidrio", "jarras de vidrio", "frascos de vidrio"
}:
    clasificar[normalizar(item)] = "verde"

for item in {
    "botellas de plastico", "bolsas de plastico", "tapas de plastico", "envases de plastico"
}:
    clasificar[normalizar(item)] = "amarillo"

for item in {
    "latas de aluminio", "latas de hierro", "latas de acero", "latas de cobre"
}:
    clasificar[normalizar(item)] = "amarillo"

for item in {
    "cajas de carton", "periodicos", "hojas de papel"
}:
    clasificar[normalizar(item)] = "azul"

ideas_reciclaje = {
    "botella de plastico": "Usar como maceta.",
    "carton": "Hacer una caja organizadora.",
    "frasco": "Guardar botones o clips.",
    "papel": "Notas o borradores.",
    "bolsa de plastico": "Forrar cestos.",
    "botellas de plastico": "Maceteros, sistemas de riego o lámparas.",
    "botes de vidrio": "Portalápices, frascos decorativos.",
    "latas": "Macetas, organizadores.",
    "ropa vieja": "Trapos, cojines, bolsas de tela.",
    "cajas de carton": "Juguetes, organizadores o compostaje."
}

# Streamlit app
st.title("EcoCode - Clasificación de Desechos")

opcion = st.sidebar.radio("Selecciona una opción", ["Clasificar desecho", "Guía de clasificación", "Ideas de reciclaje"])

# Opción 1: Clasificar desecho
if opcion == "Clasificar desecho":
    st.subheader("Clasificador de Desechos")
    desecho = st.text_input("Ingrese el desecho a clasificar:")
    if desecho:
        desecho_normalizado = normalizar(desecho)
        contenedor = clasificar.get(desecho_normalizado)
        if contenedor:
            st.success(f"El desecho **'{desecho}'** se clasifica en el basurero: **{contenedor.upper()}**")
        else:
            st.warning("Ese desecho no está registrado.")
            if st.checkbox("¿Querés clasificarlo manualmente?"):
                nuevo_color = st.selectbox("Selecciona un basurero", ["azul", "verde", "amarillo", "naranja", "rojo", "gris"])
                clasificar[desecho_normalizado] = nuevo_color
                st.info(f"'{desecho}' fue agregado como '{nuevo_color.upper()}' (temporalmente).")

# Opción 2: Guía de clasificación
elif opcion == "Guía de clasificación":
    st.subheader("Guía de clasificación")
    guia = {}
    for des, color in clasificar.items():
        guia.setdefault(color, []).append(des)

    for color in sorted(guia.keys()):
        st.markdown(f"### ️ {color.upper()}")
        st.markdown(", ".join(sorted(guia[color])))

# Opción 3: Ideas de reciclaje
elif opcion == "Ideas de reciclaje":
    st.subheader(" Ideas para reciclar")
    desecho = st.text_input("Ingrese el desecho:")
    if desecho:
        desecho_normalizado = normalizar(desecho)
        idea = ideas_reciclaje.get(desecho_normalizado)
        if idea:
            st.info(f"Idea para '{desecho}': {idea}")
        else:
            st.warning("No hay idea disponible para ese desecho.")

st.markdown("---")
st.markdown(" Gracias por ser parte de la comunidad EcoCode")

    
    