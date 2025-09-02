@echo off
echo ========================================
echo    Network Stack Reset Tool
echo ========================================
echo.

:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [INFO] Running with administrator privileges.
) else (
    echo [WARNING] Administrator privileges are required for network stack reset.
    echo [INFO] This is needed to reset Winsock catalog and TCP/IP stack, which require system-level access.
    echo [INFO] Relaunching as administrator...
    powershell "start-process cmd -argumentlist '/c %~f0' -verb runas"
    exit
)

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
echo.
echo ========================================
echo Network stack reset completed!
echo Please restart your computer for changes to take effect.
echo ========================================

exit
echo ========================================
