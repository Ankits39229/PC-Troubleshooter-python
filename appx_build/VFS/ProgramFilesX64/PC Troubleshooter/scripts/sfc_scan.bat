@echo off
echo ========================================
echo    System File Checker (SFC) Tool
echo ========================================
echo.

echo [INFO] Running System File Checker...
echo [INFO] This may take several minutes. Please wait...
echo.

sfc /scannow

echo.
echo [INFO] SFC scan completed. Checking results...

:: Check if CBS.log exists and show recent entries
if exist "C:\Windows\Logs\CBS\CBS.log" (
    echo.
    echo [INFO] Recent SFC log entries:
    powershell -Command "Get-Content 'C:\Windows\Logs\CBS\CBS.log' | Select-String 'SFC' | Select-Object -Last 10"
)

echo.
echo [INFO] Running DISM health check...
dism /online /cleanup-image /checkhealth

echo.
echo [INFO] If SFC found issues, you can run additional DISM commands:
echo   dism /online /cleanup-image /scanhealth
echo   dism /online /cleanup-image /restorehealth

echo.
echo [INFO] System file integrity status:
powershell -Command "if (Test-Path 'C:\Windows\Logs\CBS\CBS.log') { $sfcResults = Get-Content 'C:\Windows\Logs\CBS\CBS.log' | Select-String 'SFC' | Select-Object -Last 5; if ($sfcResults -match 'corrupt') { Write-Host 'CORRUPT FILES DETECTED - Run DISM repair' -ForegroundColor Red } else { Write-Host 'No corruption detected' -ForegroundColor Green } }"

echo.
echo ========================================
echo System File Checker scan completed!
echo Check the output above for any issues found.
echo ========================================
