#!/usr/bin/env python3
"""
PC Troubleshooter - Simplified APPX Builder
Creates APPX package structure without requiring Windows SDK
"""

import os
import sys
import shutil
import json
import subprocess
from pathlib import Path
from datetime import datetime

class SimpleAppxBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.appx_dir = self.project_root / "appx_package"
        self.app_name = "PC Troubleshooter"
        self.package_name = "PCTroubleshooter"
        self.publisher = "CN=PC Troubleshooter Team"
        self.version = "1.0.0.0"
        self.display_name = "PC Troubleshooter"
        
    def clean_build_dir(self):
        """Clean previous APPX build directory"""
        print("🧹 Cleaning previous APPX build directory...")
        if self.appx_dir.exists():
            shutil.rmtree(self.appx_dir)
            print(f"   Removed: {self.appx_dir}")
        self.appx_dir.mkdir(parents=True)
        print(f"   Created: {self.appx_dir}")
    
    def create_app_structure(self):
        """Create the APPX application structure"""
        print("📁 Creating APPX application structure...")
        
        # Create necessary directories
        directories = [
            "Images",
            "App",
        ]
        
        for dir_path in directories:
            (self.appx_dir / dir_path).mkdir(parents=True, exist_ok=True)
        
        print("   ✅ Directory structure created")
    
    def copy_application_files(self):
        """Copy application files to APPX structure"""
        print("📋 Copying application files...")
        
        app_dir = self.appx_dir / "App"
        
        # Copy Python files
        files_to_copy = [
            "main.py",
            "config.ini",
            "requirements.txt",
            "README.md",
        ]
        
        for file_name in files_to_copy:
            file_path = self.project_root / file_name
            if file_path.exists():
                shutil.copy2(file_path, app_dir)
                print(f"   Copied: {file_name}")
        
        # Copy directories
        dirs_to_copy = ["ui", "scripts", "docs", "assets"]
        for dir_name in dirs_to_copy:
            dir_path = self.project_root / dir_name
            if dir_path.exists():
                shutil.copytree(dir_path, app_dir / dir_name, dirs_exist_ok=True)
                print(f"   Copied directory: {dir_name}")
        
        # Copy the built executable if it exists
        exe_path = self.project_root / "dist" / "PC_Troubleshooter.exe"
        if exe_path.exists():
            shutil.copy2(exe_path, app_dir / "PC_Troubleshooter.exe")
            print(f"   Copied: PC_Troubleshooter.exe")
        
        print("   ✅ Application files copied")
    
    def create_app_icons(self):
        """Create APPX icons from the existing ICO file"""
        print("🎨 Creating APPX icons...")
        
        try:
            from PIL import Image
            
            source_icon = self.project_root / "assets" / "icon.ico"
            images_dir = self.appx_dir / "Images"
            
            if not source_icon.exists():
                print(f"   ⚠️ Source icon not found: {source_icon}")
                return False
            
            # APPX required icon sizes
            icon_sizes = {
                "Square44x44Logo.png": (44, 44),
                "Square150x150Logo.png": (150, 150),
                "StoreLogo.png": (50, 50),
                "Wide310x150Logo.png": (310, 150),
                "LargeTile.png": (310, 310),
                "SmallTile.png": (71, 71),
            }
            
            # Load the ICO file
            img = Image.open(source_icon)
            
            # If it's an ICO with multiple sizes, use the largest
            if hasattr(img, 'size'):
                # Find the largest size in the ICO
                try:
                    sizes_available = []
                    for i in range(100):  # Try up to 100 frames
                        try:
                            img.seek(i)
                            sizes_available.append((img.size, i))
                        except EOFError:
                            break
                    
                    if sizes_available:
                        # Use the largest size
                        largest_size, frame_index = max(sizes_available, key=lambda x: x[0][0] * x[0][1])
                        img.seek(frame_index)
                        print(f"   Using ICO frame {frame_index} with size {largest_size}")
                except:
                    # If seeking fails, use the default frame
                    pass
            
            for icon_name, size in icon_sizes.items():
                if icon_name == "Wide310x150Logo.png":
                    # Create wide logo with padding
                    wide_img = Image.new('RGBA', size, (0, 0, 0, 0))
                    # Resize original to fit height
                    resized = img.resize((150, 150), Image.Resampling.LANCZOS)
                    # Center it
                    wide_img.paste(resized, (80, 0))
                    wide_img.save(images_dir / icon_name, "PNG")
                else:
                    resized_img = img.resize(size, Image.Resampling.LANCZOS)
                    resized_img.save(images_dir / icon_name, "PNG")
                
                print(f"   Created: {icon_name} ({size[0]}x{size[1]})")
            
            print("   ✅ APPX icons created successfully")
            return True
            
        except ImportError:
            print("   📥 Installing Pillow for icon processing...")
            subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"], check=True)
            return self.create_app_icons()  # Retry after installation
        except Exception as e:
            print(f"   ❌ Icon creation failed: {e}")
            return False
    
    def create_app_manifest(self):
        """Create the AppxManifest.xml file"""
        print("📄 Creating AppxManifest.xml...")
        
        manifest_content = f'''<?xml version="1.0" encoding="utf-8"?>
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
  xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
  xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities">

  <Identity
    Name="{self.package_name}"
    Publisher="{self.publisher}"
    Version="{self.version}" />

  <Properties>
    <DisplayName>{self.display_name}</DisplayName>
    <PublisherDisplayName>PC Troubleshooter Team</PublisherDisplayName>
    <Logo>Images\\StoreLogo.png</Logo>
    <Description>Professional Windows System Diagnostic and Repair Tool</Description>
  </Properties>

  <Dependencies>
    <TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.17763.0" MaxVersionTested="10.0.22000.0" />
  </Dependencies>

  <Resources>
    <Resource Language="x-generate"/>
  </Resources>

  <Applications>
    <Application Id="App"
      Executable="App\\PC_Troubleshooter.exe"
      EntryPoint="Windows.FullTrustApplication">
      <uap:VisualElements
        DisplayName="{self.display_name}"
        Description="Professional Windows System Diagnostic and Repair Tool"
        BackgroundColor="transparent"
        Square150x150Logo="Images\\Square150x150Logo.png"
        Square44x44Logo="Images\\Square44x44Logo.png">
        <uap:DefaultTile Wide310x150Logo="Images\\Wide310x150Logo.png" />
        <uap:SplashScreen Image="Images\\Square150x150Logo.png" />
      </uap:VisualElements>
    </Application>
  </Applications>

  <Capabilities>
    <rescap:Capability Name="runFullTrust" />
    <Capability Name="internetClient" />
    <Capability Name="privateNetworkClientServer" />
  </Capabilities>
</Package>'''
        
        manifest_path = self.appx_dir / "AppxManifest.xml"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(manifest_content)
        
        print(f"   ✅ Manifest created: {manifest_path}")
        return manifest_path
    
    def create_installation_guide(self):
        """Create installation guide for the APPX package"""
        guide_content = f'''# PC Troubleshooter APPX Installation Guide

## APPX Package Structure

The APPX package has been created in the `appx_package` folder. This contains all the necessary files for a Windows APPX package.

## Installation Methods

### Method 1: Using PowerShell (Recommended)

1. **Copy the entire `appx_package` folder** to your target location
2. **Open PowerShell as Administrator**
3. **Navigate to the parent directory** of the appx_package folder
4. **Run the installation command**:
   ```powershell
   Add-AppxPackage -Register "appx_package\\AppxManifest.xml"
   ```

### Method 2: Create APPX file (Requires Windows SDK)

If you have Windows SDK installed:

1. **Install Windows 10/11 SDK** from Microsoft
2. **Use MakeAppx.exe** to create the APPX file:
   ```cmd
   "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.22621.0\\x64\\makeappx.exe" pack /d appx_package /p PCTroubleshooter.appx
   ```
3. **Install the APPX file**:
   ```powershell
   Add-AppxPackage -Path "PCTroubleshooter.appx"
   ```

### Method 3: Developer Mode Installation

1. **Enable Developer Mode**:
   - Open Settings → Update & Security → For developers
   - Select "Developer mode"
   - Confirm the change

2. **Register the app directly**:
   ```powershell
   Add-AppxPackage -Register "appx_package\\AppxManifest.xml"
   ```

## Package Contents

- **App folder**: Contains the PC Troubleshooter executable and all dependencies
- **Images folder**: Contains all required APPX icons
- **AppxManifest.xml**: Package manifest file

## Uninstallation

### Using Settings:
1. Open Settings → Apps
2. Find "PC Troubleshooter"
3. Click "Uninstall"

### Using PowerShell:
```powershell
Remove-AppxPackage -Package "{self.package_name}_1.0.0.0_x64__8wekyb3d8bbwe"
```

## Troubleshooting

- **Installation fails**: Ensure Developer Mode is enabled or run as Administrator
- **App won't start**: The executable should be self-contained
- **Permission errors**: Run installation commands as Administrator

## Notes

- This is an unsigned APPX package for testing/sideloading
- For Microsoft Store distribution, the package needs to be signed with a certificate
- The executable is self-contained and doesn't require Python installation
'''
        
        guide_path = self.project_root / "releases" / "APPX_Installation_Guide.md"
        guide_path.parent.mkdir(exist_ok=True)
        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(guide_content)
        
        print(f"   ✅ Installation guide created: {guide_path}")
    
    def create_appx_installer_script(self):
        """Create a PowerShell script to install the APPX package"""
        installer_script = f'''# PC Troubleshooter APPX Installer
# Run this script as Administrator

Write-Host "PC Troubleshooter APPX Installer" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
$isAdmin = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {{
    Write-Host "❌ This script must be run as Administrator" -ForegroundColor Red
    Write-Host "Right-click on PowerShell and select 'Run as Administrator'" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}}

Write-Host "✅ Running as Administrator" -ForegroundColor Green

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$appxDir = Join-Path $scriptDir "appx_package"
$manifestPath = Join-Path $appxDir "AppxManifest.xml"

# Check if APPX package exists
if (-not (Test-Path $manifestPath)) {{
    Write-Host "❌ APPX package not found at: $manifestPath" -ForegroundColor Red
    Write-Host "Please ensure the appx_package folder is in the same directory as this script" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}}

Write-Host "📦 Found APPX package: $appxDir" -ForegroundColor Green

try {{
    Write-Host "🚀 Installing PC Troubleshooter..." -ForegroundColor Yellow
    
    # Register the APPX package
    Add-AppxPackage -Register $manifestPath -ForceApplicationShutdown
    
    Write-Host "✅ PC Troubleshooter installed successfully!" -ForegroundColor Green
    Write-Host "You can now find it in the Start Menu" -ForegroundColor Green
    
}} catch {{
    Write-Host "❌ Installation failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Try enabling Developer Mode in Windows Settings" -ForegroundColor Yellow
}}

Write-Host ""
Read-Host "Press Enter to exit"
'''
        
        installer_path = self.appx_dir.parent / "Install_APPX.ps1"
        with open(installer_path, 'w', encoding='utf-8') as f:
            f.write(installer_script)
        
        print(f"   ✅ APPX installer script created: {installer_path}")
    
    def build(self):
        """Main build process for APPX package"""
        print("🚀 Starting PC Troubleshooter Simplified APPX Build Process")
        print("=" * 60)
        
        try:
            # Clean build directory
            self.clean_build_dir()
            
            # Create app structure
            self.create_app_structure()
            
            # Copy application files
            self.copy_application_files()
            
            # Create icons
            icon_success = self.create_app_icons()
            if not icon_success:
                print("   ⚠️ Continuing without proper icons")
            
            # Create manifest
            self.create_app_manifest()
            
            # Create installation guide and scripts
            self.create_installation_guide()
            self.create_appx_installer_script()
            
            print("=" * 60)
            print("✅ APPX PACKAGE STRUCTURE CREATED SUCCESSFULLY!")
            print(f"📦 APPX Package Folder: {self.appx_dir}")
            print(f"🔧 PowerShell Installer: {self.appx_dir.parent / 'Install_APPX.ps1'}")
            print("📖 Installation Guide: releases/APPX_Installation_Guide.md")
            print("=" * 60)
            
            return {
                'appx_dir': self.appx_dir,
                'success': True
            }
                
        except Exception as e:
            print(f"❌ Build process failed: {e}")
            return {'success': False, 'error': str(e)}

if __name__ == "__main__":
    builder = SimpleAppxBuilder()
    result = builder.build()
    
    if result.get('success'):
        print("\n🎉 Your PC Troubleshooter APPX package structure is ready!")
        print("Use the Install_APPX.ps1 script to install the application.")
    else:
        print("\n💥 APPX build failed. Please check the error messages above.")
        sys.exit(1)
