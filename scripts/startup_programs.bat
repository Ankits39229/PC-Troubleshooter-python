@echo off
echo ========================================
echo    Startup Programs Analysis Tool
echo ========================================
echo.

echo [INFO] Listing startup programs from Registry...
echo.
echo [CURRENT USER STARTUP PROGRAMS]
reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" 2>nul
echo.

echo [ALL USERS STARTUP PROGRAMS]
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" 2>nul
echo.

echo [INFO] Startup programs from Startup folder...
echo.
echo [USER STARTUP FOLDER]
dir "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /b 2>nul
echo.

echo [ALL USERS STARTUP FOLDER]
dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup" /b 2>nul
echo.

echo [INFO] Analyzing startup impact using PowerShell...
powershell -Command "Get-CimInstance -ClassName Win32_StartupCommand | Select-Object Name, Command, Location, User | Format-Table -AutoSize"

echo.
echo [INFO] Windows 10/11 Startup Apps (if available)...
powershell -Command "if (Get-Command Get-StartApps -ErrorAction SilentlyContinue) { Get-StartApps | Where-Object {$_.StartupApproval -eq 'Enabled'} | Select-Object Name, StartupApproval | Format-Table -AutoSize }"

echo.
echo [INFO] Services set to start automatically...
powershell -Command "Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -eq 'Running'} | Select-Object Name, DisplayName, Status | Sort-Object DisplayName | Format-Table -AutoSize"

echo.
echo ========================================
echo Startup programs analysis completed!
echo Use msconfig or Task Manager to disable unwanted startup programs.
echo ========================================
