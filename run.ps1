# Script PowerShell para ejecutar el Sistema Experto de Absentismo Escolar

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Sistema Experto de Absentismo Escolar" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Iniciando aplicacion Streamlit..." -ForegroundColor Green
Write-Host ""

# Configurar Streamlit para modo headless
$env:STREAMLIT_SERVER_HEADLESS = 'true'

# Ejecutar Streamlit
python -m streamlit run app.py --server.headless true

Write-Host ""
Write-Host "Aplicacion cerrada." -ForegroundColor Yellow
Read-Host "Presiona Enter para salir"
