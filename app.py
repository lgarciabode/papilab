import streamlit as st
from PIL import Image
import os
import random

st.set_page_config(page_title="PapiLab Educativo", layout="centered")

st.title("🧬 Papilab - Clasificación de Patrones Papilares")
st.write("Este es un espacio interactivo para practicar la identificación de patrones papilares")

#Selector de area
area = st.selectbox("¿En qué área deseas practicar?", ["Dactilar", "Palmar", "Plantar"]
)

folder = f"huellas/{area.lower()}es"
imagenes = os.listdir(folder)
imagen_seleccionada = random.choice(imagenes)
st.image(f"{folder}/{imagen_seleccionada}",  width=400) #use_container_width=True,


#Seleccion de patron
tipo_patron = st.selectbox(
    "¿Qué patrón papilar identificas en la huella?",
    ["Seleccionar", "Arco", "Presilla interna", "Presilla externa", "Verticilo"]
)
st.write(f"Elegiste: {tipo_patron}")


#Evalua la respuesta
if tipo_patron != "Seleccionar":
    if tipo_patron == "Verticilo":
        st.success("✅ ¡Correcto! Esta huella es un verticilo.")
    else:
        st.error("❌ Incorrecto. La respuesta correcta es: Verticilo.")

if tipo_patron == "Arco":
        subclasificacion = st.selectbox("Subclasificación (Arco)", ["6", "7", "8", "9"])
elif tipo_patron in ["Presilla", "Verticilo"]:
        subclasificacion = st.selectbox(f"Subclasificación ({tipo_patron})", ["S", "D", "M"])
