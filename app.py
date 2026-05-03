"""
Aplicación Streamlit para el Sistema Experto de Absentismo Escolar
Autor: César Domínguez Notario
"""

import streamlit as st
from sistema_experto import valorar_caso

st.set_page_config(
    page_title="Sistema Experto - Absentismo Escolar",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Sistema Experto de Absentismo Escolar")
st.markdown("""
**Sistema de apoyo a la decisión inicial ante casos de absentismo escolar en adolescentes**

Este sistema experto está basado en reglas extraídas de entrevistas con profesionales 
del ámbito socioeducativo y utiliza un motor de inferencia para recomendar actuaciones iniciales.
""")

st.divider()

with st.sidebar:
    st.header("Información del Sistema")
    st.markdown("""
    **Alcance:**
    - Valoración inicial de casos
    - Recomendación de protocolo
    - Apoyo a la decisión profesional
    
    **Limitaciones:**
    - No sustituye valoración profesional
    - No realiza diagnóstico clínico
    - Requiere supervisión humana
    
    **Autor:** César Domínguez Notario  
    **Módulo:** Modelos de IA  
    **Curso:** 2025-2026
    """)
    
    st.divider()
    
    with st.expander("Glosario de términos"):
        st.markdown("""
        **SISO:** Herramienta de valoración social (0-100)  
        **ETI:** Equipo Técnico de Inclusión  
        **Intensidad baja:** ~25% faltas injustificadas  
        **Intensidad media:** ~50% faltas injustificadas  
        **Intensidad alta:** ~75% faltas injustificadas
        """)

st.header("Datos del Caso")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Información del Centro Educativo")
    
    intervencion_previa = st.radio(
        "¿El centro educativo ha realizado intervención previa?",
        options=['si', 'no'],
        format_func=lambda x: 'Sí' if x == 'si' else 'No',
        help="El protocolo requiere que el centro haya intervenido antes de activar servicios sociales"
    )
    
    intensidad = st.select_slider(
        "Intensidad del absentismo",
        options=['baja', 'media', 'alta'],
        value='media',
        help="Baja: ~25% faltas | Media: ~50% faltas | Alta: ~75% faltas"
    )
    
    estado_info = st.selectbox(
        "Estado de la información disponible",
        options=['completa', 'incompleta', 'contradictoria'],
        help="Evalúa la calidad y coherencia de los datos disponibles"
    )

with col2:
    st.subheader("Contexto Familiar y Social")
    
    siso = st.slider(
        "Puntuación SISO (vulnerabilidad social)",
        min_value=0,
        max_value=100,
        value=50,
        help="Herramienta de valoración social. Umbral crítico: 58 puntos"
    )
    
    colaboracion = st.select_slider(
        "Nivel de colaboración familiar",
        options=['nula', 'baja', 'media', 'alta'],
        value='media',
        help="Grado de cooperación de la familia con el centro y servicios sociales"
    )
    
    antecedentes = st.radio(
        "¿Existen antecedentes de absentismo?",
        options=['no', 'si'],
        format_func=lambda x: 'Sí' if x == 'si' else 'No',
        help="Casos previos de absentismo en el mismo menor"
    )

st.subheader("Indicadores Adicionales")

col3, col4 = st.columns(2)

with col3:
    desproteccion = st.radio(
        "¿Se detectan indicadores de desprotección del menor?",
        options=['no', 'si'],
        format_func=lambda x: 'Sí' if x == 'si' else 'No',
        help="Situación en la que no están cubiertas las necesidades básicas del menor"
    )

with col4:
    situacion_personal = st.selectbox(
        "Situación personal del menor",
        options=[
            'sin_indicadores',
            'conducta_disruptiva',
            'salud_mental_grave',
            'psicopatologia',
            'consumo_sustancias'
        ],
        format_func=lambda x: {
            'sin_indicadores': 'Sin indicadores especiales',
            'conducta_disruptiva': 'Conducta disruptiva',
            'salud_mental_grave': 'Salud mental grave',
            'psicopatologia': 'Psicopatología',
            'consumo_sustancias': 'Consumo de sustancias'
        }[x],
        help="Indicadores que pueden requerir valoración especializada"
    )

st.divider()

if st.button("Analizar Caso", type="primary", use_container_width=True):
    with st.spinner("Ejecutando motor de inferencia..."):
        resultado = valorar_caso(
            intervencion_previa_centro=intervencion_previa,
            intensidad_absentismo=intensidad,
            siso=siso,
            colaboracion_familiar=colaboracion,
            antecedentes=antecedentes,
            desproteccion=desproteccion,
            situacion_personal=situacion_personal,
            estado_informacion=estado_info
        )
    
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
    
    for i, linea in enumerate(resultado['explicacion'], 1):
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
    
    with st.expander("Ver datos del caso introducidos"):
        st.json({
            "Intervención previa centro": intervencion_previa,
            "Intensidad absentismo": intensidad,
            "Puntuación SISO": siso,
            "Colaboración familiar": colaboracion,
            "Antecedentes": antecedentes,
            "Desprotección": desproteccion,
            "Situación personal": situacion_personal,
            "Estado información": estado_info
        })

st.divider()

with st.expander("Acerca del sistema"):
    st.markdown("""
    ### Sistema Experto de Absentismo Escolar
    
    **Desarrollo:** César Domínguez Notario  
    **Curso:** Especialización en Inteligencia Artificial y Big Data  
    **Módulo:** Modelos de Inteligencia Artificial  
    **Fecha:** Abril 2026
    
    **Tecnologías utilizadas:**
    - Motor de inferencia: Experta (Python)
    - Interfaz: Streamlit
    - Basado en: Entrevistas con expertos del ámbito socioeducativo
    
    **Fuente de conocimiento:**
    - María José Notario Asensio (Educadora Social, Ayuntamiento de Ciudad Real)
    - Protocolo de absentismo escolar
    - Herramienta SISO de valoración social
    
    **Reglas implementadas:** 12+ reglas de producción  
    **Casos contemplados:** Seguimiento, Prevención, Intervención ETI, Equipo de Familia, Derivación, Revisión Manual
    """)

st.markdown("---")
st.caption("Sistema Experto de Absentismo Escolar | IES Maestre de Calatrava | 2026")
