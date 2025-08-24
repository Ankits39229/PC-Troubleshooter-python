# Test PC Troubleshooter MSIX Installation

Write-Host "🧪 Testing PC Troubleshooter MSIX Installation" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan

$msixFile = "releases\PCTroubleshooter_v1.0.0.msix"

if (Test-Path $msixFile) {
    Write-Host "✅ Found MSIX file: $msixFile" -ForegroundColor Green
    
    $fileSize = [Math]::Round((Get-Item $msixFile).Length / 1MB, 1)
    Write-Host "📊 File size: $fileSize MB" -ForegroundColor Yellow
    
    Write-Host ""
    Write-Host "🚀 Installation commands:" -ForegroundColor Cyan
    Write-Host "Add-AppxPackage -Path '$msixFile'" -ForegroundColor White
    Write-Host ""
    Write-Host "📋 For Microsoft Store certification:" -ForegroundColor Cyan
    Write-Host "Installer parameters: 'Installer runs in silent mode but does not require switches'" -ForegroundColor White
    
} else {
    Write-Host "❌ MSIX file not found" -ForegroundColor Red
}

Read-Host "Press Enter to continue"
