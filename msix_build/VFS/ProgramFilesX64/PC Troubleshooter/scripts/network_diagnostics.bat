@echo off
echo ========================================
echo    Network Diagnostics Tool
echo ========================================
echo.

echo [INFO] Current IP Configuration:
ipconfig /all
echo.

echo [INFO] Testing DNS resolution...
nslookup google.com
echo.

echo [INFO] Testing internet connectivity...
ping -n 4 8.8.8.8
echo.

echo [INFO] Testing specific website connectivity...
ping -n 4 google.com
echo.

echo [INFO] Network route table:
route print
echo.

echo [INFO] Active network connections:
netstat -an | findstr :80
netstat -an | findstr :443

echo.
echo ========================================
echo Network diagnostics completed!
echo ========================================
