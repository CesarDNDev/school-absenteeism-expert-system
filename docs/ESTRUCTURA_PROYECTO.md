# 📁 Estructura del Proyecto

```
school-absenteeism-expert-system/
│
├── 📄 app.py                          # Interfaz Streamlit (aplicación web)
├── 🧠 sistema_experto.py              # Motor de inferencia con Experta
├── 🧪 casos_prueba.py                 # 10 casos de prueba para validación
│
├── 📋 requirements.txt                # Dependencias del proyecto
├── 📖 README.md                       # Documentación principal
├── 🚀 DEPLOYMENT.md                   # Guía de despliegue en Streamlit Cloud
├── 🗂️ .gitignore                      # Archivos ignorados por Git
│
└── 📚 AdquisiciónConceptualización... # Documento de análisis del conocimiento
```

## 🔍 Descripción de archivos

### Archivos principales

#### `app.py` (7.7 KB)
Aplicación web con Streamlit que proporciona:
- Formulario interactivo para introducir datos del caso
- Visualización de resultados del análisis
- Explicaciones detalladas de las recomendaciones
- Interfaz amigable para profesionales

#### `sistema_experto.py` (9.7 KB)
Motor de inferencia basado en Experta que contiene:
- Clase `SistemaAbsentismoEscolar` (KnowledgeEngine)
- 12+ reglas de producción
- Función `valorar_caso()` para análisis
- Lógica de razonamiento basada en hechos

#### `casos_prueba.py` (6.5 KB)
Script de validación con 10 casos de prueba:
1. Seguimiento simple
2. Intervención ETI especializada
3. Revisión manual (salud mental)
4. Sin intervención previa
5. Desprotección detectada
6. Intervención preventiva
7. No cooperación familiar
8. Equipo de familia
9. Información contradictoria
10. Consumo de sustancias

### Archivos de configuración

#### `requirements.txt`
```
streamlit==1.31.0
experta==1.9.4
```

#### `.gitignore`
Ignora archivos temporales, cache de Python, entornos virtuales, etc.

### Documentación

#### `README.md`
Documentación completa del proyecto con:
- Descripción y objetivos
- Instrucciones de instalación
- Guía de uso
- Especificación de indicadores
- Base de conocimiento
- Contexto académico

#### `DEPLOYMENT.md`
Guía paso a paso para desplegar en Streamlit Cloud

## 🔄 Flujo de ejecución

```
Usuario → app.py → sistema_experto.py → Reglas de inferencia → Resultado
                                              ↓
                                    Base de conocimiento
                                    (12+ reglas extraídas
                                     de entrevistas)
```

## 🧠 Reglas implementadas

1. ✅ Verificación intervención previa centro
2. ✅ Casos con salud mental grave → Revisión manual
3. ✅ Información contradictoria → Ampliar información
4. ✅ Información incompleta → Ampliar información
5. ✅ Desprotección detectada → Intervención urgente ETI
6. ✅ Seguimiento (riesgo bajo)
7. ✅ Intervención preventiva (SISO > 58, pocas faltas)
8. ✅ Intervención ETI especializada (SISO > 58, absentismo consolidado)
9. ✅ No cooperación familiar → Riesgo alto
10. ✅ Equipo de familia (SISO ≤ 58, familia colabora)

## 📊 Métricas del código

- **Líneas de código total**: ~500 líneas
- **Reglas de producción**: 12+
- **Casos de prueba**: 10
- **Archivos Python**: 3
- **Dependencias externas**: 2

## 🎯 Próximos pasos

1. ✅ Código implementado
2. ✅ Casos de prueba creados
3. ✅ Documentación completa
4. 🔄 **Desplegar en Streamlit Cloud** (siguiente paso)
5. ⏳ Validación con casos reales
6. ⏳ Mejoras basadas en feedback

---

**Estado del proyecto**: ✅ Listo para desplegar
