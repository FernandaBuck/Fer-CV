import streamlit as st

# Personalización de estilos CSS
st.markdown(
    """
    <style>
    .main {
        font-family: "Arial", sans-serif;
    }
    .header-title {
        font-size: 48px;
        font-weight: bold;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color: #2E4053;
    }
    .text {
        font-size: 16px;
        line-height: 1.6;
    }
    .bold-text {
        font-weight: bold;
    }
    .section {
        margin-top: 40px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Título del CV
st.markdown('<h1 class="header-title">Fernanda Buck</h1>', unsafe_allow_html=True)

# Dividir en dos columnas
col1, col2 = st.columns([1, 2])

# Columna 1: Foto
with col1:
    st.image("BUCK.png", caption="Fernanda Buck", width=150)

# Columna 2: Información personal
with col2:
    st.markdown('<div class="subheader">Información Personal</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="text">
    <li><span class="bold-text">Nombre:</span> ESTUDIANTE DE ADMINITRACIÓN Y FINANZAS/li>
    <li><span class="bold-text">Nombre:</span> María Fernanda Buck Nuñez</li>
    <li><span class="bold-text">Correo Electrónico:</span> fernandabuckn@outlook.com</li>
    <li><span class="bold-text">Teléfono:</span> 477 648 7258</li>
    </ul>
    """, unsafe_allow_html=True)

# Resumen profesional
st.markdown('<div class="section subheader">Resumen Profesional</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
Actualmente, me encuentro en el octavo semestre de la carrera de Administración y Finanzas en la Universidad Panamericana, campus Guadalajara. Soy una persona altamente organizada y proactiva, siempre comprometida a dar lo mejor de mí en todas mis actividades. Disfruto trabajar en equipo y considero que la colaboración es clave para alcanzar metas exitosas. Estoy en búsqueda de desafíos profesionales que me permitan crecer y superarme.
</div>
""", unsafe_allow_html=True)

# Experiencia profesional
st.markdown('<div class="section subheader">Experiencia Profesional</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
### Intern en Contabilidad y Administración<br>
**Wilson Abogados S.C - Abril 2021 - Agosto 2022**<br>
- Apoyo en registro contable y administrativo de operaciones propias del despacho y de clientes externos.
- Apoyo en el desarrollo de modelos de análisis propios y para clientes.
- Contabilidad y Finanzas.

### Presidente del Comité de Administración y Finanzas<br>
**Universidad Panamericana - Enero - Diciembre 2023**<br>
- Coordinación de un equipo de 20 estudiantes para llevar a cabo actividades para más de 600 estudiantes.
- Organización de eventos, gestión de relaciones públicas y análisis de estados financieros para la toma de decisiones estratégicas.

### Área de Operaciones<br>
**Inmobiliaria Magnum - Enero 2020 - 2023**<br>
- Atención al cliente y captación de nuevos prospectos.
- Seguimiento y cierre de operaciones internas.
- Análisis de información financiera y control administrativo para la toma de decisiones.
</div>
""", unsafe_allow_html=True)

# Educación
st.markdown('<div class="section subheader">Educación</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
**Licenciatura en Administración y Finanzas**<br>
Universidad Panamericana - Campus Guadalajara - Agosto 2020 - Diciembre 2024

### Otros cursos y certificaciones
- Certificación SAP - Universidad Panamericana - Agosto 2023 - Diciembre 2023
</div>
""", unsafe_allow_html=True)

# Habilidades
st.markdown('<div class="section subheader">Habilidades</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
- Toma de Desiciones
- Trabajo en Equipo
- Solución de Problemas
- Liderazgo
</div>
""", unsafe_allow_html=True)

# Idiomas
st.markdown('<div class="section subheader">Idiomas</div>', unsafe_allow_html=True)
st.markdown("""
<div class="text">
- Español - Nativo
- Inglés - Avanzado
</div>
""", unsafe_allow_html=True)

