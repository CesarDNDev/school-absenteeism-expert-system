@echo off
echo ========================================
echo Sistema Experto de Absentismo Escolar
echo ========================================
echo.
echo Iniciando aplicacion Streamlit...
echo.

REM Configurar Streamlit para modo headless
set STREAMLIT_SERVER_HEADLESS=true

REM Ejecutar Streamlit
python -m streamlit run app.py --server.headless true

pause
