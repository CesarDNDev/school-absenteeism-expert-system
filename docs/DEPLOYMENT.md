# 🚀 Guía de Despliegue en Streamlit Cloud

## Pasos para desplegar la aplicación

### 1. Preparar el repositorio en GitHub

Asegúrate de que todos los archivos estén en el repositorio:
- ✅ `app.py` - Aplicación Streamlit
- ✅ `sistema_experto.py` - Motor de inferencia
- ✅ `requirements.txt` - Dependencias
- ✅ `README.md` - Documentación

### 2. Acceder a Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con tu cuenta de GitHub
3. Haz clic en **"New app"**

### 3. Configurar el despliegue

Completa los campos:

- **Repository**: `CesarDNDev/school-absenteeism-expert-system`
- **Branch**: `main` (o `master`)
- **Main file path**: `app.py`
- **App URL** (opcional): Elige un nombre personalizado

### 4. Desplegar

1. Haz clic en **"Deploy!"**
2. Espera 2-3 minutos mientras se instalan las dependencias
3. La aplicación estará disponible en una URL como:
   ```
   https://[tu-app-name].streamlit.app
   ```

## 🔧 Solución de problemas

### Error: "Module not found"
- Verifica que `requirements.txt` esté en la raíz del repositorio
- Asegúrate de que las versiones sean compatibles

### Error: "App failed to load"
- Revisa los logs en Streamlit Cloud
- Verifica que `app.py` no tenga errores de sintaxis
- Comprueba que `sistema_experto.py` esté en el mismo directorio

### La app se reinicia constantemente
- Puede ser un problema de memoria
- Streamlit Cloud gratuito tiene límites de recursos
- Considera optimizar el código si es necesario

## 📝 Configuración adicional (opcional)

### Crear archivo `.streamlit/config.toml`

Para personalizar la apariencia:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
```

## 🔄 Actualizar la aplicación

Cada vez que hagas `git push` al repositorio, Streamlit Cloud:
1. Detectará los cambios automáticamente
2. Reconstruirá la aplicación
3. La desplegará con los nuevos cambios

## 📊 Monitoreo

En el panel de Streamlit Cloud puedes:
- Ver logs en tiempo real
- Reiniciar la aplicación manualmente
- Ver estadísticas de uso
- Gestionar configuraciones

## 🌐 URL final esperada

Una vez desplegado, tu aplicación estará disponible en:
```
https://school-absenteeism-expert-system.streamlit.app
```

O similar, dependiendo de la disponibilidad del nombre.

---

**¡Listo!** Tu sistema experto estará accesible desde cualquier navegador 🎉
