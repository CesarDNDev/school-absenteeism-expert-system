@echo off
echo ========================================
echo Sistema Experto de Absentismo Escolar
echo INSTALACION DE DEPENDENCIAS
echo ========================================
echo.
echo Instalando dependencias de Python...
echo.

REM Instalar dependencias desde requirements.txt
pip install -r requirements.txt

echo.
echo ========================================
echo Instalacion completada!
echo ========================================
echo.
echo Ahora puedes ejecutar la aplicacion con run.bat
echo.
pause
