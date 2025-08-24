#!/usr/bin/env python3
"""
PC Troubleshooter - EXE Build Script
Professional executable build system with PyInstaller
"""

import os
import sys
import shutil
import subprocess
import json
from pathlib import Path

class ExeBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.dist_dir = self.project_root / "dist"
        self.build_dir = self.project_root / "build"
        self.app_name = "PC_Troubleshooter"
        self.version = "1.0.0"
        
    def clean_build_dirs(self):
        """Clean previous build directories"""
        print("🧹 Cleaning previous build directories...")
        for dir_path in [self.dist_dir, self.build_dir]:
            if dir_path.exists():
                shutil.rmtree(dir_path)
                print(f"   Removed: {dir_path}")
    
    def install_pyinstaller(self):
        """Install PyInstaller if not present"""
        print("📦 Checking PyInstaller installation...")
        try:
            import PyInstaller
            print("   ✅ PyInstaller already installed")
        except ImportError:
            print("   📥 Installing PyInstaller...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
            print("   ✅ PyInstaller installed successfully")
    
    def create_spec_file(self):
        """Create PyInstaller spec file for advanced configuration"""
        spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[r'{self.project_root.as_posix()}'],
    binaries=[],
    datas=[
        ('ui', 'ui'),
        ('scripts', 'scripts'),
        ('assets', 'assets'),
        ('docs', 'docs'),
        ('config.ini', '.'),
    ],
    hiddenimports=[
        'PyQt6.QtCore',
        'PyQt6.QtGui', 
        'PyQt6.QtWidgets',
        'PyQt6.QtSvg',
        'PyQt6.QtPrintSupport',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{self.app_name}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Windowed application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=r'{self.project_root / "assets" / "icon.png"}',
    version='version_info.txt'
)
'''
        
        spec_file = self.project_root / f"{self.app_name}.spec"
        with open(spec_file, 'w', encoding='utf-8') as f:
            f.write(spec_content)
        
        print(f"   ✅ Created spec file: {spec_file}")
        return spec_file
    
    def create_version_info(self):
        """Create Windows version info file"""
        version_info = f'''# UTF-8
#
# Version information for PC Troubleshooter
#

VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'PC Troubleshooter Team'),
        StringStruct(u'FileDescription', u'PC Troubleshooter - Professional System Diagnostic Tool'),
        StringStruct(u'FileVersion', u'{self.version}'),
        StringStruct(u'InternalName', u'{self.app_name}'),
        StringStruct(u'LegalCopyright', u'Copyright © 2025 PC Troubleshooter Team'),
        StringStruct(u'OriginalFilename', u'{self.app_name}.exe'),
        StringStruct(u'ProductName', u'PC Troubleshooter'),
        StringStruct(u'ProductVersion', u'{self.version}')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
        
        version_file = self.project_root / "version_info.txt"
        with open(version_file, 'w', encoding='utf-8') as f:
            f.write(version_info)
        
        print(f"   ✅ Created version info: {version_file}")
        return version_file
    
    def convert_icon_to_ico(self):
        """Convert PNG icon to ICO format for Windows"""
        try:
            from PIL import Image
            
            png_icon = self.project_root / "assets" / "icon.png"
            ico_icon = self.project_root / "assets" / "icon.ico"
            
            if png_icon.exists():
                print("🎨 Converting PNG icon to ICO format...")
                img = Image.open(png_icon)
                
                # Create multiple sizes for ICO
                sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
                img.save(ico_icon, format='ICO', sizes=sizes)
                print(f"   ✅ Created ICO icon: {ico_icon}")
                return ico_icon
            else:
                print(f"   ⚠️ PNG icon not found: {png_icon}")
                return None
                
        except ImportError:
            print("   📥 Installing Pillow for icon conversion...")
            subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"], check=True)
            return self.convert_icon_to_ico()  # Retry after installation
        except Exception as e:
            print(f"   ⚠️ Icon conversion failed: {e}")
            return None
    
    def build_executable(self):
        """Build the executable using PyInstaller"""
        print("🔨 Building executable with PyInstaller...")
        
        # Convert icon
        ico_icon = self.convert_icon_to_ico()
        
        # Create spec file
        spec_file = self.create_spec_file()
        
        # Update spec file with ICO icon if available
        if ico_icon:
            spec_content = spec_file.read_text()
            spec_content = spec_content.replace('icon.png', 'icon.ico')
            spec_file.write_text(spec_content)
        
        # Create version info
        self.create_version_info()
        
        # Build with PyInstaller
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm",
            str(spec_file)
        ]
        
        print(f"   Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=self.project_root, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ Executable built successfully!")
            exe_path = self.dist_dir / f"{self.app_name}.exe"
            if exe_path.exists():
                print(f"   📁 Executable location: {exe_path}")
                print(f"   📊 File size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
                return exe_path
            else:
                print("   ❌ Executable not found in expected location")
                return None
        else:
            print("   ❌ Build failed!")
            print(f"   Error: {result.stderr}")
            return None
    
    def create_portable_package(self, exe_path):
        """Create a portable package with the executable and dependencies"""
        print("📦 Creating portable package...")
        
        portable_dir = self.project_root / "releases" / f"{self.app_name}_v{self.version}_Portable"
        portable_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy executable
        shutil.copy2(exe_path, portable_dir / f"{self.app_name}.exe")
        
        # Copy essential files
        essential_files = [
            "README.md",
            "LICENSE",
            "config.ini",
        ]
        
        for file_name in essential_files:
            file_path = self.project_root / file_name
            if file_path.exists():
                shutil.copy2(file_path, portable_dir)
        
        # Copy essential directories
        essential_dirs = ["docs", "scripts"]
        for dir_name in essential_dirs:
            dir_path = self.project_root / dir_name
            if dir_path.exists():
                shutil.copytree(dir_path, portable_dir / dir_name, dirs_exist_ok=True)
        
        # Create launcher scripts
        self.create_launcher_scripts(portable_dir)
        
        print(f"   ✅ Portable package created: {portable_dir}")
        return portable_dir
    
    def create_launcher_scripts(self, portable_dir):
        """Create launcher scripts for the portable package"""
        
        # Simple launcher
        launcher_script = f'''@echo off
title PC Troubleshooter v{self.version}
echo Starting PC Troubleshooter...
start "" "{self.app_name}.exe"
'''
        
        launcher_path = portable_dir / "Launch_PC_Troubleshooter.bat"
        with open(launcher_path, 'w') as f:
            f.write(launcher_script)
        
        # Admin launcher
        admin_launcher = f'''@echo off
title PC Troubleshooter v{self.version} (Administrator)
echo Starting PC Troubleshooter with Administrator privileges...
echo This may prompt for UAC confirmation.
powershell -Command "Start-Process '{self.app_name}.exe' -Verb RunAs"
'''
        
        admin_path = portable_dir / "Launch_PC_Troubleshooter_Admin.bat"
        with open(admin_path, 'w') as f:
            f.write(admin_launcher)
        
        print("   ✅ Created launcher scripts")
    
    def build(self):
        """Main build process"""
        print("🚀 Starting PC Troubleshooter EXE Build Process")
        print("=" * 60)
        
        try:
            # Clean previous builds
            self.clean_build_dirs()
            
            # Install PyInstaller
            self.install_pyinstaller()
            
            # Build executable
            exe_path = self.build_executable()
            
            if exe_path:
                # Create portable package
                portable_dir = self.create_portable_package(exe_path)
                
                print("=" * 60)
                print("✅ BUILD COMPLETED SUCCESSFULLY!")
                print(f"📁 Executable: {exe_path}")
                print(f"📦 Portable Package: {portable_dir}")
                print("=" * 60)
                
                return {
                    'exe_path': exe_path,
                    'portable_dir': portable_dir,
                    'success': True
                }
            else:
                print("❌ BUILD FAILED!")
                return {'success': False}
                
        except Exception as e:
            print(f"❌ Build process failed: {e}")
            return {'success': False, 'error': str(e)}

if __name__ == "__main__":
    builder = ExeBuilder()
    result = builder.build()
    
    if result.get('success'):
        print("\n🎉 Your PC Troubleshooter executable is ready!")
        print("You can find it in the 'dist' and 'releases' folders.")
    else:
        print("\n💥 Build failed. Please check the error messages above.")
        sys.exit(1)
