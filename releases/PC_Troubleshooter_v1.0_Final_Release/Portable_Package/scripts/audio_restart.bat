@echo off
echo ========================================
echo    Audio Services Restart Tool
echo ========================================
echo.

echo [INFO] Stopping audio services...
net stop "Windows Audio"
net stop "Windows Audio Endpoint Builder"
net stop "Multimedia Class Scheduler"

echo.
echo [INFO] Waiting 3 seconds...
timeout /t 3 /nobreak >nul

echo.
echo [INFO] Starting audio services...
net start "Multimedia Class Scheduler"
net start "Windows Audio Endpoint Builder"
net start "Windows Audio"

echo.
echo [INFO] Current audio service status:
sc query "Audiosrv" | findstr "STATE"
sc query "AudioEndpointBuilder" | findstr "STATE"
sc query "MMCSS" | findstr "STATE"

echo.
echo [INFO] Audio devices status:
powershell -Command "Get-AudioDevice -List | Format-Table"

echo.
echo ========================================
echo Audio services restart completed!
echo ========================================
