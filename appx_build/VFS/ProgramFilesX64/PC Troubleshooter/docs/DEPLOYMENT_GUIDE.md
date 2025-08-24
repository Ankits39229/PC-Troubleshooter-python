# PC Troubleshooter - Deployment Guide

## 📦 Deployment Artifacts and Installation

This guide covers the deployment process and installation methods for PC Troubleshooter v1.0.

## 🚀 Quick Installation Options

### Option 1: Standalone Executable (Recommended)
- **File**: `PCTroubleshooter_v1.0_Setup.exe`
- **Size**: ~50 MB
- **Requirements**: Windows 10/11, Administrator privileges
- **Installation**: Double-click and follow wizard

### Option 2: Portable Version
- **File**: `PCTroubleshooter_v1.0_Portable.zip`
- **Size**: ~25 MB
- **Requirements**: Python 3.8+ installed
- **Installation**: Extract and run `launch.bat`

### Option 3: Python Source
- **File**: `PCTroubleshooter_v1.0_Source.zip`
- **Size**: ~5 MB
- **Requirements**: Python 3.8+, PyQt6
- **Installation**: Extract and run `python main.py`

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10 (Build 1809) or Windows 11
- **RAM**: 4 GB
- **Storage**: 500 MB free space
- **Display**: 1024x768 resolution

### Recommended Requirements
- **OS**: Windows 11 (latest updates)
- **RAM**: 8 GB or more
- **Storage**: 1 GB free space
- **Display**: 1920x1080 or higher
- **Privileges**: Administrator account

## 🔧 Installation Instructions

### Standalone Installer Method

1. **Download** `PCTroubleshooter_v1.0_Setup.exe`
2. **Right-click** the installer and select "Run as Administrator"
3. **Follow** the installation wizard:
   - Accept the license agreement
   - Choose installation directory (default: `C:\Program Files\PCTroubleshooter\`)
   - Select additional components (desktop shortcut, start menu entry)
   - Complete the installation
4. **Launch** from Start Menu or desktop shortcut

### Portable Version Method

1. **Download** `PCTroubleshooter_v1.0_Portable.zip`
2. **Extract** to your desired location (e.g., `C:\Tools\PCTroubleshooter\`)
3. **Run** `install_dependencies.bat` as Administrator (first time only)
4. **Launch** using `launch.bat`

### Source Installation Method

1. **Install Python 3.8+** from python.org
2. **Download** `PCTroubleshooter_v1.0_Source.zip`
3. **Extract** to your desired location
4. **Open Command Prompt** as Administrator
5. **Navigate** to the extracted directory
6. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```
7. **Run the application**:
   ```cmd
   python main.py
   ```

## 📁 File Structure After Installation

### Standalone Installation
```
C:\Program Files\PCTroubleshooter\
├── PCTroubleshooter.exe          # Main executable
├── scripts\                      # Diagnostic scripts
│   ├── network\
│   ├── audio\
│   ├── display\
│   ├── bluetooth\
│   ├── storage\
│   └── performance\
├── docs\                         # Documentation
├── logs\                         # Application logs
├── config\                       # Configuration files
└── uninstall.exe                 # Uninstaller
```

### Portable Installation
```
PCTroubleshooter\
├── main.py                       # Application entry point
├── launch.bat                    # Launcher script
├── install_dependencies.bat      # Dependency installer
├── ui\                           # User interface modules
├── scripts\                      # Diagnostic scripts
├── docs\                         # Documentation
├── config\                       # Configuration files
├── requirements.txt              # Python dependencies
└── README.md                     # Basic information
```

## 🛠️ Build Process Documentation

### Building from Source

#### Prerequisites
```bash
# Install Python 3.8+
python --version

# Install build dependencies
pip install pyinstaller
pip install auto-py-to-exe  # Optional GUI for PyInstaller
```

#### Create Standalone Executable
```bash
# Navigate to project directory
cd C:\path\to\app3

# Build single file executable
pyinstaller --onefile --windowed --icon=assets\icon.ico --name=PCTroubleshooter main.py

# Build directory-based executable (faster startup)
pyinstaller --onedir --windowed --icon=assets\icon.ico --name=PCTroubleshooter main.py
```

#### Advanced Build Options
```bash
# Build with additional data files
pyinstaller --onefile --windowed ^
    --icon=assets\icon.ico ^
    --add-data "scripts;scripts" ^
    --add-data "config;config" ^
    --add-data "docs;docs" ^
    --name=PCTroubleshooter ^
    main.py

# Build with hidden imports (if needed)
pyinstaller --onefile --windowed ^
    --hidden-import=PyQt6.QtCore ^
    --hidden-import=PyQt6.QtWidgets ^
    --hidden-import=PyQt6.QtGui ^
    --icon=assets\icon.ico ^
    --name=PCTroubleshooter ^
    main.py
```

### Creating Windows Installer

#### NSIS Installer Script
Create `installer.nsi`:

```nsis
; PC Troubleshooter Installer Script
; Requires NSIS (Nullsoft Scriptable Install System)

!define APP_NAME "PC Troubleshooter"
!define APP_VERSION "1.0"
!define APP_PUBLISHER "PC Troubleshooter Team"
!define APP_URL "https://github.com/pc-troubleshooter"
!define APP_SUPPORT_URL "https://github.com/pc-troubleshooter/support"

; Main installer settings
Name "${APP_NAME} v${APP_VERSION}"
OutFile "PCTroubleshooter_v${APP_VERSION}_Setup.exe"
InstallDir "$PROGRAMFILES\${APP_NAME}"
InstallDirRegKey HKLM "Software\${APP_NAME}" ""
RequestExecutionLevel admin

; Interface settings
!include "MUI2.nsh"
!define MUI_ABORTWARNING
!define MUI_ICON "assets\icon.ico"
!define MUI_UNICON "assets\icon.ico"

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Languages
!insertmacro MUI_LANGUAGE "English"

; Installer sections
Section "Main Application" SecMain
  SetOutPath "$INSTDIR"
  
  ; Copy main files
  File "dist\PCTroubleshooter.exe"
  File "README.md"
  File "LICENSE"
  
  ; Copy directories
  SetOutPath "$INSTDIR\scripts"
  File /r "scripts\*"
  
  SetOutPath "$INSTDIR\docs"
  File /r "docs\*"
  
  SetOutPath "$INSTDIR\config"
  File /r "config\*"
  
  ; Create shortcuts
  CreateDirectory "$SMPROGRAMS\${APP_NAME}"
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\PCTroubleshooter.exe"
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe"
  CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\PCTroubleshooter.exe"
  
  ; Registry entries
  WriteRegStr HKLM "Software\${APP_NAME}" "" "$INSTDIR"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "DisplayName" "${APP_NAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "UninstallString" "$INSTDIR\uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "DisplayVersion" "${APP_VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "Publisher" "${APP_PUBLISHER}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "URLInfoAbout" "${APP_URL}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" "HelpLink" "${APP_SUPPORT_URL}"
  
  ; Create uninstaller
  WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

; Uninstaller section
Section "Uninstall"
  ; Remove files
  Delete "$INSTDIR\PCTroubleshooter.exe"
  Delete "$INSTDIR\README.md"
  Delete "$INSTDIR\LICENSE"
  Delete "$INSTDIR\uninstall.exe"
  
  ; Remove directories
  RMDir /r "$INSTDIR\scripts"
  RMDir /r "$INSTDIR\docs"
  RMDir /r "$INSTDIR\config"
  RMDir /r "$INSTDIR\logs"
  RMDir "$INSTDIR"
  
  ; Remove shortcuts
  Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
  Delete "$SMPROGRAMS\${APP_NAME}\Uninstall.lnk"
  RMDir "$SMPROGRAMS\${APP_NAME}"
  Delete "$DESKTOP\${APP_NAME}.lnk"
  
  ; Remove registry entries
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"
  DeleteRegKey HKLM "Software\${APP_NAME}"
SectionEnd
```

#### Build Installer
```bash
# Install NSIS from https://nsis.sourceforge.io/
# Build installer
makensis installer.nsi
```

### Creating Portable Package

#### Portable Build Script
Create `build_portable.py`:

```python
#!/usr/bin/env python3
"""
Build script for creating portable version of PC Troubleshooter
"""

import os
import shutil
import zipfile
import subprocess
from pathlib import Path

def create_portable_package():
    """Create portable package"""
    
    print("Creating PC Troubleshooter Portable Package...")
    
    # Create build directory
    build_dir = Path("build/portable")
    build_dir.mkdir(parents=True, exist_ok=True)
    
    app_dir = build_dir / "PCTroubleshooter"
    if app_dir.exists():
        shutil.rmtree(app_dir)
    
    # Copy application files
    print("Copying application files...")
    shutil.copytree(".", app_dir, ignore=shutil.ignore_patterns(
        'build', '.git', '__pycache__', '*.pyc', '.pytest_cache',
        'dist', '*.egg-info', '.vscode', '.idea'
    ))
    
    # Create launcher script
    print("Creating launcher scripts...")
    launcher_content = """@echo off
title PC Troubleshooter v1.0
echo Starting PC Troubleshooter...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Check if dependencies are installed
if not exist "requirements_installed.txt" (
    echo Installing dependencies...
    pip install -r requirements.txt
    if %errorLevel% equ 0 (
        echo Dependencies installed > requirements_installed.txt
    ) else (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Start application
cd /d "%~dp0"
python main.py

if %errorLevel% neq 0 (
    echo.
    echo Application exited with error code %errorLevel%
    pause
)
"""
    
    with open(app_dir / "launch.bat", "w") as f:
        f.write(launcher_content)
    
    # Create admin launcher
    admin_launcher_content = """@echo off
title PC Troubleshooter v1.0 (Administrator)
echo Starting PC Troubleshooter with Administrator privileges...
echo.

REM Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting Administrator privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs"
    exit /b
)

call launch.bat
"""
    
    with open(app_dir / "launch_admin.bat", "w") as f:
        f.write(admin_launcher_content)
    
    # Create installation script for dependencies
    install_deps_content = """@echo off
title PC Troubleshooter - Install Dependencies
echo Installing PC Troubleshooter Dependencies...
echo.

REM Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires Administrator privileges.
    echo Please run as Administrator.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

if %errorLevel% equ 0 (
    echo.
    echo =============================================
    echo Dependencies installed successfully!
    echo You can now run PC Troubleshooter using:
    echo   launch.bat (normal mode)
    echo   launch_admin.bat (administrator mode)
    echo =============================================
    echo Dependencies installed > requirements_installed.txt
) else (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please check your internet connection and try again
)

pause
"""
    
    with open(app_dir / "install_dependencies.bat", "w") as f:
        f.write(install_deps_content)
    
    # Create README for portable version
    portable_readme = """# PC Troubleshooter v1.0 - Portable Version

## Quick Start

1. **First Time Setup**:
   - Right-click `install_dependencies.bat` and select "Run as Administrator"
   - Wait for dependency installation to complete

2. **Running the Application**:
   - For normal use: Double-click `launch.bat`
   - For administrator privileges: Double-click `launch_admin.bat`

## Requirements

- Windows 10/11
- Python 3.8 or higher
- Administrator privileges (recommended)

## Features

- Complete black dark theme interface
- Real-time system monitoring
- 20+ diagnostic and repair tools
- System tray integration
- Keyboard shortcuts

## Troubleshooting

If you encounter issues:

1. **Python not found**: Install Python from https://python.org
2. **Dependencies fail**: Run `install_dependencies.bat` as Administrator
3. **Scripts fail**: Ensure you're running as Administrator
4. **UI issues**: Update your graphics drivers

## Support

- Documentation: See `docs/` folder
- Issues: Contact support team
- Updates: Check for latest version

---

PC Troubleshooter v1.0 - Professional System Diagnostics
"""
    
    with open(app_dir / "README_PORTABLE.md", "w") as f:
        f.write(portable_readme)
    
    # Create ZIP package
    print("Creating ZIP package...")
    zip_path = build_dir / "PCTroubleshooter_v1.0_Portable.zip"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(app_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(build_dir)
                zip_file.write(file_path, arc_path)
    
    print(f"Portable package created: {zip_path}")
    print(f"Package size: {zip_path.stat().st_size / 1024 / 1024:.1f} MB")
    
    return zip_path

if __name__ == "__main__":
    create_portable_package()
    print("Portable package build complete!")
```

## 🔧 Configuration Files

### requirements.txt
```txt
PyQt6>=6.4.0
```

### requirements-dev.txt (for development)
```txt
PyQt6>=6.4.0
pytest>=7.0.0
pytest-qt>=4.0.0
black>=22.0.0
flake8>=4.0.0
mypy>=0.950
pyinstaller>=5.0.0
```

### setup.py (for pip installation)
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pc-troubleshooter",
    version="1.0.0",
    author="PC Troubleshooter Team",
    author_email="support@pctroubleshooter.com",
    description="Professional Windows system diagnostic and repair tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pc-troubleshooter/pc-troubleshooter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": ["scripts/**/*.bat", "docs/**/*.md", "config/**/*.json"],
    },
    entry_points={
        "console_scripts": [
            "pc-troubleshooter=main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/pc-troubleshooter/pc-troubleshooter/issues",
        "Source": "https://github.com/pc-troubleshooter/pc-troubleshooter",
        "Documentation": "https://github.com/pc-troubleshooter/pc-troubleshooter/wiki",
    },
)
```

## 📊 Version Information

### Version 1.0.0 Release Notes

#### New Features
- ✨ Complete black dark theme interface
- ⚡ Real-time system status monitoring
- 🛠️ 20+ diagnostic and repair tools across 6 categories
- 🖥️ Professional PyQt6-based GUI
- 📊 Status dashboard with live metrics
- 🔧 System tray integration
- ⌨️ Keyboard shortcuts for power users
- 📝 Comprehensive logging system
- 🎨 Professional animations and visual effects

#### Diagnostic Categories
- 🌐 **Network**: 4 tools for connectivity issues
- 📶 **Bluetooth**: 3 tools for Bluetooth problems  
- 🔊 **Audio**: 4 tools for sound issues
- 🖥️ **Display**: 4 tools for graphics problems
- 💾 **Storage**: 4 tools for disk optimization
- ⚡ **Performance**: 4 tools for system optimization

#### Technical Specifications
- **Framework**: PyQt6 for modern GUI
- **Platform**: Windows 10/11 
- **Architecture**: Threaded script execution
- **Scripts**: Windows Batch and PowerShell
- **Size**: ~50 MB (standalone), ~25 MB (portable)

#### Known Issues
- Requires Administrator privileges for full functionality
- Some antivirus software may flag script execution
- High DPI scaling may cause minor UI issues

#### Planned Features (Future Releases)
- Custom script editor
- Scheduled diagnostics
- Network deployment tools
- Plugin system
- Multi-language support

## 🚀 Deployment Checklist

### Pre-Release Testing
- [ ] All unit tests pass
- [ ] Integration tests complete
- [ ] UI tests on different resolutions
- [ ] Performance testing completed
- [ ] Security scan performed
- [ ] Documentation reviewed
- [ ] Version numbers updated

### Build Verification
- [ ] Standalone executable builds without errors
- [ ] Installer creates all necessary files
- [ ] Portable version extracts correctly
- [ ] All dependencies included
- [ ] File associations work
- [ ] Shortcuts function properly

### Distribution Preparation
- [ ] Release notes written
- [ ] Download links updated
- [ ] Documentation uploaded
- [ ] Support channels notified
- [ ] User guides published
- [ ] Video tutorials created

### Post-Release Activities
- [ ] Monitor download statistics
- [ ] Watch for user feedback
- [ ] Track error reports
- [ ] Update support documentation
- [ ] Plan next release cycle

---

**PC Troubleshooter v1.0 - Deployment Complete**  
*Professional system diagnostics made simple*

*Release Date: August 24, 2025*
