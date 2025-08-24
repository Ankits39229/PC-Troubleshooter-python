# PC Troubleshooter APPX Installer
# Run this script as Administrator

Write-Host "PC Troubleshooter APPX Installer" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
$isAdmin = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "❌ This script must be run as Administrator" -ForegroundColor Red
    Write-Host "Right-click on PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Running as Administrator" -ForegroundColor Green

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$appxDir = Join-Path $scriptDir "appx_package"
$manifestPath = Join-Path $appxDir "AppxManifest.xml"

# Check if APPX package exists
if (-not (Test-Path $manifestPath)) {
    Write-Host "❌ APPX package not found at: $manifestPath" -ForegroundColor Red
    Write-Host "Please ensure the appx_package folder is in the same directory as this script" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "📦 Found APPX package: $appxDir" -ForegroundColor Green

try {
    Write-Host "🚀 Installing PC Troubleshooter..." -ForegroundColor Yellow
    
    # Register the APPX package
    Add-AppxPackage -Register $manifestPath -ForceApplicationShutdown
    
    Write-Host "✅ PC Troubleshooter installed successfully!" -ForegroundColor Green
    Write-Host "You can now find it in the Start Menu" -ForegroundColor Green
    
} catch {
    Write-Host "❌ Installation failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Try enabling Developer Mode in Windows Settings" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to exit"
