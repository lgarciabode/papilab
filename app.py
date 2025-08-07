import streamlit as st
from PIL import Image

st.set_page_config(page_title="PapiLab Educativo", layout="centered")

st.title("🧬 Papilab - Clasificación de Patrones Papilares")
st.write("Este es un espacio interactivo para practicar la identificación de patrones papilares")

#Muestra la imagen de una huella
img = Image.open("huellas/huella1.png")
img = img.resize((300, 400))  # ancho x alto en píxeles
st.image(img, caption="Huella dactilar 1")

#Seleccion de patron
opcion = st.selectbox(
    "¿Qué patrón papilar identificas en la huella?",
    ["Seleccionar", "Arco", "Presilla interna", "Presilla externa", "Verticilo"]
)
st.write(f"Elegiste: {opcion}")


#Evalua la respuesta
if opcion != "Seleccionar":
    if opcion == "Verticilo":
        st.success("✅ ¡Correcto! Esta huella es un verticilo.")
    else:
        st.error("❌ Incorrecto. La respuesta correcta es: Verticilo.")
