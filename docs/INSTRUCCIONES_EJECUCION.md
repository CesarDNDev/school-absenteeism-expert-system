# Instrucciones de Ejecución

## Primera vez: Instalar dependencias

**IMPORTANTE:** Antes de ejecutar por primera vez, instala las dependencias:

### Opción 1: Script de instalación (Recomendado)
1. Haz doble clic en `install.bat`
2. Espera a que termine la instalación
3. Cierra la ventana

### Opción 2: Manual
```bash
pip install -r requirements.txt
```

---

## Ejecutar la aplicación localmente

### Opción 1: Script BAT (Windows - Doble clic)
1. Haz doble clic en `run.bat`
2. Se abrirá una ventana de consola
3. El navegador se abrirá automáticamente en http://localhost:8501
4. Para cerrar: Cierra la ventana de consola o presiona `Ctrl+C`

### Opción 2: Script PowerShell
1. Click derecho en `run.ps1` → "Ejecutar con PowerShell"
2. O desde PowerShell: `.\run.ps1`
3. El navegador se abrirá automáticamente en http://localhost:8501
4. Para cerrar: Presiona `Ctrl+C` y luego Enter

### Opción 3: Línea de comandos manual
```bash
python -m streamlit run app.py
```

## Requisitos previos

Asegúrate de tener instaladas las dependencias:
```bash
pip install -r requirements.txt
```

## URLs de acceso

Una vez iniciada la aplicación, estará disponible en:
- **Local:** http://localhost:8501
- **Red local:** http://[tu-ip]:8501

## Solución de problemas

### Error: "streamlit no se reconoce como comando"
```bash
pip install streamlit --user
```

### Error: "No module named 'clips'"
```bash
pip install clipspy
```

### El navegador no se abre automáticamente
Abre manualmente: http://localhost:8501

### Puerto 8501 ocupado
Usa un puerto diferente:
```bash
python -m streamlit run app.py --server.port 8502
```

## Detener la aplicación

- **Desde consola:** Presiona `Ctrl+C`
- **Desde Windows:** Cierra la ventana de consola
- **Forzar cierre:** `taskkill /F /IM python.exe` (cierra todos los procesos Python)
