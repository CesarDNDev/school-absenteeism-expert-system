# Casos de Demostración del Sistema Experto

## Sistema Experto de Absentismo Escolar en Adolescentes

Este documento contiene 10 casos de prueba que demuestran todos los flujos del sistema experto.

---

## CASO 1: Sin Intervención Previa del Centro

**Descripción:** El centro educativo no ha realizado ninguna actuación previa.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → **No**
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- Desprotección → No
- Intensidad del absentismo → Media
- Puntuación SISO → 45
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Ampliar información
- **Nivel de riesgo:** No valorable
- **Explicación:** El centro debe realizar intervención previa antes de derivar a servicios sociales

---

## CASO 2: Desprotección del Menor (PRIORIDAD MÁXIMA)

**Descripción:** Se detectan indicadores de desprotección del menor.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → **Sí**
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- **Desprotección → Sí**
- Intensidad del absentismo → Media
- Puntuación SISO → 45
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Intervención ETI urgente
- **Nivel de riesgo:** Alto - Desprotección
- **Explicación:** Intervención urgente del Equipo Técnico de Inclusión

---

## CASO 3: Riesgo Bajo - Seguimiento Ordinario

**Descripción:** Faltas esporádicas con buena colaboración familiar.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- Desprotección → No
- **Intensidad del absentismo → Baja**
- **Puntuación SISO → 45** (≤ 58)
- **Colaboración familiar → Alta**
- **Antecedentes → No**

**Resultado esperado:**
- **Recomendación:** Seguimiento
- **Nivel de riesgo:** Bajo
- **Explicación:** Mantener seguimiento ordinario desde el centro educativo

---

## CASO 4: Intervención Preventiva (Vulnerabilidad Alta)

**Descripción:** Pocas faltas pero alta vulnerabilidad social (SISO > 58).

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- Desprotección → No
- **Intensidad del absentismo → Baja**
- **Puntuación SISO → 65** (> 58)
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Intervención ETI (preventiva)
- **Nivel de riesgo:** Preventivo - Vulnerabilidad alta
- **Explicación:** Intervención preventiva para evitar desprotección futura

---

## CASO 5: Intervención ETI Especializada

**Descripción:** Absentismo consolidado con alta vulnerabilidad social.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- Desprotección → No
- **Intensidad del absentismo → Alta**
- **Puntuación SISO → 70** (> 58)
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Intervención ETI
- **Nivel de riesgo:** Medio-Alto
- **Explicación:** Absentismo consolidado + Vulnerabilidad elevada

---

## CASO 6: No Cooperación Familiar

**Descripción:** Absentismo alto sin colaboración de la familia.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- Desprotección → No
- **Intensidad del absentismo → Alta**
- Puntuación SISO → 45
- **Colaboración familiar → Nula**
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Intervención ETI con valoración de derivación
- **Nivel de riesgo:** Alto - No cooperación familiar
- **Explicación:** Posible derivación a Fiscalía si persisten faltas tras 3-6 meses

---

## CASO 7: Equipo de Familia

**Descripción:** Absentismo consolidado pero familia colaboradora y vulnerabilidad moderada.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- Estado de la información → Completa
- Situación personal → Sin indicadores especiales
- Desprotección → No
- **Intensidad del absentismo → Media**
- **Puntuación SISO → 50** (≤ 58)
- **Colaboración familiar → Alta**
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Equipo de familia
- **Nivel de riesgo:** Medio
- **Explicación:** Derivar a Equipo de Familia para intervención ordinaria

---

## CASO 8: Caso Complejo - Revisión Manual

**Descripción:** Situación personal compleja que requiere valoración especializada.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- Estado de la información → Completa
- **Situación personal → Salud mental grave**
- Desprotección → No
- Intensidad del absentismo → Media
- Puntuación SISO → 45
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Revisión manual obligatoria
- **Nivel de riesgo:** Requiere valoración especializada
- **Explicación:** Caso fuera del sistema experto automático

---

## CASO 9: Información Incompleta

**Descripción:** La información disponible es insuficiente para valorar el caso.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- **Estado de la información → Incompleta**
- Situación personal → Sin indicadores especiales
- Desprotección → No
- Intensidad del absentismo → Media
- Puntuación SISO → 45
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Ampliar información
- **Nivel de riesgo:** No valorable
- **Explicación:** Solicitar datos adicionales al centro educativo y/o familia

---

## CASO 10: Información Contradictoria

**Descripción:** Existen contradicciones entre las fuentes de información.

**Datos de entrada:**
- ¿El centro ha intervenido previamente? → Sí
- **Estado de la información → Contradictoria**
- Situación personal → Sin indicadores especiales
- Desprotección → No
- Intensidad del absentismo → Media
- Puntuación SISO → 45
- Colaboración familiar → Media
- Antecedentes → No

**Resultado esperado:**
- **Recomendación:** Ampliar información
- **Nivel de riesgo:** No valorable
- **Explicación:** Contactar con equipo de atención primaria para aclarar contradicciones

---

## Resumen de Flujos Demostrados

| Caso | Flujo Principal | Prioridad |
|------|----------------|-----------|
| 1 | Sin intervención previa | Bloqueante |
| 2 | Desprotección | Máxima (100) |
| 3 | Seguimiento ordinario | Baja (10) |
| 4 | Intervención preventiva | Media (20) |
| 5 | Intervención ETI especializada | Media-Alta (30) |
| 6 | No cooperación familiar | Alta (40) |
| 7 | Equipo de familia | Media (25) |
| 8 | Revisión manual | Muy Alta (90) |
| 9 | Información incompleta | Alta (80) |
| 10 | Información contradictoria | Muy Alta (85) |

---

## Notas para la Demostración

### Orden recomendado de presentación:

1. **Caso 3** (Riesgo bajo) - Mostrar el flujo más simple
2. **Caso 1** (Sin intervención) - Mostrar validación inicial
3. **Caso 2** (Desprotección) - Mostrar prioridad máxima
4. **Caso 8** (Caso complejo) - Mostrar límites del sistema
5. **Caso 5** (ETI especializada) - Mostrar caso típico de intervención
6. **Caso 6** (No cooperación) - Mostrar escalado de riesgo
7. **Caso 4** (Preventiva) - Mostrar enfoque preventivo

### Puntos clave a destacar:

- **Sistema basado en vectores ordenados** (no usa deftemplate)
- **Motor de inferencia CLIPS** con reglas de producción
- **Prioridades (salience)** para control de flujo
- **10 reglas de producción** que cubren todos los escenarios
- **Interfaz interactiva** paso a paso
- **Explicaciones detalladas** de cada decisión

---

## Ejecución de los Tests

Para ejecutar todos los casos automáticamente:

```bash
python test_vectores.py
```

Para ejecutar la aplicación interactiva:

```bash
run.bat
```

O manualmente:

```bash
python -m streamlit run app.py
```
