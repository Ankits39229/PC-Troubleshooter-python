@echo off
title PC Troubleshooter - Build Script
echo ========================================
echo PC Troubleshooter Build Script
echo ========================================
echo.

echo 🔍 Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

echo 📦 Installing build dependencies...
python -m pip install --upgrade pip
python -m pip install pyinstaller pillow
echo.

echo 🏗️ Starting build process...
echo Choose build option:
echo 1. Build EXE only
echo 2. Build APPX only  
echo 3. Build both EXE and APPX (Recommended)
echo.

set /p choice=Enter your choice (1-3): 

if "%choice%"=="1" (
    echo 🔨 Building EXE package...
    python build_all.py --exe-only --no-deps
) else if "%choice%"=="2" (
    echo 📦 Building APPX package...
    python build_all.py --appx-only --no-deps
) else if "%choice%"=="3" (
    echo 🚀 Building all packages...
    python build_all.py --no-deps
) else (
    echo ❌ Invalid choice. Building all packages by default...
    python build_all.py --no-deps
)

echo.
echo 🏁 Build process completed!
echo Check the 'releases' folder for your packages.
echo.
pause
