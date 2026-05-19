# Instrucciones de Instalación y Ejecución

## Sistema Experto de Absentismo Escolar

---

## Requisitos previos

- **Python 3.11 o 3.12** instalado en el sistema
- **Conexión a Internet** (solo para la instalación inicial)

---

## Instalación (Primera vez)

### Opción 1: Instalación automática (RECOMENDADO)

1. Abre la carpeta del proyecto
2. Haz **doble clic** en `install.bat`
3. Espera a que termine la instalación (puede tardar 1-2 minutos)
4. Cierra la ventana cuando veas "Instalación completada!"

### Opción 2: Instalación manual

Abre una terminal (CMD o PowerShell) en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

---

## Ejecutar la aplicación

### Opción 1: Script BAT (MÁS FÁCIL)

1. Haz **doble clic** en `run.bat`
2. Se abrirá una ventana de consola
3. El navegador se abrirá automáticamente en http://localhost:8501
4. ¡Listo! Ya puedes usar el sistema experto

### Opción 2: Script PowerShell

1. Click derecho en `run.ps1` → "Ejecutar con PowerShell"
2. El navegador se abrirá automáticamente

### Opción 3: Línea de comandos

```bash
streamlit run app.py
```

---

## Acceder a la aplicación

Una vez iniciada, la aplicación estará disponible en:

- **URL local:** http://localhost:8501
- **URL red local:** http://[tu-ip]:8501

Si el navegador no se abre automáticamente, copia y pega la URL en tu navegador.

---

## Cerrar la aplicación

- **Opción 1:** Cierra la ventana de consola
- **Opción 2:** Presiona `Ctrl+C` en la consola y luego Enter

---

## Uso del Sistema Experto

El sistema te guiará paso a paso:

1. **Paso 1:** ¿El centro ha intervenido previamente?
2. **Paso 2:** Estado de la información
3. **Paso 3:** Situación personal del menor
4. **Paso 4:** Indicadores de desprotección
5. **Paso 5:** Intensidad del absentismo
6. **Paso 6:** Puntuación SISO (0-100)
7. **Paso 7:** Colaboración familiar
8. **Paso 8:** Antecedentes

Al final obtendrás:
- **Nivel de riesgo**
- **Recomendación inicial**
- **Explicación detallada**
- **Factores activados**

---

## Solución de problemas

### Error: "streamlit no se reconoce como comando"

**Solución:** Ejecuta `install.bat` primero para instalar las dependencias.

### Error: "No module named 'clips'"

**Solución:** 
```bash
pip install clipspy
```

### El navegador no se abre automáticamente

**Solución:** Abre manualmente http://localhost:8501 en tu navegador.

### Puerto 8501 ocupado

**Solución:** Usa un puerto diferente:
```bash
streamlit run app.py --server.port 8502
```

### Error de compilación de clipspy

**Solución:** Asegúrate de tener Python 3.11 o 3.12. Python 3.14 no es compatible.

---

## Ejecutar tests

Para verificar que el sistema funciona correctamente:

### Tests básicos
```bash
python tests/test_simple.py
```

### Tests unitarios
```bash
python tests/test_reglas.py
```

### Suite completa de casos
```bash
python tests/casos_prueba.py
```

---

## Documentación adicional

- **Reglas CLIPS:** `docs/REGLAS_CLIPS.md`
- **Estructura del proyecto:** `docs/ESTRUCTURA_PROYECTO.md`
- **Instrucciones de ejecución:** `docs/INSTRUCCIONES_EJECUCION.md`

---

## Consejos

- Ejecuta `install.bat` solo la primera vez
- Usa `run.bat` cada vez que quieras usar la aplicación
- Puedes tener múltiples casos abiertos en diferentes pestañas del navegador
- Usa el botón "Reiniciar" en la barra lateral para analizar un nuevo caso

---

## Soporte

**Autor:** César Domínguez Notario  
**Proyecto:** Sistema Experto de Absentismo Escolar  
**Módulo:** Modelos de Inteligencia Artificial  
**Curso:** 2025-2026

---

## Resumen rápido

```
1. Doble clic en install.bat (solo primera vez)
2. Doble clic en run.bat
3. Usar la aplicación en http://localhost:8501
4. Cerrar la ventana de consola cuando termines
```

Eso es todo.
