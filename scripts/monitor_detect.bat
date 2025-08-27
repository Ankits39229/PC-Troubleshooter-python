@echo off
echo ========================================
echo    Monitor Detection Tool
echo ========================================
echo.

:: Check for admin privileges (for potential monitor reset operations)
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [INFO] Running with administrator privileges.
) else (
    echo [WARNING] Administrator privileges may be required for advanced monitor operations.
    echo [INFO] This is needed for resetting monitor devices if that feature is enabled.
    echo [INFO] Relaunching as administrator...
    powershell "start-process cmd -argumentlist '/c %~f0' -verb runas"
    exit
)

echo [INFO] Detecting all connected monitors...
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Screen]::AllScreens | ForEach-Object { Write-Host 'Monitor:' $_.DeviceName 'Resolution:' $_.Bounds.Width 'x' $_.Bounds.Height 'Primary:' $_.Primary }"

echo.
echo [INFO] Forcing monitor detection...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Monitor'} | ForEach-Object { Write-Host 'Note: Skipping reset for' $_.FriendlyName '(requires admin privileges)' }"

echo.
echo [INFO] Monitor devices in Device Manager:
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Monitor'} | Format-Table FriendlyName, Status -AutoSize"

echo.
echo [INFO] Display configuration:
powershell -Command "Get-WmiObject -Class Win32_DesktopMonitor | Select-Object Name, ScreenHeight, ScreenWidth, MonitorType, MonitorManufacturer | Format-Table -AutoSize"

echo.
echo [INFO] Refreshing display settings...
powershell -Command "Start-Process rundll32.exe -ArgumentList 'user32.dll,UpdatePerUserSystemParameters' -Wait"

echo.
echo ========================================
echo Monitor detection completed!
echo ========================================

exit
