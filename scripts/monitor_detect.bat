@echo off
echo ========================================
echo    Monitor Detection Tool
echo ========================================
echo.

echo [INFO] Detecting all connected monitors...
powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Screen]::AllScreens | ForEach-Object { Write-Host 'Monitor:' $_.DeviceName 'Resolution:' $_.Bounds.Width 'x' $_.Bounds.Height 'Primary:' $_.Primary }"

echo.
echo [INFO] Forcing monitor detection...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'Monitor'} | ForEach-Object { Write-Host 'Detecting:' $_.FriendlyName; Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false; Start-Sleep -Seconds 1; Enable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false }"

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
