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

    # Habilidades
    st.header("Habilidades")
    st.markdown("""
    - Toma de Decisiones
    - Trabajo en Equipo 
    - Solución de Problemas 
    - Liderazgo
    - Excel 
    """)

with col2:
    # Resumen profesional
    st.header("Resumen Profesional")
    st.markdown("""
    Actualmente, me encuentro en el octavo semestre de la carrera de Administración y Finanzas en la Universidad Panamericana, campus Guadalajara. Soy una persona altamente organizada y proactiva, siempre comprometida a dar lo mejor de mí en todas mis actividades. Disfruto trabajar en equipo y considero que la colaboración es clave para alcanzar metas exitosas. Estoy en búsqueda de desafíos profesionales que me permitan crecer y superarme.
    """)

    # Experiencia profesional
    st.header("Experiencia Profesional")
    st.markdown("""
    ### Pasante en Contabilidad y Administración
    **[Wilson Abogados S.C] / Abril 2021 - Agosto 2022**
    - Apoyo en registro contable y administrativo de operaciones propias del despacho y de clientes externos.
    - Apoyo en el desarrollo de modelos de análisis propios y para clientes.
    - Contabilidad y Finanzas.

    ### Presidente del Comité de Administración y Finanzas
    **[Universidad Panamericana] / Enero - Diciembre 2023**
    - Coordinación de un equipo de 20 estudiantes para llevar a cabo actividades para más de 600 estudiantes.
    - Organización de eventos, gestión de relaciones públicas y análisis de estados financieros para la toma de decisiones estratégicas.

    ### Área de Operaciones 
    **[Inmobiliaria Magnum] / Enero 2020 - 2023**
    - Atención al cliente y captación de nuevos prospectos.
    - Seguimiento y cierre de operaciones internas. 
    - Análisis de información financiera y control administrativo para la toma de decisiones.
    """)


