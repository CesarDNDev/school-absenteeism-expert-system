# 🎓 Sistema Experto de Absentismo Escolar

Sistema experto orientado a apoyar la decisión inicial ante casos de absentismo escolar en adolescentes.

## 📋 Descripción

Sistema experto basado en reglas de producción que apoya la toma de decisiones iniciales en casos de absentismo escolar. Utiliza un motor de inferencia (Experta) para analizar múltiples indicadores y recomendar protocolos de actuación coherentes con criterios profesionales establecidos.

## 🎯 Objetivos

- Identificar el nivel inicial de riesgo asociado al absentismo
- Proponer actuación socioeducativa inicial coherente
- Facilitar la derivación al protocolo correspondiente
- Servir como apoyo explicable para el profesional responsable

## 🔧 Tecnologías

- **Python 3.8+**
- **Experta 1.9.4** - Motor de inferencia basado en reglas
- **Streamlit 1.31.0** - Interfaz web interactiva

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/CesarDNDev/school-absenteeism-expert-system.git
cd school-absenteeism-expert-system

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🚀 Uso

### Ejecutar la aplicación Streamlit

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

### Usar el motor de inferencia directamente

```python
from sistema_experto import valorar_caso

resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=65,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)

print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
```

## 📊 Indicadores del Sistema

### Entrada
- **Intervención previa del centro**: Sí/No
- **Intensidad del absentismo**: Baja (25%) / Media (50%) / Alta (75%)
- **Puntuación SISO**: 0-100 (vulnerabilidad social)
- **Colaboración familiar**: Alta / Media / Baja / Nula
- **Antecedentes**: Sí/No
- **Desprotección**: Sí/No
- **Situación personal**: Sin indicadores / Conducta disruptiva / Salud mental grave / Psicopatología / Consumo
- **Estado de información**: Completa / Incompleta / Contradictoria

### Salida
- **Nivel de riesgo**: Bajo / Medio / Alto / Preventivo / No valorable
- **Recomendación inicial**: 
  - Seguimiento
  - Intervención ETI (preventiva)
  - Intervención ETI
  - Equipo de familia
  - Derivación
  - Ampliar información
  - Revisión manual obligatoria

## 🧠 Base de Conocimiento

El sistema implementa **12+ reglas de producción** extraídas de entrevistas con expertos:

### Reglas principales
1. Verificación de intervención previa del centro
2. Detección de desprotección (prioridad máxima)
3. Casos que requieren revisión manual (salud mental, consumo)
4. Información incompleta o contradictoria
5. Seguimiento (riesgo bajo)
6. Intervención preventiva (vulnerabilidad alta, pocas faltas)
7. Intervención ETI especializada (SISO > 58)
8. No cooperación familiar (riesgo de derivación)
9. Equipo de familia (vulnerabilidad moderada)

### Umbrales clave
- **SISO > 58**: Umbral para intervención especializada
- **Intensidad baja**: ~25% faltas injustificadas
- **Intensidad media**: ~50% faltas injustificadas
- **Intensidad alta**: ~75% faltas injustificadas

## 🔍 Alcance y Límites

### Alcance
✅ Valoración inicial de casos  
✅ Clasificación según criterios predefinidos  
✅ Recomendación de protocolo inicial  
✅ Explicación de la decisión  

### Límites
❌ No sustituye valoración profesional final  
❌ No realiza diagnóstico clínico/psicológico  
❌ No decide sanciones administrativas  
❌ Requiere supervisión humana obligatoria  

## 📚 Documentación

- **Adquisición del conocimiento**: Ver documento `AdquisiciónConceptualización_CESAR_DOMÍNGUEZ_NOTARIO.docx (1).txt`
- **Entrevistas con expertos**: 3 sesiones estructuradas
- **Fuente experta**: María José Notario Asensio (Educadora Social, Ayuntamiento de Ciudad Real)

## 🎓 Contexto Académico

**Autor:** César Domínguez Notario  
**Curso:** Especialización en Inteligencia Artificial y Big Data  
**Módulo:** Modelos de Inteligencia Artificial  
**Centro:** IES Maestre de Calatrava  
**Fecha:** Abril 2026  

## 📄 Licencia

Este proyecto es un trabajo académico desarrollado para el módulo de Modelos de IA.

## 🤝 Agradecimientos

- María José Notario Asensio - Experta en el dominio
- IES Maestre de Calatrava
- Ayuntamiento de Ciudad Real

---

**⚠️ IMPORTANTE**: Este sistema es una herramienta de apoyo a la decisión. La valoración final debe ser realizada siempre por un profesional cualificado del ámbito socioeducativo.
