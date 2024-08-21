import streamlit as st

# CSS personalizado para ajustar márgenes y espaciado
st.markdown("""
    <style>
        .header {
            margin-bottom: 5px; /* Reducir margen inferior del encabezado */
        }
        .content {
            margin-top: -20px; /* Ajustar margen superior del contenido */
        }
        .block-container {
            padding-top: 10px; /* Ajustar margen superior de la página */
            padding-left: 20px; /* Ajustar margen izquierdo */
            padding-right: 20px; /* Ajustar margen derecho */
            padding-bottom: 10px; /* Ajustar margen inferior */
        }
    </style>
""", unsafe_allow_html=True)

# Título del CV
st.title("Fernanda Buck")

# Resumen profesional
st.header("Resumen Profesional", className="header")
st.markdown("""
<div class="content">
Actualmente, me encuentro en el octavo semestre de la carrera de Administración y Finanzas en la Universidad Panamericana, campus Guadalajara. Soy una persona altamente organizada y proactiva, siempre comprometida a dar lo mejor de mí en todas mis actividades. Disfruto trabajar en equipo y considero que la colaboración es clave para alcanzar metas exitosas. Estoy en búsqueda de desafíos profesionales que me permitan crecer y superarme.
</div>
""", unsafe_allow_html=True)

# Creando las columnas
col1, col2 = st.columns(2)

with col1:
    # Información personal
    st.header("Información Personal", className="header")
    st.markdown("""
    <div class="content">
    **Nombre:** María Fernanda Buck Nuñez  
    **Correo Electrónico:** fernandabuckn@outlook.com  
    **Teléfono:** 477 648 7258
    </div>
    """, unsafe_allow_html=True)

    # Educación
    st.header("Educación", className="header")
    st.markdown("""
    <div class="content">
    **Licenciatura en Administración y Finanzas**  
    Universidad Panamericana, Zapopan, Jal.  
    Agosto 2020 - Diciembre 2024

    **Certificación SAP**  
    Universidad Panamericana, Zapopan, Jal.  
    Agosto 2023 - Diciembre 2023

    **Certificate III in Business**  
    Lonsdale Institute, Melbourne, Aus.  
    Sep 2019 - Feb 2020
    </div>
    """, unsafe_allow_html=True)

    # Idiomas
    st.header("Idiomas", className="header")
    st.markdown("""
    <div class="content">
    - Español - Nativo
    - Inglés - Avanzado
    </div>
    """, unsafe_allow_html=True)

    # Habilidades
    st.header("Habilidades", className="header")
    st.markdown("""
    <div class="content">
    - Toma de Decisiones
    - Trabajo en Equipo 
    - Solución de Problemas 
    - Liderazgo
    - Excel 
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Experiencia profesional
    st.header("Experiencia Profesional", className="header")
    st.markdown("""
    <div class="content">
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
    </div>
    """, unsafe_allow_html=True)


