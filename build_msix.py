#!/usr/bin/env python3
"""
PC Troubleshooter - MSIX Build Script
Modern Microsoft Store package build system using MSIX format
"""

import os
import sys
import shutil
import subprocess
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

class MsixBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.msix_dir = self.project_root / "msix_build"
        self.app_name = "PC Troubleshooter"
        self.package_name = "PCTroubleshooter"
        self.publisher = "CN=PC Troubleshooter Team"
        self.version = "1.0.0.0"
        self.display_name = "PC Troubleshooter"
        self.package_family_name = f"{self.package_name}_8wekyb3d8bbwe"
        
    def clean_build_dir(self):
        """Clean previous MSIX build directory"""
        print("🧹 Cleaning previous MSIX build directory...")
        if self.msix_dir.exists():
            shutil.rmtree(self.msix_dir)
            print(f"   Removed: {self.msix_dir}")
        self.msix_dir.mkdir(parents=True)
        print(f"   Created: {self.msix_dir}")
    
    def create_app_structure(self):
        """Create the MSIX application structure"""
        print("📁 Creating MSIX application structure...")
        
        # Create necessary directories
        directories = [
            "Images",
            "VFS/ProgramFilesX64/PC Troubleshooter",
            "Assets",
        ]
        
        for dir_path in directories:
            (self.msix_dir / dir_path).mkdir(parents=True, exist_ok=True)
        
        print("   ✅ Directory structure created")
    
    def copy_application_files(self):
        """Copy application files to MSIX structure"""
        print("📋 Copying application files...")
        
        app_dir = self.msix_dir / "VFS/ProgramFilesX64/PC Troubleshooter"
        
        # Copy the built executable
        exe_path = self.project_root / "dist" / "PC_Troubleshooter.exe"
        if exe_path.exists():
            shutil.copy2(exe_path, app_dir / "PC_Troubleshooter.exe")
            print(f"   Copied: PC_Troubleshooter.exe ({exe_path.stat().st_size / (1024*1024):.1f} MB)")
        else:
            print(f"   ⚠️ EXE not found: {exe_path}")
            print("   Run build_exe.py first to create the executable")
            return False
        
        # Copy essential files
        files_to_copy = [
            "README.md",
            "config.ini",
        ]
        
        for file_name in files_to_copy:
            file_path = self.project_root / file_name
            if file_path.exists():
                shutil.copy2(file_path, app_dir)
                print(f"   Copied: {file_name}")
        
        # Copy directories
        dirs_to_copy = ["docs", "scripts"]
        for dir_name in dirs_to_copy:
            dir_path = self.project_root / dir_name
            if dir_path.exists():
                shutil.copytree(dir_path, app_dir / dir_name, dirs_exist_ok=True)
                print(f"   Copied directory: {dir_name}")
        
        print("   ✅ Application files copied")
        return True
    
    def create_msix_icons(self):
        """Create MSIX icons from the existing ICO file"""
        print("🎨 Creating MSIX icons...")
        
        try:
            from PIL import Image
            
            source_icon = self.project_root / "assets" / "icon.ico"
            images_dir = self.msix_dir / "Images"
            
            if not source_icon.exists():
                print(f"   ⚠️ Source icon not found: {source_icon}")
                return False
            
            # MSIX required icon sizes (updated for modern requirements)
            icon_sizes = {
                "Square44x44Logo.scale-200.png": (88, 88),
                "Square44x44Logo.targetsize-24_altform-unplated.png": (24, 24),
                "Square44x44Logo.targetsize-32_altform-unplated.png": (32, 32),
                "Square44x44Logo.targetsize-48_altform-unplated.png": (48, 48),
                "Square150x150Logo.scale-200.png": (300, 300),
                "StoreLogo.png": (50, 50),
                "StoreLogo.scale-200.png": (100, 100),
                "Wide310x150Logo.scale-200.png": (620, 300),
                "LargeTile.scale-200.png": (620, 620),
                "SmallTile.scale-200.png": (142, 142),
                "SplashScreen.scale-200.png": (1240, 600),
            }
            
            # Load the ICO file
            img = Image.open(source_icon)
            
            # If it's an ICO with multiple sizes, use the largest
            if hasattr(img, 'size'):
                try:
                    sizes_available = []
                    for i in range(100):
                        try:
                            img.seek(i)
                            sizes_available.append((img.size, i))
                        except EOFError:
                            break
                    
                    if sizes_available:
                        largest_size, frame_index = max(sizes_available, key=lambda x: x[0][0] * x[0][1])
                        img.seek(frame_index)
                        print(f"   Using ICO frame {frame_index} with size {largest_size}")
                except:
                    pass
            
            for icon_name, size in icon_sizes.items():
                if "Wide310x150Logo" in icon_name or "SplashScreen" in icon_name:
                    # Create wide/splash images with proper aspect ratio
                    if "Wide310x150Logo" in icon_name:
                        wide_img = Image.new('RGBA', size, (30, 30, 30, 255))  # Dark background
                        # Resize to fit height and center
                        icon_size = min(size[1], size[0] // 2)
                        resized = img.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
                        x_pos = (size[0] - icon_size) // 2
                        y_pos = (size[1] - icon_size) // 2
                        wide_img.paste(resized, (x_pos, y_pos), resized if resized.mode == 'RGBA' else None)
                    else:  # SplashScreen
                        splash_img = Image.new('RGBA', size, (30, 30, 30, 255))  # Dark background
                        # Center the icon
                        icon_size = min(size[1] // 2, size[0] // 4)
                        resized = img.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
                        x_pos = (size[0] - icon_size) // 2
                        y_pos = (size[1] - icon_size) // 2
                        splash_img.paste(resized, (x_pos, y_pos), resized if resized.mode == 'RGBA' else None)
                        wide_img = splash_img
                    
                    wide_img.save(images_dir / icon_name, "PNG")
                else:
                    # Regular square icons
                    resized_img = img.resize(size, Image.Resampling.LANCZOS)
                    resized_img.save(images_dir / icon_name, "PNG")
                
                print(f"   Created: {icon_name} ({size[0]}x{size[1]})")
            
            print("   ✅ MSIX icons created successfully")
            return True
            
        except ImportError:
            print("   📥 Installing Pillow for icon processing...")
            subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"], check=True)
            return self.create_msix_icons()  # Retry after installation
        except Exception as e:
            print(f"   ❌ Icon creation failed: {e}")
            return False
    
    def create_app_manifest(self):
        """Create the AppxManifest.xml file for MSIX"""
        print("📄 Creating AppxManifest.xml...")
        
        manifest_content = f'''<?xml version="1.0" encoding="utf-8"?>
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
  xmlns:mp="http://schemas.microsoft.com/appx/2014/phone/manifest"
  xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
  xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
  xmlns:iot="http://schemas.microsoft.com/appx/manifest/iot/windows10"
  xmlns:desktop="http://schemas.microsoft.com/appx/manifest/desktop/windows10">

  <Identity
    Name="{self.package_name}"
    Publisher="{self.publisher}"
    Version="{self.version}" />

  <mp:PhoneIdentity PhoneProductId="9f1bb572-d5ce-4043-8ac2-e1c47e1b8a5b" PhonePublisherId="00000000-0000-0000-0000-000000000000"/>

  <Properties>
    <DisplayName>{self.display_name}</DisplayName>
    <PublisherDisplayName>PC Troubleshooter Team</PublisherDisplayName>
    <Logo>Images\\StoreLogo.png</Logo>
    <Description>Professional Windows System Diagnostic and Repair Tool with 20+ automated diagnostic scripts across 6 categories.</Description>
  </Properties>

  <Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" MinVersion="10.0.17763.0" MaxVersionTested="10.0.22000.0" />
    <TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.17763.0" MaxVersionTested="10.0.22000.0" />
  </Dependencies>

  <Resources>
    <Resource Language="x-generate"/>
  </Resources>

  <Applications>
    <Application Id="App"
      Executable="VFS\\ProgramFilesX64\\PC Troubleshooter\\PC_Troubleshooter.exe"
      EntryPoint="Windows.FullTrustApplication">
      <uap:VisualElements
        DisplayName="{self.display_name}"
        Description="Professional Windows System Diagnostic and Repair Tool"
        BackgroundColor="transparent"
        Square150x150Logo="Images\\Square150x150Logo.scale-200.png"
        Square44x44Logo="Images\\Square44x44Logo.scale-200.png">
        <uap:DefaultTile 
          Wide310x150Logo="Images\\Wide310x150Logo.scale-200.png"
          Square71x71Logo="Images\\SmallTile.scale-200.png"
          Square310x310Logo="Images\\LargeTile.scale-200.png"
          ShortName="PC Troubleshooter">
          <uap:ShowNameOnTiles>
            <uap:ShowOn Tile="square150x150Logo"/>
            <uap:ShowOn Tile="wide310x150Logo"/>
            <uap:ShowOn Tile="square310x310Logo"/>
          </uap:ShowNameOnTiles>
        </uap:DefaultTile>
        <uap:SplashScreen Image="Images\\SplashScreen.scale-200.png" />
      </uap:VisualElements>
    </Application>
  </Applications>

  <Capabilities>
    <rescap:Capability Name="runFullTrust" />
    <Capability Name="internetClient" />
    <Capability Name="privateNetworkClientServer" />
  </Capabilities>
</Package>'''
        
        manifest_path = self.msix_dir / "AppxManifest.xml"
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(manifest_content)
        
        print(f"   ✅ Manifest created: {manifest_path}")
        return manifest_path
    
    def create_priconfig_xml(self):
        """Create priconfig.xml for resource indexing"""
        print("📄 Creating priconfig.xml...")
        
        priconfig_content = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<resources targetOsVersion="10.0.0" majorVersion="1">
  <index root="\" startIndexAt="\">
    <default>
      <qualifier name="Language" value="en-US" />
      <qualifier name="Contrast" value="standard" />
      <qualifier name="Scale" value="200" />
      <qualifier name="HomeRegion" value="001" />
      <qualifier name="TargetSize" value="256" />
      <qualifier name="LayoutDirection" value="LTR" />
      <qualifier name="Theme" value="dark" />
      <qualifier name="AlternateForm" value="" />
      <qualifier name="DXFeatureLevel" value="DX9" />
      <qualifier name="Configuration" value="" />
      <qualifier name="DeviceFamily" value="Universal" />
      <qualifier name="Custom" value="" />
    </default>
    <indexer-config type="folder" foldernameAsQualifier="true" filenameAsQualifier="true">
      <exclude>
        <files>
          <file>*.log</file>
          <file>*.tmp</file>
        </files>
      </exclude>
    </indexer-config>
  </index>
</resources>'''
        
        priconfig_path = self.msix_dir / "priconfig.xml"
        with open(priconfig_path, 'w', encoding='utf-8') as f:
            f.write(priconfig_content)
        
        print(f"   ✅ PRI config created: {priconfig_path}")
        return priconfig_path
    
    def build_msix_package(self):
        """Build the MSIX package using Windows SDK tools"""
        print("📦 Building MSIX package...")
        
        # Check for Windows SDK tools
        makemsix_path = self.find_makemsix_tool()
        if not makemsix_path:
            print("   ❌ Windows SDK MakeAppx.exe not found")
            print("   Please install Windows 10/11 SDK")
            return None
        
        output_dir = self.project_root / "releases"
        output_dir.mkdir(exist_ok=True)
        
        msix_file = output_dir / f"{self.package_name}_v{self.version.replace('.0', '')}.msix"
        
        # Build MSIX package
        cmd = [
            str(makemsix_path),
            "pack",
            "/d", str(self.msix_dir),
            "/p", str(msix_file),
            "/o"  # Overwrite existing
        ]
        
        print(f"   Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ MSIX package built successfully!")
            print(f"   📁 Package location: {msix_file}")
            print(f"   📊 Package size: {msix_file.stat().st_size / (1024*1024):.1f} MB")
            return msix_file
        else:
            print("   ❌ MSIX build failed!")
            print(f"   Error: {result.stderr}")
            print(f"   Output: {result.stdout}")
            return None
    
    def find_makemsix_tool(self):
        """Find MakeAppx.exe in Windows SDK (also works for MSIX)"""
        possible_paths = [
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.22621.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.22000.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.19041.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.18362.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.17763.0\\x64\\makeappx.exe",
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(f"   Found Windows SDK: {path}")
                return path
        
        # Try to find it in PATH
        try:
            result = subprocess.run(["where", "makeappx.exe"], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip().split('\n')[0]
        except:
            pass
        
        return None
    
    def create_installation_guide(self):
        """Create installation guide for the MSIX package"""
        guide_content = f'''# PC Troubleshooter MSIX Installation Guide

## Installation Methods

### Method 1: PowerShell Installation (Recommended)

1. **Open PowerShell as Administrator**
2. **Run the installation command**:
   ```powershell
   Add-AppxPackage -Path "{self.package_name}_v{self.version.replace('.0', '')}.msix"
   ```

### Method 2: App Installer (Windows 10 1709+)

1. **Double-click** the MSIX file
2. **Click "Install"** in the App Installer dialog
3. **Wait** for installation to complete

### Method 3: Microsoft Store for Business

1. **Upload** the MSIX to Store for Business
2. **Distribute** to devices via Intune or SCCM
3. **Install** automatically on managed devices

### Method 4: Developer Mode (For Testing)

1. **Enable Developer Mode**:
   - Open Settings → Update & Security → For developers
   - Select "Developer mode"
2. **Install the MSIX**:
   ```powershell
   Add-AppxPackage -Path "{self.package_name}_v{self.version.replace('.0', '')}.msix"
   ```

## MSIX Advantages

- **Automatic Updates**: Support for delta updates
- **Clean Uninstall**: Complete removal with no registry residue
- **Containerization**: Isolated execution environment
- **Modern Deployment**: Compatible with Intune, SCCM, Store
- **Security**: Package integrity verification

## Installer Parameters

For silent installation via command line:
```cmd
powershell -Command "Add-AppxPackage -Path 'PCTroubleshooter_v1.0.0.msix'"
```

## Uninstallation

### Using Settings:
1. Open Settings → Apps
2. Find "PC Troubleshooter"
3. Click "Uninstall"

### Using PowerShell:
```powershell
Remove-AppxPackage -Package "{self.package_name}_1.0.0.0_x64__8wekyb3d8bbwe"
```

### Get Package Information:
```powershell
Get-AppxPackage | Where-Object {{$_.Name -like "*PCTroubleshooter*"}}
```

## Troubleshooting

- **Installation fails**: Ensure running as Administrator
- **App won't start**: Check if package is properly signed
- **Permission errors**: Verify MSIX is not corrupted
- **Developer Mode issues**: Try App Installer method instead

## Enterprise Deployment

### SCCM Deployment:
1. Create Application in SCCM Console
2. Use PowerShell script for installation
3. Deploy to device collections

### Intune Deployment:
1. Upload MSIX to Intune
2. Create app assignment
3. Deploy to Azure AD groups

## Notes

- This MSIX package is self-contained
- No additional dependencies required
- Compatible with Windows 10 1709+ and Windows 11
- Supports x64 architecture only
'''
        
        guide_path = self.project_root / "releases" / "MSIX_Installation_Guide.md"
        guide_path.parent.mkdir(exist_ok=True)
        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(guide_content)
        
        print(f"   ✅ MSIX installation guide created: {guide_path}")
    
    def create_msix_installer_script(self):
        """Create a PowerShell script to install the MSIX package"""
        installer_script = f'''# PC Troubleshooter MSIX Installer
# Run this script as Administrator

Write-Host "PC Troubleshooter MSIX Installer" -ForegroundColor Cyan
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
$msixFile = Join-Path $scriptDir "{self.package_name}_v{self.version.replace('.0', '')}.msix"

# Check if MSIX package exists
if (-not (Test-Path $msixFile)) {{
    Write-Host "❌ MSIX package not found at: $msixFile" -ForegroundColor Red
    Write-Host "Please ensure the MSIX file is in the same directory as this script" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}}

Write-Host "📦 Found MSIX package: $msixFile" -ForegroundColor Green
$fileSize = [Math]::Round((Get-Item $msixFile).Length / 1MB, 1)
Write-Host "📊 Package size: $fileSize MB" -ForegroundColor Green

try {{
    Write-Host "🚀 Installing PC Troubleshooter..." -ForegroundColor Yellow
    
    # Install the MSIX package
    Add-AppxPackage -Path $msixFile -ForceApplicationShutdown
    
    Write-Host "✅ PC Troubleshooter installed successfully!" -ForegroundColor Green
    Write-Host "🎯 You can find it in the Start Menu" -ForegroundColor Green
    Write-Host "🎉 Installation completed!" -ForegroundColor Green
    
    # Show installed package info
    $installedApp = Get-AppxPackage | Where-Object {{$_.Name -like "*PCTroubleshooter*"}}
    if ($installedApp) {{
        Write-Host ""
        Write-Host "📋 Installed Package Details:" -ForegroundColor Cyan
        Write-Host "   Name: $($installedApp.Name)" -ForegroundColor White
        Write-Host "   Version: $($installedApp.Version)" -ForegroundColor White
        Write-Host "   Publisher: $($installedApp.Publisher)" -ForegroundColor White
    }}
    
}} catch {{
    Write-Host "❌ Installation failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "💡 Try the following solutions:" -ForegroundColor Yellow
    Write-Host "   1. Enable Developer Mode in Windows Settings" -ForegroundColor White
    Write-Host "   2. Ensure the MSIX file is not corrupted" -ForegroundColor White
    Write-Host "   3. Try running as Administrator" -ForegroundColor White
}}

Write-Host ""
Read-Host "Press Enter to exit"
'''
        
        installer_path = self.project_root / "releases" / "Install_MSIX.ps1"
        with open(installer_path, 'w', encoding='utf-8') as f:
            f.write(installer_script)
        
        print(f"   ✅ MSIX installer script created: {installer_path}")
    
    def build(self):
        """Main build process for MSIX package"""
        print("🚀 Starting PC Troubleshooter MSIX Build Process")
        print("=" * 60)
        
        try:
            # Clean build directory
            self.clean_build_dir()
            
            # Create app structure
            self.create_app_structure()
            
            # Copy application files
            if not self.copy_application_files():
                return {'success': False, 'error': 'Failed to copy application files'}
            
            # Create icons
            icon_success = self.create_msix_icons()
            if not icon_success:
                print("   ⚠️ Continuing without proper icons")
            
            # Create manifest and config files
            self.create_app_manifest()
            self.create_priconfig_xml()
            
            # Build MSIX package
            msix_file = self.build_msix_package()
            
            if msix_file:
                # Create installation guides and scripts
                self.create_installation_guide()
                self.create_msix_installer_script()
                
                print("=" * 60)
                print("✅ MSIX BUILD COMPLETED SUCCESSFULLY!")
                print(f"📦 MSIX Package: {msix_file}")
                print(f"🔧 PowerShell Installer: {self.project_root}/releases/Install_MSIX.ps1")
                print("📖 Installation Guide: releases/MSIX_Installation_Guide.md")
                print("=" * 60)
                
                return {
                    'msix_file': msix_file,
                    'success': True
                }
            else:
                print("❌ MSIX BUILD FAILED!")
                return {'success': False, 'error': 'Failed to build MSIX package'}
                
        except Exception as e:
            print(f"❌ Build process failed: {e}")
            return {'success': False, 'error': str(e)}

if __name__ == "__main__":
    builder = MsixBuilder()
    result = builder.build()
    
    if result.get('success'):
        print("\n🎉 Your PC Troubleshooter MSIX package is ready!")
        print("Use the Install_MSIX.ps1 script for installation.")
        print("\n📋 Silent Installation Command:")
        print('powershell -Command "Add-AppxPackage -Path \'PCTroubleshooter_v1.0.0.msix\'"')
    else:
        print("\n💥 MSIX build failed. Please check the error messages above.")
        sys.exit(1)
