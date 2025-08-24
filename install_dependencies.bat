@echo off
title PC Troubleshooter v1.0 - Dependency Installer
echo ===============================================
echo   PC Troubleshooter v1.0 - Install Dependencies
echo ===============================================
echo.

REM Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: This script requires Administrator privileges.
    echo Please right-click and select "Run as Administrator"
    echo.
    pause
    exit /b 1
)

echo Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python is not installed or not found in PATH
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Checking version...
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Python version: %PYTHON_VERSION%

echo.
echo Installing Python dependencies...
echo.

REM Upgrade pip first
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install PyQt6
echo Installing PyQt6 GUI framework...
pip install PyQt6>=6.4.0

if %errorLevel% neq 0 (
    echo.
    echo ERROR: Failed to install PyQt6
    echo This might be due to:
    echo 1. No internet connection
    echo 2. Antivirus blocking installation
    echo 3. Python version compatibility issue
    echo.
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

REM Create marker file to indicate dependencies are installed
echo Dependencies installed successfully > requirements_installed.txt
echo Installation date: %date% %time% >> requirements_installed.txt

echo.
echo ===============================================
echo   Installation completed successfully!
echo ===============================================
echo.
echo PC Troubleshooter is now ready to use.
echo.
echo To start the application:
echo   - Double-click "launch.bat" for normal mode
echo   - Double-click "launch_admin.bat" for administrator mode
echo.
echo For best results, always run as Administrator.
echo.
pause
