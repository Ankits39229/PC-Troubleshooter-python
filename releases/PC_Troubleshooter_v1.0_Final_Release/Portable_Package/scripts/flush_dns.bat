@echo off
echo ========================================
echo    DNS Cache Flush Tool
echo ========================================
echo.

echo [INFO] Flushing DNS resolver cache...
ipconfig /flushdns

if %errorlevel% equ 0 (
    echo [SUCCESS] DNS cache flushed successfully
    echo [INFO] DNS cache has been cleared
) else (
    echo [ERROR] Failed to flush DNS cache
    echo [INFO] You may need to run this as administrator
)

echo.
echo [INFO] Displaying current DNS cache...
ipconfig /displaydns | findstr "Record Name"

echo.
echo ========================================
echo DNS flush operation completed!
echo ========================================
