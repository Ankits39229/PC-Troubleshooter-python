@echo off
echo ========================================
echo    Temporary Files Cleanup Tool
echo ========================================
echo.

:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [INFO] Running with administrator privileges.
) else (
    echo [WARNING] Administrator privileges are required for temporary files cleanup.
    echo [INFO] This is needed to clean system temporary files, prefetch, and Windows Update cache.
    echo [INFO] Relaunching as administrator...
    powershell "start-process cmd -argumentlist '/c %~f0' -verb runas"
    exit
)

echo [INFO] Clearing Windows temporary files...
del /f /s /q "%temp%\*.*" >nul 2>&1
for /d %%i in ("%temp%\*") do rd /s /q "%%i" >nul 2>&1

echo [INFO] Clearing system temporary files...
del /f /s /q "C:\Windows\Temp\*.*" >nul 2>&1
for /d %%i in ("C:\Windows\Temp\*") do rd /s /q "%%i" >nul 2>&1

echo [INFO] Clearing prefetch files...
del /f /s /q "C:\Windows\Prefetch\*.*" >nul 2>&1

echo [INFO] Clearing recent documents...
del /f /s /q "%userprofile%\Recent\*.*" >nul 2>&1

echo [INFO] Clearing browser cache (Internet Explorer)...
del /f /s /q "%userprofile%\AppData\Local\Microsoft\Windows\INetCache\*.*" >nul 2>&1
for /d %%i in ("%userprofile%\AppData\Local\Microsoft\Windows\INetCache\*") do rd /s /q "%%i" >nul 2>&1

echo [INFO] Clearing Windows Update cache...
net stop wuauserv >nul 2>&1
del /f /s /q "C:\Windows\SoftwareDistribution\Download\*.*" >nul 2>&1
for /d %%i in ("C:\Windows\SoftwareDistribution\Download\*") do rd /s /q "%%i" >nul 2>&1
net start wuauserv >nul 2>&1

echo [INFO] Clearing DNS cache...
ipconfig /flushdns >nul 2>&1

echo [INFO] Emptying Recycle Bin...
powershell -Command "Clear-RecycleBin -Confirm:$false" >nul 2>&1

echo.
echo [INFO] Calculating freed space...
powershell -Command "$before = (Get-WmiObject -Class Win32_LogicalDisk | Where-Object {$_.DeviceID -eq 'C:'}).FreeSpace; Write-Host 'Cleanup completed. Check disk space for freed storage.'"

echo.
echo ========================================
echo Temporary files cleanup completed!
echo ========================================

exit
