"""
Aplicación Streamlit INTERACTIVA para el Sistema Experto de Absentismo Escolar
Modo: Preguntas progresivas según respuestas anteriores
Autor: César Domínguez Notario
"""

import streamlit as st
from sistema_experto import valorar_caso

st.set_page_config(
    page_title="Sistema Experto - Absentismo Escolar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de sesión
if 'paso' not in st.session_state:
    st.session_state.paso = 1
if 'datos' not in st.session_state:
    st.session_state.datos = {}

st.title("Sistema Experto de Absentismo Escolar")
st.markdown("""
**Sistema de apoyo a la decisión inicial ante casos de absentismo escolar en adolescentes**

Este sistema te guiará paso a paso para valorar el caso.
""")

with st.sidebar:
    st.header("Información del Sistema")
    st.markdown("""
    **Alcance:**
    - Valoración inicial de casos
    - Recomendación de protocolo
    - Apoyo a la decisión profesional
    
    **Modo:** Interactivo progresivo
    
    **Autor:** César Domínguez Notario  
    **Módulo:** Modelos de IA  
    **Curso:** 2025-2026
    """)
    
    if st.session_state.paso > 1:
        st.divider()
        st.subheader("Datos introducidos:")
        for key, value in st.session_state.datos.items():
            st.text(f"{key}: {value}")
    
    if st.button("Reiniciar"):
        st.session_state.paso = 1
        st.session_state.datos = {}
        st.rerun()

st.divider()

# PASO 1: Intervención previa del centro
if st.session_state.paso == 1:
    st.header("Paso 1: Verificación inicial")
    st.markdown("### ¿El centro educativo ha realizado intervención previa?")
    st.info("El protocolo requiere que el centro haya intervenido antes de activar servicios sociales")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sí", use_container_width=True, type="primary"):
            st.session_state.datos['intervencion_previa_centro'] = 'si'
            st.session_state.paso = 2
            st.rerun()
    with col2:
        if st.button("No", use_container_width=True):
            st.session_state.datos['intervencion_previa_centro'] = 'no'
            st.session_state.paso = 99  # Saltar a resultado
            st.rerun()

# PASO 2: Estado de la información
elif st.session_state.paso == 2:
    st.header("Paso 2: Calidad de la información")
    st.markdown("### ¿Cómo es la información disponible?")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Completa", use_container_width=True, type="primary"):
            st.session_state.datos['estado_informacion'] = 'completa'
            st.session_state.paso = 3
            st.rerun()
    with col2:
        if st.button("Incompleta", use_container_width=True):
            st.session_state.datos['estado_informacion'] = 'incompleta'
            st.session_state.paso = 99
            st.rerun()
    with col3:
        if st.button("Contradictoria", use_container_width=True):
            st.session_state.datos['estado_informacion'] = 'contradictoria'
            st.session_state.paso = 99
            st.rerun()

# PASO 3: Situación personal
elif st.session_state.paso == 3:
    st.header("Paso 3: Situación personal del menor")
    st.markdown("### ¿Presenta alguna de estas situaciones?")
    
    opciones = {
        'sin_indicadores': 'Sin indicadores especiales',
        'salud_mental_grave': 'Salud mental grave',
        'psicopatologia': 'Psicopatología',
        'consumo_sustancias': 'Consumo de sustancias',
        'conducta_disruptiva': 'Conducta disruptiva'
    }
    
    for key, label in opciones.items():
        if st.button(label, use_container_width=True, type="primary" if key == 'sin_indicadores' else "secondary"):
            st.session_state.datos['situacion_personal'] = key
            if key in ['salud_mental_grave', 'psicopatologia', 'consumo_sustancias']:
                st.session_state.paso = 99  # Requiere revisión manual
            else:
                st.session_state.paso = 4
            st.rerun()

# PASO 4: Desprotección
elif st.session_state.paso == 4:
    st.header("Paso 4: Indicadores de desprotección")
    st.markdown("### ¿Se detectan indicadores de desprotección del menor?")
    st.warning("Situación en la que no están cubiertas las necesidades básicas del menor")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("No", use_container_width=True, type="primary"):
            st.session_state.datos['desproteccion'] = 'no'
            st.session_state.paso = 5
            st.rerun()
    with col2:
        if st.button("Sí", use_container_width=True):
            st.session_state.datos['desproteccion'] = 'si'
            st.session_state.paso = 99  # Intervención urgente
            st.rerun()

# PASO 5: Intensidad del absentismo
elif st.session_state.paso == 5:
    st.header("Paso 5: Intensidad del absentismo")
    st.markdown("### ¿Cuál es la intensidad de las faltas?")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Baja", "~25%")
        if st.button("Seleccionar Baja", use_container_width=True):
            st.session_state.datos['intensidad_absentismo'] = 'baja'
            st.session_state.paso = 6
            st.rerun()
    with col2:
        st.metric("Media", "~50%")
        if st.button("Seleccionar Media", use_container_width=True, type="primary"):
            st.session_state.datos['intensidad_absentismo'] = 'media'
            st.session_state.paso = 6
            st.rerun()
    with col3:
        st.metric("Alta", "~75%")
        if st.button("Seleccionar Alta", use_container_width=True):
            st.session_state.datos['intensidad_absentismo'] = 'alta'
            st.session_state.paso = 6
            st.rerun()

# PASO 6: SISO
elif st.session_state.paso == 6:
    st.header("Paso 6: Vulnerabilidad social (SISO)")
    st.markdown("### Puntuación SISO del caso")
    st.info("Herramienta de valoración social (0-100). Umbral crítico: 58 puntos")
    
    siso = st.slider(
        "Selecciona la puntuación SISO:",
        min_value=0,
        max_value=100,
        value=50,
        help="Valores > 58 indican vulnerabilidad elevada"
    )
    
    if st.button("Continuar", type="primary", use_container_width=True):
        st.session_state.datos['siso'] = siso
        st.session_state.paso = 7
        st.rerun()

# PASO 7: Colaboración familiar
elif st.session_state.paso == 7:
    st.header("Paso 7: Colaboración familiar")
    st.markdown("### ¿Cuál es el nivel de colaboración de la familia?")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Nula", use_container_width=True):
            st.session_state.datos['colaboracion_familiar'] = 'nula'
            st.session_state.paso = 8
            st.rerun()
    with col2:
        if st.button("Baja", use_container_width=True):
            st.session_state.datos['colaboracion_familiar'] = 'baja'
            st.session_state.paso = 8
            st.rerun()
    with col3:
        if st.button("Media", use_container_width=True, type="primary"):
            st.session_state.datos['colaboracion_familiar'] = 'media'
            st.session_state.paso = 8
            st.rerun()
    with col4:
        if st.button("Alta", use_container_width=True):
            st.session_state.datos['colaboracion_familiar'] = 'alta'
            st.session_state.paso = 8
            st.rerun()

# PASO 8: Antecedentes
elif st.session_state.paso == 8:
    st.header("Paso 8: Antecedentes")
    st.markdown("### ¿Existen antecedentes de absentismo en este menor?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("No", use_container_width=True, type="primary"):
            st.session_state.datos['antecedentes'] = 'no'
            st.session_state.paso = 99
            st.rerun()
    with col2:
        if st.button("Sí", use_container_width=True):
            st.session_state.datos['antecedentes'] = 'si'
            st.session_state.paso = 99
            st.rerun()

# PASO 99: Resultado
elif st.session_state.paso == 99:
    # Completar datos faltantes con valores por defecto
    defaults = {
        'intervencion_previa_centro': 'si',
        'estado_informacion': 'completa',
        'situacion_personal': 'sin_indicadores',
        'desproteccion': 'no',
        'intensidad_absentismo': 'media',
        'siso': 50,
        'colaboracion_familiar': 'media',
        'antecedentes': 'no'
    }
    
    for key, default in defaults.items():
        if key not in st.session_state.datos:
            st.session_state.datos[key] = default
    
    # Ejecutar sistema experto
    with st.spinner("Analizando caso..."):
        resultado = valorar_caso(**st.session_state.datos)
    
    st.success("Análisis completado")
    
    st.header("Resultados del Análisis")
    
    col_res1, col_res2 = st.columns(2)
    
    with col_res1:
        st.metric(
            label="Nivel de Riesgo",
            value=resultado['nivel_riesgo']
        )
    
    with col_res2:
        st.metric(
            label="Recomendación Inicial",
            value=resultado['recomendacion']
        )
    
    st.subheader("Explicación del Sistema Experto")
    
    for linea in resultado['explicacion']:
        if 'ALERTA' in linea or 'CASO COMPLEJO' in linea:
            st.error(linea)
        elif 'RECOMENDACIÓN' in linea:
            st.info(linea)
        elif 'RIESGO' in linea:
            st.warning(linea)
        else:
            st.write(linea)
    
    if resultado['factores_activados']:
        st.subheader("Factores Activados en el Análisis")
        cols = st.columns(min(len(resultado['factores_activados']), 3))
        for idx, factor in enumerate(resultado['factores_activados']):
            with cols[idx % 3]:
                st.info(factor)
    
    st.divider()
    
    st.warning("""
    **IMPORTANTE**: Este sistema es una herramienta de apoyo a la decisión. 
    La valoración final y la toma de decisiones debe realizarse siempre por un 
    profesional cualificado del ámbito socioeducativo.
    """)
    
    if st.button("Analizar otro caso", type="primary", use_container_width=True):
        st.session_state.paso = 1
        st.session_state.datos = {}
        st.rerun()

st.divider()
st.caption("Sistema Experto de Absentismo Escolar | IES Maestre de Calatrava | 2026")
