@echo off
echo ========================================
echo    Audio Troubleshooter Tool
echo ========================================
echo.

echo [INFO] Running Windows built-in audio troubleshooter...
powershell -Command "Start-Process msdt.exe -ArgumentList '/id AudioPlaybackDiagnostic' -Wait"

echo.
echo [INFO] Checking audio enhancements...
powershell -Command "Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render\*\Properties\' | Where-Object {$_.PSChildName -like '*FxProperties*'}"

echo.
echo [INFO] Resetting audio enhancements...
powershell -Command "Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render\' | ForEach-Object { Remove-ItemProperty -Path ($_.PSPath + '\FxProperties') -Name * -ErrorAction SilentlyContinue }"

echo.
echo [INFO] Scanning for audio hardware changes...
powershell -Command "Get-PnpDevice | Where-Object {$_.Class -eq 'AudioEndpoint'} | ForEach-Object { Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false; Enable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false }"

echo.
echo ========================================
echo Audio troubleshooting completed!
echo ========================================
