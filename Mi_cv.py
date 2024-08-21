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
st.markdown("""
<h2 style='margin-bottom: 5px;'>Resumen Profesional</h2>
<p style='margin-top: -20px;'>
Actualmente, me encuentro en el octavo semestre de la carrera de Administración y Finanzas en la Universidad Panamericana, campus Guadalajara. Soy una persona altamente organizada y proactiva, siempre comprometida a dar lo mejor de mí en todas mis actividades. Disfruto trabajar en equipo y considero que la colaboración es clave para alcanzar metas exitosas. Estoy en búsqueda de desafíos profesionales que me permitan crecer y superarme.
</p>
""", unsafe_allow_html=True)

# Creando las columnas
col1, col2 = st.columns(2)

with col1:
    # Información personal
    st.markdown("""
    <h2 style='margin-bottom: 5px;'>Información Personal</h2>
    <div style='margin-top: -20px;'>
    <p><strong>Nombre:</strong> María Fernanda Buck Nuñez</p>
    <p><strong>Correo Electrónico:</strong> fernandabuckn@outlook.com</p>
    <p><strong>Teléfono:</strong> 477 648 7258</p>
    </div>
    """, unsafe_allow_html=True)

    # Educación
    st.markdown("""
    <h2 style='margin-bottom: 5px;'>Educación</h2>
    <div style='margin-top: -20px;'>
    <p><strong>Licenciatura en Administración y Finanzas</strong><br/>
    Universidad Panamericana, Zapopan, Jal.<br/>
    Agosto 2020 - Diciembre 2024</p>
    
    <p><strong>Certificación SAP</strong><br/>
    Universidad Panamericana, Zapopan, Jal.<br/>
    Agosto 2023 - Diciembre 2023</p>
    
    <p><strong>Certificate III in Business</strong><br/>
    Lonsdale Institute, Melbourne, Aus.<br/>
    Sep 2019 - Feb 2020</p>
    </div>
    """, unsafe_allow_html=True)

    # Idiomas
    st.markdown("""
    <h2 style='margin-bottom: 5px;'>Idiomas</h2>
    <div style='margin-top: -20px;'>
    <ul>
        <li>Español - Nativo</li>
        <li>Inglés - Avanzado</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Puedes continuar con la segunda columna o añadir más secciones según lo necesites




