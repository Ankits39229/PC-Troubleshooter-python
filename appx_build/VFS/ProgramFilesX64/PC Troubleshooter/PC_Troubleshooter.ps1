# PC Troubleshooter Launcher
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath
python main.py
