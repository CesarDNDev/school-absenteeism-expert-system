@echo off
echo ========================================
echo Sistema Experto de Absentismo Escolar
echo ========================================
echo.

REM Verificar si streamlit está instalado
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ERROR: Streamlit no esta instalado
    echo.
    echo Por favor, ejecuta primero: install.bat
    echo.
    pause
    exit /b 1
)

echo Iniciando aplicacion Streamlit...
echo.
echo La aplicacion se abrira en tu navegador en:
echo http://localhost:8501
echo.
echo Para cerrar: Presiona Ctrl+C o cierra esta ventana
echo.

REM Configurar Streamlit para modo headless
set STREAMLIT_SERVER_HEADLESS=true

REM Ejecutar Streamlit
python -m streamlit run app.py --server.headless true

pause
