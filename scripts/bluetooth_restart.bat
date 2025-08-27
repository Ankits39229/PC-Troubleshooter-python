@echo off
echo ========================================
echo    Bluetooth Service Restart Tool
echo ========================================
echo.

echo [INFO] Stopping Bluetooth services...
net stop bthserv
net stop BTAGService
net stop BluetoothUserService

echo.
echo [INFO] Waiting 3 seconds...
timeout /t 3 /nobreak >nul

echo.
echo [INFO] Starting Bluetooth services...
net start bthserv
net start BTAGService
net start BluetoothUserService

echo.
echo [INFO] Current Bluetooth service status:
sc query "bthserv" | findstr "STATE"
sc query "BTAGService" | findstr "STATE"
sc query "BluetoothUserService" | findstr "STATE"

echo.
echo ========================================
echo Bluetooth services restart completed!
echo ========================================
