#!/usr/bin/env python3
"""
PC Troubleshooter - APPX Build Script
Professional Microsoft Store package build system
"""

import os
import sys
import shutil
import subprocess
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

class AppxBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.appx_dir = self.project_root / "appx_build"
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
            "VFS/ProgramFilesX64/PC Troubleshooter",
        ]
        
        for dir_path in directories:
            (self.appx_dir / dir_path).mkdir(parents=True, exist_ok=True)
        
        print("   ✅ Directory structure created")
    
    def copy_application_files(self):
        """Copy application files to APPX structure"""
        print("📋 Copying application files...")
        
        app_dir = self.appx_dir / "VFS/ProgramFilesX64/PC Troubleshooter"
        
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
        
        print("   ✅ Application files copied")
    
    def create_app_icons(self):
        """Create APPX icons from the existing icon"""
        print("🎨 Creating APPX icons...")
        
        try:
            from PIL import Image
            
            source_icon = self.project_root / "assets" / "icon.png"
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
            
            img = Image.open(source_icon)
            
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
      Executable="VFS\\ProgramFilesX64\\PC Troubleshooter\\PC_Troubleshooter.exe"
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
    
    def create_python_launcher(self):
        """Create a launcher executable for the Python application"""
        print("🚀 Creating Python launcher...")
        
        app_dir = self.appx_dir / "VFS/ProgramFilesX64/PC Troubleshooter"
        
        # Create a batch launcher
        launcher_content = f'''@echo off
cd /d "%~dp0"
python main.py
'''
        
        launcher_path = app_dir / "PC_Troubleshooter.bat"
        with open(launcher_path, 'w') as f:
            f.write(launcher_content)
        
        # Create a PowerShell launcher for better integration
        ps_launcher = f'''# PC Troubleshooter Launcher
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath
python main.py
'''
        
        ps_path = app_dir / "PC_Troubleshooter.ps1"
        with open(ps_path, 'w', encoding='utf-8') as f:
            f.write(ps_launcher)
        
        # Create a simple executable wrapper (if possible)
        try:
            # Try to create a simple C# launcher
            self.create_csharp_launcher(app_dir)
        except Exception as e:
            print(f"   ⚠️ Could not create C# launcher: {e}")
        
        print("   ✅ Launcher created")
    
    def create_csharp_launcher(self, app_dir):
        """Create a C# executable launcher"""
        launcher_cs = '''using System;
using System.Diagnostics;
using System.IO;

class Program
{
    static void Main()
    {
        try
        {
            string appDir = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
            string pythonScript = Path.Combine(appDir, "main.py");
            
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = "python",
                Arguments = $"\\"{pythonScript}\\"",
                WorkingDirectory = appDir,
                UseShellExecute = false
            };
            
            Process.Start(startInfo);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error launching PC Troubleshooter: {ex.Message}");
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}'''
        
        cs_path = app_dir / "launcher.cs"
        with open(cs_path, 'w') as f:
            f.write(launcher_cs)
        
        # Try to compile it
        try:
            exe_path = app_dir / "PC_Troubleshooter.exe"
            compile_cmd = [
                "csc",
                "/out:" + str(exe_path),
                str(cs_path)
            ]
            
            result = subprocess.run(compile_cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("   ✅ C# launcher compiled successfully")
                os.remove(cs_path)  # Remove source after compilation
            else:
                print(f"   ⚠️ C# compilation failed: {result.stderr}")
                # Create a simple executable alternative
                self.create_simple_exe_launcher(app_dir)
        except FileNotFoundError:
            print("   ⚠️ C# compiler not found, creating alternative launcher")
            self.create_simple_exe_launcher(app_dir)
    
    def create_simple_exe_launcher(self, app_dir):
        """Create a simple executable using PyInstaller"""
        launcher_py = '''#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get the directory where this launcher is located
    launcher_dir = Path(__file__).parent
    main_script = launcher_dir / "main.py"
    
    if main_script.exists():
        # Change to the application directory
        os.chdir(launcher_dir)
        
        # Execute the main script
        subprocess.run([sys.executable, str(main_script)])
    else:
        print(f"Error: main.py not found in {launcher_dir}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
'''
        
        launcher_path = app_dir / "launcher.py"
        with open(launcher_path, 'w') as f:
            f.write(launcher_py)
        
        print("   ✅ Python launcher created")
    
    def build_appx_package(self):
        """Build the APPX package using Windows SDK tools"""
        print("📦 Building APPX package...")
        
        # Check for Windows SDK tools
        makeappx_path = self.find_makeappx_tool()
        if not makeappx_path:
            print("   ❌ Windows SDK MakeAppx.exe not found")
            print("   Please install Windows 10/11 SDK")
            return None
        
        output_dir = self.project_root / "releases"
        output_dir.mkdir(exist_ok=True)
        
        appx_file = output_dir / f"{self.package_name}_v{self.version.replace('.0', '')}.appx"
        
        # Build APPX package
        cmd = [
            str(makeappx_path),
            "pack",
            "/d", str(self.appx_dir),
            "/p", str(appx_file),
            "/o"  # Overwrite existing
        ]
        
        print(f"   Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ APPX package built successfully!")
            print(f"   📁 Package location: {appx_file}")
            print(f"   📊 Package size: {appx_file.stat().st_size / (1024*1024):.1f} MB")
            return appx_file
        else:
            print("   ❌ APPX build failed!")
            print(f"   Error: {result.stderr}")
            return None
    
    def find_makeappx_tool(self):
        """Find MakeAppx.exe in Windows SDK"""
        possible_paths = [
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.22621.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.22000.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.19041.0\\x64\\makeappx.exe",
            "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.18362.0\\x64\\makeappx.exe",
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
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
        """Create installation guide for the APPX package"""
        guide_content = f'''# PC Troubleshooter APPX Installation Guide

## Installation Methods

### Method 1: Developer Mode (Recommended for Testing)

1. **Enable Developer Mode**:
   - Open Settings → Update & Security → For developers
   - Select "Developer mode"
   - Confirm the change

2. **Install the APPX**:
   - Right-click on `{self.package_name}_v{self.version.replace('.0', '')}.appx`
   - Select "Install"
   - Follow the installation wizard

### Method 2: PowerShell Installation

1. **Open PowerShell as Administrator**
2. **Run the installation command**:
   ```powershell
   Add-AppxPackage -Path "{self.package_name}_v{self.version.replace('.0', '')}.appx"
   ```

### Method 3: Using App Installer

1. **Double-click** the APPX file
2. **Click "Install"** in the App Installer dialog
3. **Wait** for installation to complete

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

- **Installation fails**: Ensure Developer Mode is enabled
- **App won't start**: Check if Python is installed on the system
- **Permission errors**: Run installation as Administrator

## Notes

- This is an unsigned APPX package for testing/sideloading
- For Microsoft Store distribution, the package needs to be signed
- Python 3.8+ must be installed on the target system
'''
        
        guide_path = self.project_root / "releases" / "APPX_Installation_Guide.md"
        with open(guide_path, 'w', encoding='utf-8') as f:
            f.write(guide_content)
        
        print(f"   ✅ Installation guide created: {guide_path}")
    
    def build(self):
        """Main build process for APPX package"""
        print("🚀 Starting PC Troubleshooter APPX Build Process")
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
            
            # Create launcher
            self.create_python_launcher()
            
            # Build APPX package
            appx_file = self.build_appx_package()
            
            if appx_file:
                # Create installation guide
                self.create_installation_guide()
                
                print("=" * 60)
                print("✅ APPX BUILD COMPLETED SUCCESSFULLY!")
                print(f"📦 APPX Package: {appx_file}")
                print("📖 Installation Guide: releases/APPX_Installation_Guide.md")
                print("=" * 60)
                
                return {
                    'appx_file': appx_file,
                    'success': True
                }
            else:
                print("❌ APPX BUILD FAILED!")
                return {'success': False}
                
        except Exception as e:
            print(f"❌ Build process failed: {e}")
            return {'success': False, 'error': str(e)}

if __name__ == "__main__":
    builder = AppxBuilder()
    result = builder.build()
    
    if result.get('success'):
        print("\n🎉 Your PC Troubleshooter APPX package is ready!")
        print("Check the 'releases' folder for the installation files.")
    else:
        print("\n💥 APPX build failed. Please check the error messages above.")
        sys.exit(1)
