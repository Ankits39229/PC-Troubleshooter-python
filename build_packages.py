#!/usr/bin/env python3
"""
Build script for creating PC Troubleshooter deployment packages
"""

import os
import sys
import shutil
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime

def create_build_directory():
    """Create and clean build directory"""
    build_dir = Path("build")
    if build_dir.exists():
        shutil.rmtree(build_dir)
    
    build_dir.mkdir()
    return build_dir

def create_portable_package(build_dir):
    """Create portable package"""
    print("📦 Creating portable package...")
    
    portable_dir = build_dir / "portable" / "PCTroubleshooter_v1.0_Portable"
    portable_dir.mkdir(parents=True)
    
    # Copy application files
    shutil.copytree(".", portable_dir, ignore=shutil.ignore_patterns(
        'build', '.git', '__pycache__', '*.pyc', '.pytest_cache',
        'dist', '*.egg-info', '.vscode', '.idea', 'node_modules'
    ))
    
    # Create portable README
    portable_readme = """# PC Troubleshooter v1.0 - Portable Version

## Quick Start Guide

### First Time Setup
1. Right-click `install_dependencies.bat` and select "Run as Administrator"
2. Wait for Python dependencies to install

### Running the Application
- **Normal Mode**: Double-click `launch.bat`
- **Administrator Mode**: Double-click `launch_admin.bat` (Recommended)

## System Requirements
- Windows 10/11
- Python 3.8 or higher
- Administrator privileges (recommended for full functionality)

## Features
✨ Complete black dark theme interface
⚡ Real-time system status monitoring  
🛠️ 20+ diagnostic and repair tools
🔧 System tray integration
⌨️ Professional keyboard shortcuts

## Troubleshooting Categories
🌐 Network - 4 tools for connectivity issues
📶 Bluetooth - 3 tools for device problems
🔊 Audio - 4 tools for sound issues
🖥️ Display - 4 tools for graphics problems
💾 Storage - 4 tools for disk optimization
⚡ Performance - 4 tools for system tuning

## Support
- Documentation: Check the `docs/` folder
- User Manual: `docs/USER_MANUAL.md`
- Developer Guide: `docs/DEVELOPER_GUIDE.md`

---
PC Troubleshooter v1.0 - Professional System Diagnostics
Release Date: August 24, 2025
"""
    
    with open(portable_dir / "README.md", "w") as f:
        f.write(portable_readme)
    
    # Create ZIP package
    zip_path = build_dir / "PCTroubleshooter_v1.0_Portable.zip"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
        for root, dirs, files in os.walk(portable_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(portable_dir.parent)
                zip_file.write(file_path, arc_path)
    
    # Clean up directory
    shutil.rmtree(portable_dir.parent)
    
    size_mb = zip_path.stat().st_size / 1024 / 1024
    print(f"✅ Portable package created: {zip_path.name} ({size_mb:.1f} MB)")
    
    return zip_path

def create_source_package(build_dir):
    """Create source code package"""
    print("📄 Creating source package...")
    
    source_dir = build_dir / "source" / "PCTroubleshooter_v1.0_Source"
    source_dir.mkdir(parents=True)
    
    # Copy source files
    files_to_copy = [
        "main.py", "requirements.txt", "README.md", "LICENSE",
        "ui/", "scripts/", "docs/", "config/"
    ]
    
    for item in files_to_copy:
        src = Path(item)
        if src.is_file():
            shutil.copy2(src, source_dir / src.name)
        elif src.is_dir():
            shutil.copytree(src, source_dir / src.name)
    
    # Create source README
    source_readme = """# PC Troubleshooter v1.0 - Source Code

## Installation from Source

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps
1. Extract this archive to your desired location
2. Open Command Prompt as Administrator
3. Navigate to the extracted directory:
   ```cmd
   cd path\\to\\PCTroubleshooter_v1.0_Source
   ```
4. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
5. Run the application:
   ```cmd
   python main.py
   ```

## Development Setup

### Development Dependencies
```cmd
pip install pytest pytest-qt black flake8 mypy
```

### Running Tests
```cmd
pytest tests/
```

### Code Formatting
```cmd
black .
flake8 .
```

## Project Structure
```
PCTroubleshooter/
├── main.py              # Application entry point
├── ui/                  # User interface modules
├── scripts/             # Diagnostic scripts
├── docs/                # Documentation
├── config/              # Configuration files
└── requirements.txt     # Python dependencies
```

## Building Executable

### Using PyInstaller
```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --icon=assets\\icon.ico main.py
```

## Contributing
See `docs/DEVELOPER_GUIDE.md` for development guidelines.

---
PC Troubleshooter v1.0 - Source Code Package
"""
    
    with open(source_dir / "README.md", "w") as f:
        f.write(source_readme)
    
    # Create ZIP package
    zip_path = build_dir / "PCTroubleshooter_v1.0_Source.zip"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(source_dir.parent)
                zip_file.write(file_path, arc_path)
    
    # Clean up directory
    shutil.rmtree(source_dir.parent)
    
    size_mb = zip_path.stat().st_size / 1024 / 1024
    print(f"✅ Source package created: {zip_path.name} ({size_mb:.1f} MB)")
    
    return zip_path

def build_executable(build_dir):
    """Build standalone executable using PyInstaller"""
    print("🔨 Building standalone executable...")
    
    try:
        # Check if PyInstaller is available
        subprocess.run(["pyinstaller", "--version"], 
                      capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], 
                      check=True)
    
    # Build executable
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=PCTroubleshooter",
        "--distpath=" + str(build_dir / "executable"),
        "--workpath=" + str(build_dir / "temp"),
        "--specpath=" + str(build_dir / "spec"),
        "main.py"
    ]
    
    # Add icon if available
    icon_path = Path("assets/icon.ico")
    if icon_path.exists():
        cmd.extend(["--icon=" + str(icon_path)])
    
    # Add additional data
    cmd.extend([
        "--add-data=scripts;scripts",
        "--add-data=docs;docs", 
        "--add-data=config;config"
    ])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        exe_path = build_dir / "executable" / "PCTroubleshooter.exe"
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / 1024 / 1024
            print(f"✅ Executable created: {exe_path.name} ({size_mb:.1f} MB)")
            return exe_path
        else:
            print("❌ Executable not found after build")
            return None
    else:
        print(f"❌ Build failed: {result.stderr}")
        return None

def create_release_info(build_dir, packages):
    """Create release information file"""
    print("📋 Creating release information...")
    
    release_info = f"""# PC Troubleshooter v1.0 - Release Information

## Release Details
- **Version**: 1.0.0
- **Release Date**: {datetime.now().strftime('%B %d, %Y')}
- **Build Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Available Packages

"""
    
    for pkg_path in packages:
        if pkg_path and pkg_path.exists():
            size_mb = pkg_path.stat().st_size / 1024 / 1024
            release_info += f"- **{pkg_path.name}** - {size_mb:.1f} MB\n"
    
    release_info += f"""
## System Requirements
- **OS**: Windows 10 (Build 1809) or Windows 11
- **RAM**: 4 GB minimum, 8 GB recommended
- **Storage**: 500 MB free space
- **Display**: 1024x768 minimum resolution

## Installation Methods

### Standalone Executable (Recommended)
- Download: `PCTroubleshooter.exe`
- No Python installation required
- Includes all dependencies
- Double-click to run

### Portable Version
- Download: `PCTroubleshooter_v1.0_Portable.zip`
- Extract and run `launch_admin.bat`
- Requires Python 3.8+
- All features included

### Source Code
- Download: `PCTroubleshooter_v1.0_Source.zip`
- For developers and advanced users
- Requires manual dependency installation
- Full source code access

## Features
✨ **Complete Black Dark Theme** - Professional appearance
⚡ **Real-Time Monitoring** - Live system status dashboard
🛠️ **20+ Diagnostic Tools** - Comprehensive troubleshooting
🔧 **System Integration** - Tray icons and shortcuts
📊 **Professional UI** - Enterprise-quality interface

## Support
- **Documentation**: Included in all packages
- **User Manual**: `docs/USER_MANUAL.md`
- **Developer Guide**: `docs/DEVELOPER_GUIDE.md`
- **Deployment Guide**: `docs/DEPLOYMENT_GUIDE.md`

---
PC Troubleshooter Development Team
{datetime.now().strftime('%Y')}
"""
    
    release_path = build_dir / "RELEASE_INFO.md"
    with open(release_path, "w") as f:
        f.write(release_info)
    
    print(f"✅ Release info created: {release_path.name}")
    return release_path

def main():
    """Main build process"""
    print("🚀 PC Troubleshooter v1.0 - Build Script")
    print("=" * 50)
    
    # Create build directory
    build_dir = create_build_directory()
    packages = []
    
    try:
        # Create packages
        portable_pkg = create_portable_package(build_dir)
        packages.append(portable_pkg)
        
        source_pkg = create_source_package(build_dir)
        packages.append(source_pkg)
        
        # Build executable (optional)
        print("\n🔨 Do you want to build standalone executable? (y/n): ", end="")
        if input().lower().startswith('y'):
            exe_pkg = build_executable(build_dir)
            packages.append(exe_pkg)
        
        # Create release information
        release_info = create_release_info(build_dir, packages)
        
        print("\n" + "=" * 50)
        print("🎉 Build completed successfully!")
        print(f"📁 Build directory: {build_dir.absolute()}")
        print(f"📦 Packages created: {len([p for p in packages if p])}")
        
        total_size = sum(p.stat().st_size for p in packages if p and p.exists())
        print(f"💾 Total size: {total_size / 1024 / 1024:.1f} MB")
        
        print("\n📋 Available packages:")
        for pkg in packages:
            if pkg and pkg.exists():
                size_mb = pkg.stat().st_size / 1024 / 1024
                print(f"   - {pkg.name} ({size_mb:.1f} MB)")
        
        print(f"\nℹ️  Release information: {release_info.name}")
        print("\n🚀 PC Troubleshooter v1.0 is ready for deployment!")
        
    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
