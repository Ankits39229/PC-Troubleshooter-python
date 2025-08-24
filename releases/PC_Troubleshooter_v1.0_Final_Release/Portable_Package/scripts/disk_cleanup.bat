@echo off
echo ========================================
echo    Disk Cleanup Tool
echo ========================================
echo.

echo [INFO] Running Windows Disk Cleanup utility...
echo [INFO] This will open the Disk Cleanup dialog...
cleanmgr /sagerun:1

echo.
echo [INFO] Running extended cleanup...
echo [INFO] Cleaning system files and old Windows installations...

:: Clean Windows Update files
echo [INFO] Cleaning Windows Update files...
dism /online /cleanup-image /startcomponentcleanup /resetbase >nul 2>&1

:: Clean Windows Store cache
echo [INFO] Cleaning Windows Store cache...
wsreset >nul 2>&1

:: Clean thumbnail cache
echo [INFO] Cleaning thumbnail cache...
del /f /s /q "%userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache*" >nul 2>&1

:: Clean Windows logs
echo [INFO] Cleaning Windows event logs...
for /f "tokens=*" %%i in ('wevtutil el') do wevtutil cl "%%i" >nul 2>&1

:: Clean system restore points (keep latest)
echo [INFO] Cleaning old system restore points...
powershell -Command "Get-ComputerRestorePoint | Where-Object {$_.CreationTime -lt (Get-Date).AddDays(-7)} | ForEach-Object { vssadmin delete shadows /shadow=$_.ShadowId /quiet }" >nul 2>&1

echo.
echo [INFO] Current disk space:
powershell -Command "Get-WmiObject -Class Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3} | Select-Object DeviceID, @{Name='Size(GB)';Expression={[math]::Round($_.Size/1GB,2)}}, @{Name='FreeSpace(GB)';Expression={[math]::Round($_.FreeSpace/1GB,2)}}, @{Name='%Free';Expression={[math]::Round(($_.FreeSpace/$_.Size)*100,2)}} | Format-Table -AutoSize"

echo.
echo ========================================
echo Disk cleanup completed!
echo ========================================
