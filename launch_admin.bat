@echo off
title PC Troubleshooter v1.0 (Administrator Mode)
cls
echo ===============================================
echo      PC Troubleshooter v1.0 (Administrator)
echo      Professional System Diagnostics
echo ===============================================
echo.

REM Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting Administrator privileges...
    echo.
    powershell -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs"
    exit /b
)

echo Running with Administrator privileges...
echo.

REM Call the regular launcher
call "%~dp0launch.bat"
