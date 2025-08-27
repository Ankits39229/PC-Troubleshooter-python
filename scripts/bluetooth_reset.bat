@echo off
echo ========================================
echo    Bluetooth Stack Reset Tool
echo ========================================
echo.

:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [INFO] Running with administrator privileges.
) else (
    echo [WARNING] Administrator privileges are required for Bluetooth stack reset.
    echo [INFO] This is needed to stop/start services, modify registry, and reset Bluetooth adapters.
    echo [INFO] Relaunching as administrator...
    powershell "start-process cmd -argumentlist '/c %~f0' -verb runas"
    exit
)

echo [INFO] Stopping Bluetooth services...
net stop "Bluetooth Support Service" >nul 2>&1
net stop "Bluetooth Audio Gateway Service" >nul 2>&1
net stop "Bluetooth User Service" >nul 2>&1

echo.
echo [INFO] Clearing Bluetooth cache...
del /f /q "%localappdata%\Microsoft\Windows\Bluetooth\*.*" >nul 2>&1
rd /s /q "%localappdata%\Microsoft\Windows\Bluetooth" >nul 2>&1

echo.
echo [INFO] Resetting Bluetooth registry entries...
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\DeviceSetup\Bluetooth" /f >nul 2>&1

echo.
echo [INFO] Disabling Bluetooth adapter...
powershell -Command "Disable-PnpDevice -InstanceId (Get-PnpDevice | Where-Object {$_.Class -eq 'Bluetooth'}).InstanceId -Confirm:$false" >nul 2>&1

echo.
echo [INFO] Waiting 5 seconds...
timeout /t 5 /nobreak >nul

echo.
echo [INFO] Enabling Bluetooth adapter...
powershell -Command "Enable-PnpDevice -InstanceId (Get-PnpDevice | Where-Object {$_.Class -eq 'Bluetooth'}).InstanceId -Confirm:$false" >nul 2>&1

echo.
echo [INFO] Starting Bluetooth services...
net start "Bluetooth Support Service" >nul 2>&1
net start "Bluetooth Audio Gateway Service" >nul 2>&1
net start "Bluetooth User Service" >nul 2>&1

echo.
echo ========================================
echo Bluetooth stack reset completed!
echo Please try pairing your devices again.
echo ========================================

exit
