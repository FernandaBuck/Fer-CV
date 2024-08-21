import streamlit as st

# Título del CV
st.title("Fernanda Buck")

# Creando las columnas
col1, col2 = st.columns(2)

with col1:
    # Información personal
    st.header("Información Personal")
    st.markdown("""
    - **Nombre:** María Fernanda Buck Nuñez
    - **Correo Electrónico:** fernandabuckn@outlook.com
    - **Teléfono:** 477 648 7258
    """)

    # Educación
    st.header("Educación")
    st.markdown("""
    **Licenciatura en Administración y Finanzas**
    Universidad Panamericana, Zapopan, Jal.
    Agosto 2020 - Diciembre 2024

    **Certificación SAP**
    Universidad Panamericana, Zapopan, Jal.
    Agosto 2023 - Diciembre 2023

    **Certificate III in Business**
    Lonsdale Institute, Melbourne, Aus. 
    Sep 2019 - Feb 2020
    """)

    # Idiomas
    st.header("Idiomas")
    st.markdown("""
    - Español - Nativo
    - Inglés - Avanzado
    """)

with col2:
    # Resumen profesional
    st.header("Resumen Profesional")
    st.markdown("""
    Actualmente, me encuentro en el octavo semestre de la carrera de Administración y Finanzas en la Universidad Panamericana, campus
 """)