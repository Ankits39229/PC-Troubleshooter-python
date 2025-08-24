@echo off
echo ========================================
echo    Network Stack Reset Tool
echo ========================================
echo.

echo [INFO] Resetting Winsock catalog...
netsh winsock reset
if %errorlevel% equ 0 (
    echo [SUCCESS] Winsock catalog reset successfully
) else (
    echo [ERROR] Failed to reset Winsock catalog
)
echo.

echo [INFO] Resetting TCP/IP stack...
netsh int ip reset
if %errorlevel% equ 0 (
    echo [SUCCESS] TCP/IP stack reset successfully
) else (
    echo [ERROR] Failed to reset TCP/IP stack
)
echo.

echo [INFO] Releasing current IP configuration...
ipconfig /release
echo.

echo [INFO] Renewing IP configuration...
ipconfig /renew
echo.

echo [INFO] Flushing DNS resolver cache...
ipconfig /flushdns
if %errorlevel% equ 0 (
    echo [SUCCESS] DNS cache flushed successfully
) else (
    echo [ERROR] Failed to flush DNS cache
)
echo.

echo ========================================
echo Network stack reset completed!
echo Please restart your computer for changes to take effect.
echo ========================================
