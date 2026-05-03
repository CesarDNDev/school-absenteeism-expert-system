# Implementación del Sistema Experto con CLIPS

## Ampliación de la Tarea 5.2 - Reglas diseñadas para CLIPS

### Tecnología utilizada

**Motor de inferencia:** CLIPS (C Language Integrated Production System)  
**Librería Python:** clipspy 1.0.3  
**Paradigma:** Sistema basado en reglas de producción (forward-chaining)

---

## Estructura del sistema CLIPS

### Templates (Plantillas de hechos)

```clips
(deftemplate caso
    (slot intervencion-previa-centro (type SYMBOL))
    (slot intensidad-absentismo (type SYMBOL))
    (slot siso (type INTEGER))
    (slot colaboracion-familiar (type SYMBOL))
    (slot antecedentes (type SYMBOL))
    (slot desproteccion (type SYMBOL))
    (slot situacion-personal (type SYMBOL))
    (slot estado-informacion (type SYMBOL))
)

(deftemplate resultado
    (slot recomendacion (type STRING))
    (slot nivel-riesgo (type STRING))
)
```

---

## Reglas de producción implementadas

### REGLA 1: Verificación de intervención previa

```clips
(defrule sin-intervencion-previa
    (caso (intervencion-previa-centro no))
    =>
    (assert (resultado 
        (recomendacion "Ampliar información")
        (nivel-riesgo "No valorable")))
    (assert (explicacion "El centro educativo NO ha realizado intervención previa"))
    (assert (factor "Sin intervención previa del centro"))
)
```

**Descripción:** Si el centro educativo no ha intervenido previamente, se solicita que realice actuación inicial antes de activar el protocolo de servicios sociales.

---

### REGLA 2: Casos que requieren revisión manual

```clips
(defrule revision-manual-salud-mental
    (caso (intervencion-previa-centro si)
          (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias))
    =>
    (assert (resultado 
        (recomendacion "Revisión manual obligatoria")
        (nivel-riesgo "Requiere valoración especializada")))
    (assert (explicacion "CASO COMPLEJO: Requiere valoración especializada"))
    (assert (factor "Situación personal compleja"))
)
```

**Descripción:** Casos con salud mental grave, psicopatología o consumo de sustancias quedan fuera del sistema automático y requieren valoración manual por profesionales especializados.

---

### REGLA 3: Información contradictoria

```clips
(defrule informacion-contradictoria
    (caso (intervencion-previa-centro si)
          (estado-informacion contradictoria))
    =>
    (assert (resultado 
        (recomendacion "Ampliar información")
        (nivel-riesgo "No valorable")))
    (assert (explicacion "La información disponible es CONTRADICTORIA"))
    (assert (factor "Información contradictoria"))
)
```

**Descripción:** Cuando hay datos contradictorios entre fuentes (centro, familia, menor), se debe contactar con el equipo de atención primaria para contrastar información antes de clasificar el caso.

---

### REGLA 4: Información incompleta

```clips
(defrule informacion-incompleta
    (caso (intervencion-previa-centro si)
          (estado-informacion incompleta))
    =>
    (assert (resultado 
        (recomendacion "Ampliar información")
        (nivel-riesgo "No valorable")))
    (assert (explicacion "La información disponible es INCOMPLETA"))
    (assert (factor "Información incompleta"))
)
```

**Descripción:** Si faltan datos esenciales, se solicitan datos adicionales al centro educativo y/o familia antes de proceder con la valoración.

---

### REGLA 5: Desprotección del menor (MÁXIMA PRIORIDAD)

```clips
(defrule desproteccion-detectada
    (declare (salience 100))
    (caso (intervencion-previa-centro si)
          (desproteccion si)
          (estado-informacion completa))
    (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
    =>
    (assert (resultado 
        (recomendacion "Intervención ETI urgente")
        (nivel-riesgo "Alto - Desprotección")))
    (assert (explicacion "ALERTA: INDICADORES DE DESPROTECCIÓN del menor"))
    (assert (factor "Desprotección del menor"))
)
```

**Descripción:** Cuando se detectan indicadores de desprotección, el nivel de riesgo se eleva inmediatamente y se activa intervención urgente del ETI. Esta regla tiene máxima prioridad (salience 100) sobre todas las demás.

---

### REGLA 6: Seguimiento (Riesgo bajo)

```clips
(defrule seguimiento-simple
    (caso (intervencion-previa-centro si)
          (intensidad-absentismo baja)
          (colaboracion-familiar alta|media)
          (antecedentes no)
          (desproteccion no)
          (estado-informacion completa))
    =>
    (assert (resultado 
        (recomendacion "Seguimiento")
        (nivel-riesgo "Bajo")))
    (assert (explicacion "Caso de RIESGO BAJO: Faltas esporádicas"))
    (assert (factor "Intensidad baja"))
)
```

**Descripción:** Casos con faltas esporádicas, familia colaboradora y sin antecedentes se clasifican como riesgo bajo. Se mantiene seguimiento ordinario desde el centro educativo sin intervención especializada.

---

### REGLA 7: Intervención preventiva

```clips
(defrule prevencion-vulnerabilidad-alta
    (caso (intervencion-previa-centro si)
          (intensidad-absentismo baja)
          (siso ?s&:(> ?s 58))
          (desproteccion no)
          (estado-informacion completa))
    =>
    (assert (resultado 
        (recomendacion "Intervención ETI (preventiva)")
        (nivel-riesgo "Preventivo - Vulnerabilidad alta")))
    (assert (explicacion "VULNERABILIDAD SOCIAL ELEVADA (SISO > 58)"))
    (assert (factor "Vulnerabilidad SISO > 58"))
)
```

**Descripción:** Aunque las faltas sean pocas, si existe vulnerabilidad social elevada (SISO > 58) se recomienda intervención preventiva del ETI para evitar desprotección futura.

---

### REGLA 8: Intervención ETI especializada

```clips
(defrule intervencion-eti-especializada
    (caso (intervencion-previa-centro si)
          (intensidad-absentismo media|alta)
          (siso ?s&:(> ?s 58))
          (desproteccion no)
          (estado-informacion completa))
    =>
    (assert (resultado 
        (recomendacion "Intervención ETI")
        (nivel-riesgo "Medio-Alto")))
    (assert (explicacion "Absentismo consolidado + Vulnerabilidad elevada"))
    (assert (factor "Absentismo consolidado"))
)
```

**Descripción:** Cuando se combina absentismo consolidado (medio o alto) con vulnerabilidad social elevada (SISO > 58), se activa intervención especializada del Equipo Técnico de Inclusión.

---

### REGLA 9: No cooperación familiar

```clips
(defrule no-cooperacion-familiar
    (caso (intervencion-previa-centro si)
          (intensidad-absentismo media|alta)
          (siso ?s&:(<= ?s 58))
          (colaboracion-familiar baja|nula)
          (desproteccion no)
          (estado-informacion completa))
    =>
    (assert (resultado 
        (recomendacion "Intervención ETI con valoración de derivación")
        (nivel-riesgo "Alto - No cooperación familiar")))
    (assert (explicacion "NO COOPERACIÓN FAMILIAR"))
    (assert (factor "Riesgo de derivación judicial"))
)
```

**Descripción:** Absentismo consolidado con familia que no coopera se clasifica como riesgo alto. Se interviene desde ETI y, si persisten las faltas tras 3-6 meses, se valora derivación a Fiscalía de Menores.

---

### REGLA 10: Equipo de familia

```clips
(defrule equipo-familia
    (caso (intervencion-previa-centro si)
          (intensidad-absentismo media|alta)
          (siso ?s&:(<= ?s 58))
          (colaboracion-familiar alta|media)
          (desproteccion no)
          (estado-informacion completa))
    =>
    (assert (resultado 
        (recomendacion "Equipo de familia")
        (nivel-riesgo "Medio")))
    (assert (explicacion "Vulnerabilidad moderada (SISO <= 58)"))
    (assert (factor "Familia colaboradora"))
)
```

**Descripción:** Absentismo consolidado con vulnerabilidad moderada (SISO ≤ 58) y familia colaboradora se deriva a Equipo de Familia para intervención ordinaria, sin necesidad de ETI.

---

## Mecanismo de inferencia

### Forward-chaining
El motor CLIPS evalúa todas las reglas en cada ciclo y ejecuta aquellas cuyas condiciones se cumplen.

### Salience (prioridad)
- **Regla de desprotección:** salience 100 (máxima prioridad)
- **Resto de reglas:** salience por defecto (0)

### Resolución de conflictos
Cuando múltiples reglas son aplicables, CLIPS usa:
1. Salience (prioridad declarada)
2. Especificidad (reglas más específicas primero)
3. Orden de activación (LIFO por defecto)

---

## Umbrales y criterios clave

| Criterio | Valor | Fuente |
|----------|-------|--------|
| **SISO crítico** | > 58 puntos | Entrevista Nº2 y Nº3 |
| **Intensidad baja** | ~25% faltas injustificadas | Entrevista Nº1 |
| **Intensidad media** | ~50% faltas injustificadas | Entrevista Nº1 |
| **Intensidad alta** | ~75% faltas injustificadas | Entrevista Nº1 |
| **Tiempo intervención** | 3-6 meses antes de derivar | Entrevista Nº2 |

---

## Validación del sistema

El sistema ha sido validado con **10 casos de prueba** que cubren:
- ✅ Todos los niveles de riesgo
- ✅ Todas las recomendaciones posibles
- ✅ Casos límite (umbrales)
- ✅ Excepciones (revisión manual)
- ✅ Información incompleta/contradictoria

Ver archivo `casos_prueba.py` para detalles.

---

## Resumen de reglas implementadas

### REGLA 1: Verificación de intervención previa
Si el centro educativo no ha intervenido previamente, se solicita que realice actuación inicial antes de activar el protocolo de servicios sociales.

### REGLA 2: Casos que requieren revisión manual
Casos con salud mental grave, psicopatología o consumo de sustancias quedan fuera del sistema automático y requieren valoración manual por profesionales especializados.

### REGLA 3: Información contradictoria
Cuando hay datos contradictorios entre fuentes (centro, familia, menor), se debe contactar con el equipo de atención primaria para contrastar información antes de clasificar el caso.

### REGLA 4: Información incompleta
Si faltan datos esenciales, se solicitan datos adicionales al centro educativo y/o familia antes de proceder con la valoración.

### REGLA 5: Desprotección del menor (MÁXIMA PRIORIDAD)
Cuando se detectan indicadores de desprotección, el nivel de riesgo se eleva inmediatamente y se activa intervención urgente del ETI. Esta regla tiene máxima prioridad (salience 100) sobre todas las demás.

### REGLA 6: Seguimiento (Riesgo bajo)
Casos con faltas esporádicas, familia colaboradora y sin antecedentes se clasifican como riesgo bajo. Se mantiene seguimiento ordinario desde el centro educativo sin intervención especializada.

### REGLA 7: Intervención preventiva
Aunque las faltas sean pocas, si existe vulnerabilidad social elevada (SISO > 58) se recomienda intervención preventiva del ETI para evitar desprotección futura.

### REGLA 8: Intervención ETI especializada
Cuando se combina absentismo consolidado (medio o alto) con vulnerabilidad social elevada (SISO > 58), se activa intervención especializada del Equipo Técnico de Inclusión.

### REGLA 9: No cooperación familiar
Absentismo consolidado con familia que no coopera se clasifica como riesgo alto. Se interviene desde ETI y, si persisten las faltas tras 3-6 meses, se valora derivación a Fiscalía de Menores.

### REGLA 10: Equipo de familia
Absentismo consolidado con vulnerabilidad moderada (SISO ≤ 58) y familia colaboradora se deriva a Equipo de Familia para intervención ordinaria, sin necesidad de ETI.

---

## Conclusión

La implementación en CLIPS permite:
- ✅ **Explicabilidad:** Cada decisión se justifica con las reglas activadas
- ✅ **Trazabilidad:** Se registran los factores que influyen en la recomendación
- ✅ **Mantenibilidad:** Las reglas son independientes y modificables
- ✅ **Validación:** El sistema experto reproduce el razonamiento del experto humano

El sistema cumple con los objetivos de la Tarea 5.2 proporcionando un apoyo a la decisión inicial coherente, explicable y basado en conocimiento experto validado.
