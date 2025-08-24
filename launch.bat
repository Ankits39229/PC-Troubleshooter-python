@echo off
title PC Troubleshooter v1.0
cls
echo ===============================================
echo           PC Troubleshooter v1.0
echo      Professional System Diagnostics
echo ===============================================
echo.

REM Change to script directory
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python is not installed or not found in PATH
    echo.
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    echo Alternatively, run "install_dependencies.bat" as Administrator
    pause
    exit /b 1
)

REM Check if dependencies are installed
if not exist "requirements_installed.txt" (
    echo Dependencies not found. Installing...
    echo.
    echo Installing PyQt6...
    pip install PyQt6>=6.4.0
    
    if %errorLevel% equ 0 (
        echo Dependencies installed > requirements_installed.txt
        echo Installation completed successfully!
        echo.
    ) else (
        echo ERROR: Failed to install dependencies
        echo Please run "install_dependencies.bat" as Administrator
        pause
        exit /b 1
    )
)

REM Start the application
echo Starting PC Troubleshooter...
echo.
python main.py

REM Check exit status
if %errorLevel% neq 0 (
    echo.
    echo Application exited with error code: %errorLevel%
    echo.
    echo Common solutions:
    echo 1. Run as Administrator for full functionality
    echo 2. Check if all dependencies are installed
    echo 3. Ensure Windows is up to date
    echo.
    pause
)

echo.
echo Thank you for using PC Troubleshooter v1.0
pause
