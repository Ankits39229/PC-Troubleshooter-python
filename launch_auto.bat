@echo off
title PC Troubleshooter Launcher
echo Starting PC Troubleshooter...
echo.

cd /d "%~dp0"

:: Try to find Python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Using system Python...
    python main.py
) else (
    echo Python not found in PATH. Trying specific installation...
    C:/Users/thisi/AppData/Local/Programs/Python/Python313/python.exe main.py
)

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Could not start PC Troubleshooter.
    echo Please ensure Python and PyQt6 are installed.
    echo.
    pause
)
