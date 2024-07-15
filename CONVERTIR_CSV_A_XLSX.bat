@echo off
setlocal

rem Obtener la ruta completa del directorio del script .bat
set "SCRIPT_DIR=%~dp0"

rem Navegar al directorio del script .bat
cd /d "%SCRIPT_DIR%"

rem Ejecutar el archivo .py con Python
python convierte.py



