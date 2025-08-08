# import streamlit as st
# from PIL import Image
# import os
# import random

# st.set_page_config(page_title="🧬 PapiLab Educativo", layout="centered")

# # =========================
# # Inicializar variables de sesión
# # =========================
# if "area" not in st.session_state:
#     st.session_state.area = None
# if "imagen_actual" not in st.session_state:
#     st.session_state.imagen_actual = None
# if "intentos" not in st.session_state:
#     st.session_state.intentos = 0
# if "correctas_1" not in st.session_state:
#     st.session_state.correctas_1 = 0
# if "correctas_2" not in st.session_state:
#     st.session_state.correctas_2 = 0
# if "errores" not in st.session_state:
#     st.session_state.errores = 0

# # =========================
# # Función para cargar una nueva imagen
# # =========================
# def nueva_imagen():
#     folder = f"huellas/{st.session_state.area.lower()}es"
#     imagenes = os.listdir(folder)
#     st.session_state.imagen_actual = random.choice(imagenes)
#     st.session_state.intentos = 0

# # =========================
# # Elegir área si aún no se seleccionó
# # =========================
# if st.session_state.area is None:
#     st.title("🧬 PapiLab - Clasificación de Patrones Papilares")
#     st.write("Bienvenido/a 👋 Elige un área para practicar tus habilidades en identificación de huellas.")
#     area_seleccionada = st.selectbox("📍 ¿En qué área deseas practicar?", ["Dactilar", "Palmar", "Plantar"])
#     if st.button("Comenzar ▶️"):
#         st.session_state.area = area_seleccionada
#         nueva_imagen()
#         st.rerun()

# else:
#     st.title(f"🧬 PapiLab - Área: {st.session_state.area}")
#     folder = f"huellas/{st.session_state.area.lower()}es"
    
#     # Mostrar imagen
#     st.image(f"{folder}/{st.session_state.imagen_actual}", width=300)

#     # Opciones de patrón
#     tipo_patron = st.selectbox(
#         "🔍 ¿Qué patrón papilar identificas?",
#         ["Seleccionar", "Arco", "Presilla interna", "Presilla externa", "Verticilo"]
#     )

#     # Subclasificación según patrón
#     subclasificacion = None
#     if tipo_patron == "Arco":
#         subclasificacion = st.selectbox("Subclasificación (Arco)", ["6", "7", "8", "9"])
#     elif tipo_patron in ["Presilla interna", "Presilla externa", "Verticilo"]:
#         subclasificacion = st.selectbox(f"Subclasificación ({tipo_patron})", ["S", "D", "M"])

#     # Botón para confirmar respuesta
#     if st.button("Responder ✅"):
#         if tipo_patron != "Seleccionar":
#             st.session_state.intentos += 1
            
#             # Simulación de respuesta correcta (luego lo conectamos a una base de datos real)
#             respuesta_correcta = "Verticilo"

#             if tipo_patron == respuesta_correcta:
#                 if st.session_state.intentos == 1:
#                     st.session_state.correctas_1 += 1
#                     st.success("🎯 ¡Perfecto! Lo lograste al primer intento.")
#                 else:
#                     st.session_state.correctas_2 += 1
#                     st.info("👍 ¡Bien! Lo lograste en el segundo intento.")
#                 nueva_imagen()
#             else:
#                 if st.session_state.intentos < 2:
#                     st.warning("⚠️ No es correcto... inténtalo de nuevo.")
#                 else:
#                     st.session_state.errores += 1
#                     st.error(f"❌ Incorrecto. La respuesta correcta era: **{respuesta_correcta}**. Revisa la bibliografía 📚.")
#                     nueva_imagen()

#     # Mostrar contadores
#     st.markdown("---")
#     st.subheader("📊 Estadísticas de la sesión")
#     st.write(f"✅ Correctas al primer intento: **{st.session_state.correctas_1}**")
#     st.write(f"👌 Correctas al segundo intento: **{st.session_state.correctas_2}**")
#     st.write(f"❌ Errores: **{st.session_state.errores}**")

#     # Botón para terminar
#     if st.button("Finalizar sesión 🏁"):
#         st.session_state.area = None
#         st.session_state.imagen_actual = None
#         st.session_state.correctas_1 = 0
#         st.session_state.correctas_2 = 0
#         st.session_state.errores = 0
#         st.rerun()

import streamlit as st
from PIL import Image
import os
import random

st.set_page_config(page_title="🧬 PapiLab Educativo", layout="centered")

# =========================
# Opciones de clasificación
# =========================
opciones_del_sistema = {
    "Palmar": {
        "Palmer Pond": ["Tipo 1", "Tipo 2", "Tipo 3"],
        "Stockis": ["Grupo A", "Grupo B", "Grupo C"],
        "Alvariza": ["Clase X", "Clase Y", "Clase Z"]
    },
    "Plantar": {
        "Preller": ["Tipo A", "Tipo B", "Tipo C"],
        "WW": ["Clase I", "Clase II", "Clase III"],
        "Jerlow": ["Forma 1", "Forma 2", "Forma 3"],
        "Urquijo": ["Variante α", "Variante β", "Variante γ"]
    }
}

# =========================
# Inicializar variables de sesión
# =========================
for key, value in {
    "area": None, "imagen_actual": None, "intentos": 0,
    "correctas_1": 0, "correctas_2": 0, "errores": 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================
# Función para cargar una nueva imagen
# =========================
def nueva_imagen():
    folder = f"huellas/{st.session_state.area.lower()}es"
    imagenes = os.listdir(folder)
    st.session_state.imagen_actual = random.choice(imagenes)
    st.session_state.intentos = 0

# =========================
# Elegir área
# =========================
if st.session_state.area is None:
    st.title("🧬 PapiLab - Clasificación de Patrones Papilares")
    st.write("Bienvenido/a 👋 Elige un área para practicar tus habilidades en identificación de huellas.")
    area_seleccionada = st.selectbox("📍 ¿En qué área deseas practicar?", ["Dactilar", "Palmar", "Plantar"])
    if st.button("Comenzar ▶️"):
        st.session_state.area = area_seleccionada
        nueva_imagen()
        st.rerun()

else:
    st.title(f"🧬 PapiLab - Área: {st.session_state.area}")
    folder = f"huellas/{st.session_state.area.lower()}es"
    st.image(f"{folder}/{st.session_state.imagen_actual}", width=300)

    respuesta_usuario = None  # Variable para guardar la respuesta

    if st.session_state.area == "Dactilar":
        tipo_patron = st.selectbox("🔍 ¿Qué patrón papilar identificas?",
                                   ["Seleccionar", "Arco", "Presilla interna", "Presilla externa", "Verticilo"])
        if tipo_patron == "Arco":
            subclasificacion = st.selectbox("Subclasificación (Arco)", ["6", "7", "8", "9"])
        elif tipo_patron in ["Presilla interna", "Presilla externa", "Verticilo"]:
            subclasificacion = st.selectbox("Subclasificación", ["S", "D", "M"])
        respuesta_usuario = tipo_patron

    elif st.session_state.area == "Palmar":
        sistema = st.selectbox("📚 Sistema de clasificación", list(opciones_del_sistema["Palmar"].keys()))
        clasificacion = st.selectbox("Clasificación", opciones_del_sistema["Palmar"][sistema])
        respuesta_usuario = clasificacion

    elif st.session_state.area == "Plantar":
        sistema = st.selectbox("📚 Sistema de clasificación", list(opciones_del_sistema["Plantar"].keys()))
        clasificacion = st.selectbox("Clasificación", opciones_del_sistema["Plantar"][sistema])
        respuesta_usuario = clasificacion

    # =========================
    # Botón para confirmar respuesta
    # =========================
    if st.button("Responder ✅"):
        if respuesta_usuario and respuesta_usuario != "Seleccionar":
            st.session_state.intentos += 1
            respuesta_correcta = "Verticilo"  # Placeholder
            if respuesta_usuario == respuesta_correcta:
                if st.session_state.intentos == 1:
                    st.session_state.correctas_1 += 1
                    st.success("🎯 ¡Perfecto! Lo lograste al primer intento.")
                else:
                    st.session_state.correctas_2 += 1
                    st.info("👍 ¡Bien! Lo lograste en el segundo intento.")
                nueva_imagen()
            else:
                if st.session_state.intentos < 2:
                    st.warning("⚠️ No es correcto... inténtalo de nuevo.")
                else:
                    st.session_state.errores += 1
                    st.error(f"❌ Incorrecto. La respuesta correcta era: **{respuesta_correcta}**. Revisa la bibliografía 📚.")
                    nueva_imagen()

    # =========================
    # Estadísticas
    # =========================
    st.markdown("---")
    st.subheader("📊 Estadísticas de la sesión")
    st.write(f"✅ Correctas al primer intento: **{st.session_state.correctas_1}**")
    st.write(f"👌 Correctas al segundo intento: **{st.session_state.correctas_2}**")
    st.write(f"❌ Errores: **{st.session_state.errores}**")

    if st.button("Finalizar sesión 🏁"):
        for key in ["area", "imagen_actual", "correctas_1", "correctas_2", "errores"]:
            st.session_state[key] = None if key == "area" else 0
        st.rerun()

