@echo off
echo ========================================
echo    Audio Device Detection Tool
echo ========================================
echo.

echo [INFO] Detecting audio devices...
powershell -Command "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status, DeviceID | Format-Table -AutoSize"

echo.
echo [INFO] Audio playback devices:
powershell -Command "Get-AudioDevice -Playback | Format-Table"

echo.
echo [INFO] Audio recording devices:
powershell -Command "Get-AudioDevice -Recording | Format-Table"

echo.
echo [INFO] Checking audio drivers in Device Manager...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'AudioEndpoint' -or $_.Class -eq 'MEDIA'} | Format-Table FriendlyName, Status -AutoSize"

echo.
echo [INFO] Current default audio device:
powershell -Command "Get-AudioDevice -Default | Format-Table"

echo.
echo ========================================
echo Audio device detection completed!
echo ========================================
