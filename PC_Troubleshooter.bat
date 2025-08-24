@echo off
color 0B
title PC Troubleshooter - Professional System Diagnostics
cls

echo.
echo        ╔══════════════════════════════════════════════════════════╗
echo        ║              PC TROUBLESHOOTER v1.0                     ║
echo        ║          Professional System Diagnostics Tool           ║
echo        ╚══════════════════════════════════════════════════════════╝
echo.
echo                            🔧 Starting Application...
echo.

cd /d "%~dp0"

:: Check for Python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo                        ✅ Python found - launching GUI...
    echo.
    timeout /t 2 /nobreak >nul
    python main.py
) else (
    echo                        🔍 Searching for Python installation...
    if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\python.exe" (
        echo                        ✅ Python found - launching GUI...
        echo.
        timeout /t 2 /nobreak >nul
        "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\python.exe" main.py
    ) else (
        echo.
        echo                        ❌ Python not found!
        echo.
        echo        Please install Python 3.7+ and PyQt6:
        echo        1. Download Python from python.org
        echo        2. Run: pip install PyQt6
        echo.
        pause
    )
)

if %errorlevel% neq 0 (
    echo.
    echo                        ❌ Error starting PC Troubleshooter
    echo.
    echo        Possible solutions:
    echo        • Run as Administrator
    echo        • Check if PyQt6 is installed: pip install PyQt6
    echo        • Verify Python installation
    echo.
    pause
)
