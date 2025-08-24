@echo off
echo ========================================
echo    Disk Space Check Tool
echo ========================================
echo.

echo [INFO] Checking disk space on all drives...
powershell -Command "Get-WmiObject -Class Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3} | Select-Object DeviceID, @{Name='Size(GB)';Expression={[math]::Round($_.Size/1GB,2)}}, @{Name='Used(GB)';Expression={[math]::Round(($_.Size-$_.FreeSpace)/1GB,2)}}, @{Name='Free(GB)';Expression={[math]::Round($_.FreeSpace/1GB,2)}}, @{Name='%Free';Expression={[math]::Round(($_.FreeSpace/$_.Size)*100,2)}} | Format-Table -AutoSize"

echo.
echo [INFO] Checking largest files and folders on C: drive...
powershell -Command "Get-ChildItem C:\ -Directory | ForEach-Object { $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum; [PSCustomObject]@{Folder=$_.Name; 'Size(MB)'=[math]::Round($size/1MB,2)} } | Sort-Object 'Size(MB)' -Descending | Select-Object -First 10 | Format-Table -AutoSize"

echo.
echo [INFO] Checking disk fragmentation...
powershell -Command "Get-WmiObject -Class Win32_Volume | Where-Object {$_.DriveLetter -ne $null} | Select-Object DriveLetter, Label, @{Name='Capacity(GB)';Expression={[math]::Round($_.Capacity/1GB,2)}}, @{Name='FreeSpace(GB)';Expression={[math]::Round($_.FreeSpace/1GB,2)}} | Format-Table -AutoSize"

echo.
echo [INFO] Checking for low disk space warnings...
powershell -Command "Get-WmiObject -Class Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3 -and ($_.FreeSpace/$_.Size)*100 -lt 15} | ForEach-Object { Write-Host 'WARNING: Drive' $_.DeviceID 'is running low on space (' ([math]::Round(($_.FreeSpace/$_.Size)*100,2)) '% free)' -ForegroundColor Red }"

echo.
echo [INFO] Recent large files (last 7 days):
powershell -Command "Get-ChildItem C:\Users\$env:USERNAME -Recurse -File -ErrorAction SilentlyContinue | Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-7) -and $_.Length -gt 100MB} | Sort-Object Length -Descending | Select-Object -First 5 | Select-Object Name, @{Name='Size(MB)';Expression={[math]::Round($_.Length/1MB,2)}}, LastWriteTime | Format-Table -AutoSize"

echo.
echo ========================================
echo Disk space check completed!
echo ========================================
