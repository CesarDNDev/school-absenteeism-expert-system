# Ejecutar el Sistema Experto en CLIPS

Este documento explica cómo ejecutar el sistema experto interactivo en CLIPS.

---

## Requisitos

- **CLIPS** instalado en el sistema
- Descargar desde: https://www.clipsrules.net/

---

## Archivos necesarios

- `sistema_experto.clp` - Sistema experto interactivo en CLIPS

---

## Instrucciones de ejecución

### 1. Abrir CLIPS

Ejecuta el intérprete de CLIPS desde la línea de comandos:

```bash
clips
```

O abre la interfaz gráfica de CLIPS (CLIPS IDE).

### 2. Cargar el sistema experto

En CLIPS IDE: `File` → `Load` → Selecciona `sistema_experto.clp`

O desde la línea de comandos:
```clips
CLIPS> (load "sistema_experto.clp")
```

### 3. Resetear el entorno

```clips
CLIPS> (reset)
```

### 4. Ejecutar el sistema

```clips
CLIPS> (run)
```

### 5. Responder a las preguntas

El sistema te hará preguntas paso a paso. Responde según el caso que quieras analizar.

**El sistema se detendrá automáticamente** cuando llegue a una conclusión y mostrará:
- Recomendación
- Nivel de riesgo
- Explicación detallada

---

## Ejemplo de ejecución

```
CLIPS> (reset)
CLIPS> (run)

========================================
SISTEMA EXPERTO DE ABSENTISMO ESCOLAR
========================================

PREGUNTA 1: Intervencion previa del centro
¿El centro educativo ha realizado intervencion previa?
Respuesta (si/no): si

PREGUNTA 2: Estado de la informacion
¿Como es la informacion disponible?
Opciones: completa / incompleta / contradictoria
Respuesta: completa

PREGUNTA 3: Situacion personal del menor
¿Presenta alguna de estas situaciones?
1. sin_indicadores
2. salud_mental_grave
3. psicopatologia
4. consumo_sustancias
5. conducta_disruptiva
Respuesta: sin_indicadores

PREGUNTA 4: Indicadores de desproteccion
¿Se detectan indicadores de desproteccion del menor?
Respuesta (si/no): no

PREGUNTA 5: Intensidad del absentismo
¿Cual es la intensidad de las faltas?
Opciones: baja / media / alta
Respuesta: baja

PREGUNTA 6: Vulnerabilidad social (SISO)
Puntuacion SISO del caso (0-100):
Umbral critico: 58 puntos
Respuesta: 45

PREGUNTA 7: Colaboracion familiar
¿Cual es el nivel de colaboracion de la familia?
Opciones: nula / baja / media / alta
Respuesta: alta

PREGUNTA 8: Antecedentes
¿Existen antecedentes de absentismo en este menor?
Respuesta (si/no): no

========================================
RESULTADO
========================================
Recomendacion: Seguimiento
Nivel de riesgo: Bajo

EXPLICACION:
- Caso de RIESGO BAJO: Faltas esporadicas
- La familia muestra colaboracion adecuada
- RECOMENDACION: Mantener seguimiento ordinario
========================================
```

---

## Valores válidos para las respuestas

### 1. intervencion-previa-centro
- `si`
- `no`

### 2. intensidad-absentismo
- `baja` (~25% de faltas)
- `media` (~50% de faltas)
- `alta` (~75% de faltas)

### 3. siso
- Número entre `0` y `100`
- Umbral crítico: `58`

### 4. colaboracion-familiar
- `nula`
- `baja`
- `media`
- `alta`

### 5. antecedentes
- `si`
- `no`

### 6. desproteccion
- `si`
- `no`

### 7. situacion-personal
- `sin_indicadores`
- `salud_mental_grave`
- `psicopatologia`
- `consumo_sustancias`
- `conducta_disruptiva`

### 8. estado-informacion
- `completa`
- `incompleta`
- `contradictoria`

---

## Casos de prueba sugeridos

Para probar diferentes flujos del sistema, consulta el documento `CASOS_DEMOSTRACION.md` que contiene 10 casos completos con sus datos de entrada y resultados esperados.

---

## Comandos útiles de CLIPS

### Analizar otro caso
```clips
CLIPS> (reset)
CLIPS> (run)
```

### Ver todas las reglas cargadas
```clips
CLIPS> (rules)
```

### Salir de CLIPS
```clips
CLIPS> (exit)
```

---

## Notas importantes

1. **Sistema interactivo:** El sistema hace preguntas paso a paso
2. **Detención automática:** El sistema se detiene cuando llega a una conclusión
3. **Resetear entre casos:** Ejecuta `(reset)` y `(run)` para analizar un nuevo caso
4. **Prioridades:** Las reglas tienen diferentes prioridades para controlar el flujo de preguntas

---

## Autor

**César Domínguez Notario**  
Módulo: Modelos de Inteligencia Artificial  
Curso: 2025-2026
