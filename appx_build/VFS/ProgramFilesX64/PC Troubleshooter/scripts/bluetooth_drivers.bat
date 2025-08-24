@echo off
echo ========================================
echo    Bluetooth Driver Check Tool
echo ========================================
echo.

echo [INFO] Checking Bluetooth devices in Device Manager...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Bluetooth' -or $_.FriendlyName -like '*Bluetooth*'} | Format-Table FriendlyName, Status, InstanceId -AutoSize"

echo.
echo [INFO] Checking Bluetooth services...
sc query "bthserv"
echo.
sc query "BTAGService"
echo.

echo [INFO] Checking for Bluetooth hardware...
powershell -Command "Get-WmiObject -Class Win32_PnPEntity | Where-Object {$_.Name -like '*Bluetooth*'} | Select-Object Name, Status, DeviceID"

echo.
echo [INFO] Bluetooth registry information...
reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\bthserv" /v Start

echo.
echo ========================================
echo Bluetooth driver check completed!
echo ========================================
