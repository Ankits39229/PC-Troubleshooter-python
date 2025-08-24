@echo off
title PC Troubleshooter - EXE Builder
echo ========================================
echo PC Troubleshooter EXE Builder
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

echo 🔨 Building EXE package...
python build_exe.py

echo.
echo 🏁 EXE build process completed!
echo Check the 'dist' and 'releases' folders for your executable.
echo.
pause
