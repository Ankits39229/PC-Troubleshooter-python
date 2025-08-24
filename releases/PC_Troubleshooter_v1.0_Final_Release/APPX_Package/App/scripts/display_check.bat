@echo off
echo ========================================
echo    Display Settings Check Tool
echo ========================================
echo.

echo [INFO] Current display configuration:
powershell -Command "Get-WmiObject -Class Win32_VideoController | Select-Object Name, VideoModeDescription, DriverVersion, DriverDate | Format-Table -AutoSize"

echo.
echo [INFO] Display adapters information:
powershell -Command "Get-WmiObject -Class Win32_DisplayConfiguration | Format-Table -AutoSize"

echo.
echo [INFO] Monitor information:
powershell -Command "Get-WmiObject -Class Win32_DesktopMonitor | Select-Object Name, ScreenHeight, ScreenWidth, MonitorType | Format-Table -AutoSize"

echo.
echo [INFO] Display resolution and refresh rate:
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Screen]::AllScreens | Select-Object DeviceName, Bounds, Primary | Format-Table -AutoSize"

echo.
echo [INFO] Graphics driver status:
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Display'} | Format-Table FriendlyName, Status -AutoSize"

echo.
echo ========================================
echo Display settings check completed!
echo ========================================
