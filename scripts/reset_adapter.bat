@echo off
echo ========================================
echo    Network Adapter Reset Tool
echo ========================================
echo.

echo [INFO] Disabling all network adapters...
for /f "tokens=1,2*" %%a in ('netsh interface show interface ^| findstr /i "enabled"') do (
    if not "%%c"=="" (
        echo Disabling: %%c
        netsh interface set interface "%%c" admin=disable
    )
)

echo.
echo [INFO] Waiting 3 seconds...
timeout /t 3 /nobreak >nul

echo.
echo [INFO] Enabling all network adapters...
for /f "tokens=1,2*" %%a in ('netsh interface show interface ^| findstr /i "disabled"') do (
    if not "%%c"=="" (
        echo Enabling: %%c
        netsh interface set interface "%%c" admin=enable
    )
)

echo.
echo [INFO] Current network adapter status:
netsh interface show interface

echo.
echo ========================================
echo Network adapter reset completed!
echo ========================================
