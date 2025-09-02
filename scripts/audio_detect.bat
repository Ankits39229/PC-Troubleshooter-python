@echo off
echo ========================================
echo    Audio Device Detection Tool
echo ========================================
echo.

echo [INFO] Detecting audio devices...
powershell -Command "Get-WmiObject -Class Win32_SoundDevice | Select-Object Name, Status, DeviceID | Format-Table -AutoSize"

echo.
echo [INFO] Audio playback devices:
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'MEDIA' -or $_.Class -eq 'AudioEndpoint'} | Select-Object FriendlyName, Status | Format-Table -AutoSize"

echo.
echo [INFO] Audio recording devices:
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'MEDIA' -or $_.Class -eq 'AudioEndpoint'} | Select-Object FriendlyName, Status | Format-Table -AutoSize"

echo.
echo [INFO] Checking audio drivers in Device Manager...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'AudioEndpoint' -or $_.Class -eq 'MEDIA'} | Format-Table FriendlyName, Status -AutoSize"

echo.
echo [INFO] Current default audio device:
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'MEDIA'} | Select-Object -First 1 | Select-Object FriendlyName, Status | Format-Table -AutoSize"

echo.
echo ========================================
echo Audio device detection completed!
echo ========================================
