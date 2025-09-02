@echo off
echo ========================================
echo    Memory Usage Check Tool
echo ========================================
echo.

echo [INFO] Current memory usage overview...
powershell -Command "Get-WmiObject -Class Win32_OperatingSystem | Select-Object @{Name='Total RAM (GB)';Expression={[math]::Round($_.TotalVisibleMemorySize/1MB,2)}}, @{Name='Available RAM (GB)';Expression={[math]::Round($_.FreePhysicalMemory/1MB,2)}}, @{Name='Used RAM (GB)';Expression={[math]::Round(($_.TotalVisibleMemorySize-$_.FreePhysicalMemory)/1MB,2)}}, @{Name='Memory Usage %%';Expression={[math]::Round((($_.TotalVisibleMemorySize-$_.FreePhysicalMemory)/$_.TotalVisibleMemorySize)*100,2)}} | Format-Table -AutoSize"

echo.
echo [INFO] Top memory-consuming processes...
powershell -Command "Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 | Select-Object ProcessName, @{Name='Memory(MB)';Expression={[math]::Round($_.WorkingSet/1MB,2)}}, Id, CPU | Format-Table -AutoSize"

echo.
echo [INFO] System memory details...
powershell -Command "Get-WmiObject -Class Win32_PhysicalMemory | Select-Object BankLabel, Capacity, Speed, Manufacturer | Format-Table -AutoSize"

echo.
echo [INFO] Virtual memory (pagefile) usage...
powershell -Command "Get-WmiObject -Class Win32_PageFileUsage | Select-Object Name, @{Name='Size(MB)';Expression={$_.AllocatedBaseSize}}, @{Name='Used(MB)';Expression={$_.CurrentUsage}}, @{Name='Peak(MB)';Expression={$_.PeakUsage}} | Format-Table -AutoSize"

echo.
echo [INFO] Memory performance counters...
powershell -Command "Get-Counter '\Memory\Available MBytes', '\Memory\Pages/sec', '\Memory\Page Faults/sec' | Select-Object -ExpandProperty CounterSamples | Select-Object Path, CookedValue | Format-Table -AutoSize"

echo.
echo [INFO] Checking for memory leaks (high handle/thread count)...
powershell -Command "Get-Process | Where-Object {$_.Handles -gt 1000 -or $_.Threads.Count -gt 50} | Sort-Object Handles -Descending | Select-Object ProcessName, Handles, @{Name='Threads';Expression={$_.Threads.Count}}, @{Name='Memory(MB)';Expression={[math]::Round($_.WorkingSet/1MB,2)}} | Format-Table -AutoSize"

echo.
echo ========================================
echo Memory usage check completed!
echo ========================================
