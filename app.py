import streamlit as st
import os

# =========================
# Función para mostrar imagen
# =========================
def mostrar_imagen(area, sistema=None):
    ruta = None

    if area == "Dactilar":
        ruta = os.path.join("huellas", "dactilares", "huella1.png")

    elif area == "Palmar" and sistema:
        ruta = os.path.join("huellas", "palmares", "huella1.png")

    elif area == "Plantar" and sistema:
        ruta = os.path.join("huellas", "plantares", "huella1.png")

    if ruta and os.path.exists(ruta):
        st.image(ruta, use_container_width=True)
    else:
        st.info("📷 Aún no hay imagen cargada para esta opción.")


# =========================
# Interfaz principal
# =========================
st.header("🔍 Clasificación de huellas papilares")

area = st.selectbox("Selecciona el área a clasificar:", ["Seleccionar", "Dactilar", "Palmar", "Plantar"])

# =========================
# Área Dactilar
# =========================
if area == "Dactilar":
    mostrar_imagen("Dactilar")

    tipo_patron = st.selectbox("¿Qué patrón papilar identificas?",
                               ["Seleccionar", "Arco", "Presilla interna", "Presilla externa", "Verticilo"])
    
    if tipo_patron == "Arco":
        subclasificacion = st.selectbox("Subclasificación (Arco)", ["6", "7", "8", "9"])
    elif tipo_patron in ["Presilla interna", "Presilla externa", "Verticilo"]:
        subclasificacion = st.selectbox("Subclasificación", ["S", "D", "M"])
    else:
        subclasificacion = None

    if st.button("✅ Enviar respuesta (Dactilar)"):
        if tipo_patron != "Seleccionar" and subclasificacion:
            st.success(f"Respuesta registrada: {tipo_patron} - {subclasificacion}")

# =========================
# Área Palmar
# =========================
elif area == "Palmar":
    sistema_palmar = st.selectbox("Selecciona el sistema Palmar:", ["Seleccionar", "Stockis", "PalmerPond"])
    
    if sistema_palmar != "Seleccionar":
        mostrar_imagen("Palmar", sistema_palmar)

        st.write(f"✍️ Ingresa la clasificación según el sistema **{sistema_palmar}**")

        if sistema_palmar == "Stockis":
            col1, col2, col3 = st.columns(3)
            with col1:
                c1 = st.text_input("Izquierda 1")
            with col2:
                c2 = st.text_input("Izquierda 2")
            with col3:
                c3 = st.text_input("Izquierda 3")
            with col1:
                d1 = st.text_input("Derecha 1")
            with col2:
                d2 = st.text_input("Derecha 2")
            with col3:
                d3 = st.text_input("Derecha 3")
            clasificacion = [c1, c2, c3, d1, d2, d3]

        elif sistema_palmar == "PalmerPond":
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            entradas = []
            for i, col in enumerate([col1, col2, col3, col4, col5, col6], start=1):
                with col:
                    entradas.append(st.text_input(f"Pos {i}"))
            clasificacion = entradas
        else:
            clasificacion = []

        if st.button("✅ Enviar respuesta (Palmar)"):
            st.success(f"Clasificación registrada: {clasificacion}")

# =========================
# Área Plantar
# =========================
elif area == "Plantar":
    sistema_plantar = st.selectbox("Selecciona el sistema Plantar:", ["Seleccionar", "Stockis", "OtroSistema"])
    
    if sistema_plantar != "Seleccionar":
        mostrar_imagen("Plantar", sistema_plantar)

        st.write(f"✍️ Ingresa la clasificación según el sistema **{sistema_plantar}**")

        if sistema_plantar == "Stockis":
            col1, col2, col3 = st.columns(3)
            with col1:
                c1 = st.text_input("Izquierda 1")
            with col2:
                c2 = st.text_input("Izquierda 2")
            with col3:
                c3 = st.text_input("Izquierda 3")
            with col1:
                d1 = st.text_input("Derecha 1")
            with col2:
                d2 = st.text_input("Derecha 2")
            with col3:
                d3 = st.text_input("Derecha 3")
            clasificacion = [c1, c2, c3, d1, d2, d3]

        elif sistema_plantar == "OtroSistema":
            col1, col2, col3, col4 = st.columns(4)
            entradas = []
            for i, col in enumerate([col1, col2, col3, col4], start=1):
                with col:
                    entradas.append(st.text_input(f"Pos {i}"))
            clasificacion = entradas
        else:
            clasificacion = []

        if st.button("✅ Enviar respuesta (Plantar)"):
            st.success(f"Clasificación registrada: {clasificacion}")
