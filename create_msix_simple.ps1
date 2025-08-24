# PC Troubleshooter - Direct MSIX Creation Script

Write-Host "🚀 PC Troubleshooter - Direct MSIX Creation" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Check if MSIX build directory exists
$msixBuildDir = "msix_build"
if (-not (Test-Path $msixBuildDir)) {
    Write-Host "❌ MSIX build directory not found: $msixBuildDir" -ForegroundColor Red
    Write-Host "Please run 'python build_msix.py' first" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Found MSIX package structure: $msixBuildDir" -ForegroundColor Green

# Create releases directory
$releasesDir = "releases"
if (-not (Test-Path $releasesDir)) {
    New-Item -ItemType Directory -Path $releasesDir | Out-Null
}

# Try to find Windows SDK
Write-Host "🔍 Searching for Windows SDK..." -ForegroundColor Yellow

$possiblePaths = @(
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\makeappx.exe",
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\makeappx.exe",
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\makeappx.exe"
)

$makeappxPath = $null
foreach ($path in $possiblePaths) {
    if (Test-Path $path) {
        $makeappxPath = $path
        Write-Host "✅ Found Windows SDK: $path" -ForegroundColor Green
        break
    }
}

if ($makeappxPath) {
    # Use Windows SDK
    Write-Host "📦 Creating MSIX file using Windows SDK..." -ForegroundColor Yellow
    
    $outputFile = Join-Path $releasesDir "PCTroubleshooter_v1.0.0.msix"
    
    try {
        & $makeappxPath pack /d $msixBuildDir /p $outputFile /o
        
        if (Test-Path $outputFile) {
            $fileSize = [Math]::Round((Get-Item $outputFile).Length / 1MB, 1)
            Write-Host "✅ MSIX file created successfully!" -ForegroundColor Green
            Write-Host "📁 Location: $outputFile" -ForegroundColor Green
            Write-Host "📊 Size: $fileSize MB" -ForegroundColor Green
        } else {
            Write-Host "❌ MSIX file creation failed" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ Error creating MSIX: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    # Create ZIP package
    Write-Host "⚠️ Windows SDK not found" -ForegroundColor Yellow
    Write-Host "📦 Creating ZIP package for manual conversion..." -ForegroundColor Yellow
    
    $zipFile = Join-Path $releasesDir "PCTroubleshooter_MSIX_Package.zip"
    
    try {
        if (Test-Path $zipFile) {
            Remove-Item $zipFile -Force
        }
        
        Compress-Archive -Path "$msixBuildDir\*" -DestinationPath $zipFile -Force
        
        $fileSize = [Math]::Round((Get-Item $zipFile).Length / 1MB, 1)
        Write-Host "✅ ZIP package created successfully!" -ForegroundColor Green
        Write-Host "📁 Location: $zipFile" -ForegroundColor Green
        Write-Host "📊 Size: $fileSize MB" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "🎯 Options:" -ForegroundColor Cyan
        Write-Host "   1. Upload ZIP to Microsoft Partner Center" -ForegroundColor White
        Write-Host "   2. Rename .zip to .msix and try installation" -ForegroundColor White
        
    } catch {
        Write-Host "❌ Error creating ZIP: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🎉 Process Complete!" -ForegroundColor Green
Read-Host "Press Enter to exit"
