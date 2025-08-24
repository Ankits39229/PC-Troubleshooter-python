@echo off
echo ========================================
echo    Bluetooth Service Restart Tool
echo ========================================
echo.

echo [INFO] Stopping Bluetooth services...
net stop "Bluetooth Support Service"
net stop "Bluetooth Audio Gateway Service"
net stop "Bluetooth User Service"

echo.
echo [INFO] Waiting 3 seconds...
timeout /t 3 /nobreak >nul

echo.
echo [INFO] Starting Bluetooth services...
net start "Bluetooth Support Service"
net start "Bluetooth Audio Gateway Service" 
net start "Bluetooth User Service"

echo.
echo [INFO] Current Bluetooth service status:
sc query "bthserv" | findstr "STATE"
sc query "BTAGService" | findstr "STATE"
sc query "BluetoothUserService" | findstr "STATE"

echo.
echo ========================================
echo Bluetooth services restart completed!
echo ========================================
