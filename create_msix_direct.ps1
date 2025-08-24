# PC Troubleshooter - Direct MSIX Creation Script
# Creates MSIX file without Windows SDK using PowerShell

Write-Host "🚀 PC Troubleshooter - Direct MSIX Creation" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Check if MSIX build directory exists
$msixBuildDir = "msix_build"
if (-not (Test-Path $msixBuildDir)) {
    Write-Host "❌ MSIX build directory not found: $msixBuildDir" -ForegroundColor Red
    Write-Host "Please run 'python build_msix.py' first to create the package structure" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Found MSIX package structure: $msixBuildDir" -ForegroundColor Green

# Create releases directory
$releasesDir = "releases"
if (-not (Test-Path $releasesDir)) {
    New-Item -ItemType Directory -Path $releasesDir | Out-Null
}

# Method 1: Try to find Windows SDK
Write-Host "🔍 Searching for Windows SDK..." -ForegroundColor Yellow

$possiblePaths = @(
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\makeappx.exe",
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x64\makeappx.exe",
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\makeappx.exe",
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.18362.0\x64\makeappx.exe",
    "C:\Program Files (x86)\Windows Kits\10\bin\10.0.17763.0\x64\makeappx.exe"
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
    # Method 1: Use Windows SDK
    Write-Host "📦 Creating MSIX file using Windows SDK..." -ForegroundColor Yellow
    
    $outputFile = Join-Path $releasesDir "PCTroubleshooter_v1.0.0.msix"
    
    $arguments = @(
        "pack",
        "/d", $msixBuildDir,
        "/p", $outputFile,
        "/o"
    )
    
    try {
        & $makeappxPath $arguments
        
        if (Test-Path $outputFile) {
            $fileSize = [Math]::Round((Get-Item $outputFile).Length / 1MB, 1)
            Write-Host "✅ MSIX file created successfully!" -ForegroundColor Green
            Write-Host "📁 Location: $outputFile" -ForegroundColor Green
            Write-Host "📊 Size: $fileSize MB" -ForegroundColor Green
            
            Write-Host ""
            Write-Host "🎯 For Microsoft Store submission:" -ForegroundColor Cyan
            Write-Host "   Installer parameters: 'Installer runs in silent mode but does not require switches'" -ForegroundColor White
            Write-Host ""
            Write-Host "🧪 Test installation command:" -ForegroundColor Cyan
            Write-Host "   Add-AppxPackage -Path '$outputFile'" -ForegroundColor White
        } else {
            Write-Host "❌ MSIX file creation failed" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ Error creating MSIX: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    # Method 2: Create ZIP package for manual conversion
    Write-Host "⚠️ Windows SDK not found" -ForegroundColor Yellow
    Write-Host "📦 Creating ZIP package for manual MSIX conversion..." -ForegroundColor Yellow
    
    $zipFile = Join-Path $releasesDir "PCTroubleshooter_MSIX_Package.zip"
    
    try {
        # Remove existing ZIP if it exists
        if (Test-Path $zipFile) {
            Remove-Item $zipFile -Force
        }
        
        # Create ZIP file
        Compress-Archive -Path "$msixBuildDir\*" -DestinationPath $zipFile -Force
        
        $fileSize = [Math]::Round((Get-Item $zipFile).Length / 1MB, 1)
        Write-Host "✅ ZIP package created successfully!" -ForegroundColor Green
        Write-Host "📁 Location: $zipFile" -ForegroundColor Green
        Write-Host "📊 Size: $fileSize MB" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "🎯 Next Steps:" -ForegroundColor Cyan
        Write-Host "   1. Upload this ZIP to Microsoft Partner Center" -ForegroundColor White
        Write-Host "   2. Or rename to .msix and try installation" -ForegroundColor White
        Write-Host "   3. Or install Windows SDK to create proper MSIX" -ForegroundColor White
        
    } catch {
        Write-Host "❌ Error creating ZIP: $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Method 3: Create PowerShell installation script
Write-Host ""
Write-Host "📝 Creating installation scripts..." -ForegroundColor Yellow

$installScript = @"
# PC Troubleshooter MSIX Installation Script
Write-Host "Installing PC Troubleshooter..." -ForegroundColor Green

try {
    Add-AppxPackage -Register "msix_build\AppxManifest.xml" -ForceApplicationShutdown
    Write-Host "✅ PC Troubleshooter installed successfully!" -ForegroundColor Green
    Write-Host "Find it in your Start Menu" -ForegroundColor White
} catch {
    Write-Host "❌ Installation failed: `$(`$_.Exception.Message)" -ForegroundColor Red
    Write-Host "Try running as Administrator" -ForegroundColor Yellow
}

Read-Host "Press Enter to exit"
"@

$installScriptPath = "Install_PC_Troubleshooter.ps1"
$installScript | Out-File -FilePath $installScriptPath -Encoding UTF8

Write-Host "✅ Created installation script: $installScriptPath" -ForegroundColor Green

# Method 4: Alternative MSIX creation using 7-Zip (if available)
$sevenZipPath = Get-Command "7z.exe" -ErrorAction SilentlyContinue
if ($sevenZipPath) {
    Write-Host ""
    Write-Host "🔧 Creating MSIX using 7-Zip..." -ForegroundColor Yellow
    
    $msixFile7z = Join-Path $releasesDir "PCTroubleshooter_v1.0.0_7z.msix"
    
    try {
        & "7z.exe" a -tzip "$msixFile7z" "$msixBuildDir\*" -mx=9
        
        if (Test-Path $msixFile7z) {
            $fileSize = [Math]::Round((Get-Item $msixFile7z).Length / 1MB, 1)
            Write-Host "✅ MSIX created with 7-Zip!" -ForegroundColor Green
            Write-Host "📁 Location: $msixFile7z" -ForegroundColor Green
            Write-Host "📊 Size: $fileSize MB" -ForegroundColor Green
        }
    } catch {
        Write-Host "⚠️ 7-Zip method failed: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "🎉 MSIX Creation Process Complete!" -ForegroundColor Green
Write-Host "Check the 'releases' folder for your packages" -ForegroundColor White

Read-Host "Press Enter to exit"
