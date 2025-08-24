@echo off
echo ========================================
echo    Graphics Driver Reset Tool
echo ========================================
echo.

echo [INFO] Resetting graphics driver (TDR reset)...
echo [INFO] This will temporarily black out your screen...

:: Kill GPU processes
echo [INFO] Stopping GPU-intensive processes...
taskkill /f /im dwm.exe >nul 2>&1
timeout /t 2 /nobreak >nul

:: Restart Windows Desktop Window Manager
echo [INFO] Restarting Desktop Window Manager...
start dwm.exe

echo.
echo [INFO] Disabling and re-enabling display adapters...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Display'} | ForEach-Object { Write-Host 'Resetting:' $_.FriendlyName; Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false; Start-Sleep -Seconds 2; Enable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false }"

echo.
echo [INFO] Clearing graphics cache...
del /f /q "%localappdata%\Microsoft\DirectX\*.*" >nul 2>&1
rd /s /q "%localappdata%\NVIDIA Corporation\GeForce Experience\CefCache" >nul 2>&1
rd /s /q "%localappdata%\AMD\DxCache" >nul 2>&1

echo.
echo [INFO] Current display adapter status:
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Display'} | Format-Table FriendlyName, Status -AutoSize"

echo.
echo ========================================
echo Graphics driver reset completed!
echo You may need to restart your computer if issues persist.
echo ========================================
