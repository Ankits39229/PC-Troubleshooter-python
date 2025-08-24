@echo off
echo ========================================
echo    Performance Monitor Tool
echo ========================================
echo.

echo [INFO] Current system performance overview...
echo.

echo [CPU USAGE]
powershell -Command "Get-Counter '\Processor(_Total)\% Processor Time' | Select-Object -ExpandProperty CounterSamples | Select-Object @{Name='CPU Usage %';Expression={[math]::Round($_.CookedValue,2)}} | Format-Table -AutoSize"

echo.
echo [MEMORY USAGE]
powershell -Command "Get-Counter '\Memory\Available MBytes' | Select-Object -ExpandProperty CounterSamples | Select-Object @{Name='Available Memory (MB)';Expression={$_.CookedValue}} | Format-Table -AutoSize"

echo.
echo [DISK USAGE]
powershell -Command "Get-Counter '\LogicalDisk(_Total)\% Disk Time' | Select-Object -ExpandProperty CounterSamples | Select-Object @{Name='Disk Usage %';Expression={[math]::Round($_.CookedValue,2)}} | Format-Table -AutoSize"

echo.
echo [NETWORK USAGE]
powershell -Command "Get-Counter '\Network Interface(*)\Bytes Total/sec' | Select-Object -ExpandProperty CounterSamples | Where-Object {$_.InstanceName -notlike '*isatap*' -and $_.InstanceName -notlike '*loopback*'} | Select-Object InstanceName, @{Name='Bytes/sec';Expression={[math]::Round($_.CookedValue,2)}} | Format-Table -AutoSize"

echo.
echo [INFO] Top CPU consuming processes...
powershell -Command "Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 | Select-Object ProcessName, @{Name='CPU Time';Expression={$_.CPU}}, @{Name='Memory(MB)';Expression={[math]::Round($_.WorkingSet/1MB,2)}} | Format-Table -AutoSize"

echo.
echo [INFO] System uptime...
powershell -Command "Get-WmiObject -Class Win32_OperatingSystem | Select-Object @{Name='System Uptime';Expression={(Get-Date) - $_.ConvertToDateTime($_.LastBootUpTime)}} | Format-Table -AutoSize"

echo.
echo [INFO] Performance alerts...
powershell -Command "$cpu = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue; $mem = (Get-WmiObject Win32_OperatingSystem); $memUsed = (($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / $mem.TotalVisibleMemorySize) * 100; if ($cpu -gt 80) { Write-Host 'HIGH CPU USAGE: ' $cpu '%' -ForegroundColor Red }; if ($memUsed -gt 85) { Write-Host 'HIGH MEMORY USAGE: ' $memUsed '%' -ForegroundColor Red }; if ($cpu -lt 80 -and $memUsed -lt 85) { Write-Host 'System performance is normal' -ForegroundColor Green }"

echo.
echo [INFO] Windows Experience Index (if available)...
powershell -Command "if (Test-Path 'C:\Windows\Performance\WinSAT\DataStore\') { Get-ChildItem 'C:\Windows\Performance\WinSAT\DataStore\' -Filter '*Formal*' | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | ForEach-Object { [xml]$winsat = Get-Content $_.FullName; Write-Host 'WEI Score:' $winsat.WinSAT.WinSPR.SystemScore } }"

echo.
echo ========================================
echo Performance monitoring completed!
echo ========================================
