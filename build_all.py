#!/usr/bin/env python3
"""
PC Troubleshooter - Master Build Script
Builds both EXE and APPX packages with comprehensive options
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
import argparse

class MasterBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.releases_dir = self.project_root / "releases"
        
    def ensure_releases_dir(self):
        """Ensure releases directory exists"""
        self.releases_dir.mkdir(exist_ok=True)
    
    def install_build_dependencies(self):
        """Install required build dependencies"""
        print("📦 Installing build dependencies...")
        
        dependencies = [
            "pyinstaller",
            "pillow",
        ]
        
        for dep in dependencies:
            print(f"   Installing {dep}...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", dep], check=True)
                print(f"   ✅ {dep} installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"   ❌ Failed to install {dep}: {e}")
                return False
        
        print("   ✅ All build dependencies installed")
        return True
    
    def build_exe(self):
        """Build EXE package"""
        print("\n🔨 Building EXE Package...")
        print("-" * 40)
        
        try:
            from build_exe import ExeBuilder
            builder = ExeBuilder()
            return builder.build()
        except Exception as e:
            print(f"❌ EXE build failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def build_appx(self):
        """Build APPX package"""
        print("\n📦 Building APPX Package...")
        print("-" * 40)
        
        try:
            from build_appx import AppxBuilder
            builder = AppxBuilder()
            return builder.build()
        except Exception as e:
            print(f"❌ APPX build failed: {e}")
            return {'success': False, 'error': str(e)}
    
    def create_release_summary(self, exe_result, appx_result):
        """Create a summary of the build results"""
        summary_content = f"""# PC Troubleshooter v1.0 - Build Summary

**Build Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Build Results

### EXE Package
- **Status**: {'✅ Success' if exe_result.get('success') else '❌ Failed'}
"""
        
        if exe_result.get('success'):
            summary_content += f"""- **Executable**: {exe_result.get('exe_path', 'Unknown')}
- **Portable Package**: {exe_result.get('portable_dir', 'Unknown')}
"""
        else:
            summary_content += f"""- **Error**: {exe_result.get('error', 'Unknown error')}
"""
        
        summary_content += f"""
### APPX Package
- **Status**: {'✅ Success' if appx_result.get('success') else '❌ Failed'}
"""
        
        if appx_result.get('success'):
            summary_content += f"""- **APPX File**: {appx_result.get('appx_file', 'Unknown')}
- **Installation Guide**: releases/APPX_Installation_Guide.md
"""
        else:
            summary_content += f"""- **Error**: {appx_result.get('error', 'Unknown error')}
"""
        
        summary_content += """
## Installation Options

### EXE Version (Recommended)
1. **Portable**: Extract and run `Launch_PC_Troubleshooter.bat`
2. **Executable**: Run `PC_Troubleshooter.exe` directly

### APPX Version (Microsoft Store Style)
1. Enable Developer Mode in Windows Settings
2. Right-click APPX file and select "Install"
3. Or use PowerShell: `Add-AppxPackage -Path "package.appx"`

## System Requirements
- Windows 10/11
- Python 3.8+ (for APPX version)
- Administrator privileges (recommended)

## Support
- Documentation: `docs/` folder
- User Manual: `docs/USER_MANUAL.md`
- Developer Guide: `docs/DEVELOPER_GUIDE.md`
"""
        
        summary_path = self.releases_dir / "BUILD_SUMMARY.md"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"📋 Build summary created: {summary_path}")
    
    def build_all(self):
        """Build both EXE and APPX packages"""
        print("🚀 PC Troubleshooter - Master Build Process")
        print("=" * 60)
        
        # Ensure releases directory
        self.ensure_releases_dir()
        
        # Install dependencies
        if not self.install_build_dependencies():
            print("❌ Failed to install build dependencies")
            return False
        
        # Build EXE
        exe_result = self.build_exe()
        
        # Build APPX
        appx_result = self.build_appx()
        
        # Create summary
        self.create_release_summary(exe_result, appx_result)
        
        # Final summary
        print("\n" + "=" * 60)
        print("🏁 MASTER BUILD PROCESS COMPLETED")
        print("=" * 60)
        
        success_count = sum([exe_result.get('success', False), appx_result.get('success', False)])
        
        if success_count == 2:
            print("✅ ALL BUILDS SUCCESSFUL!")
            print("📁 Check the 'releases' folder for all packages")
        elif success_count == 1:
            print("⚠️ PARTIAL SUCCESS - One build completed")
            print("📁 Check the 'releases' folder for available packages")
        else:
            print("❌ ALL BUILDS FAILED")
            print("Please check the error messages above")
        
        print("\n📦 Available Packages:")
        if exe_result.get('success'):
            print("   🔧 EXE Package (Standalone executable)")
            print("   📦 Portable Package (No installation required)")
        if appx_result.get('success'):
            print("   🏪 APPX Package (Microsoft Store style)")
        
        print("\n📖 Documentation:")
        print("   📋 BUILD_SUMMARY.md - Complete build information")
        print("   📖 User Manual - docs/USER_MANUAL.md")
        print("   🔧 Developer Guide - docs/DEVELOPER_GUIDE.md")
        
        return success_count > 0

def main():
    parser = argparse.ArgumentParser(description="Build PC Troubleshooter packages")
    parser.add_argument("--exe-only", action="store_true", help="Build only EXE package")
    parser.add_argument("--appx-only", action="store_true", help="Build only APPX package")
    parser.add_argument("--no-deps", action="store_true", help="Skip dependency installation")
    
    args = parser.parse_args()
    
    builder = MasterBuilder()
    
    if args.exe_only:
        print("Building EXE package only...")
        if not args.no_deps:
            builder.install_build_dependencies()
        result = builder.build_exe()
        success = result.get('success', False)
    elif args.appx_only:
        print("Building APPX package only...")
        if not args.no_deps:
            builder.install_build_dependencies()
        result = builder.build_appx()
        success = result.get('success', False)
    else:
        print("Building all packages...")
        success = builder.build_all()
    
    if success:
        print("\n🎉 Build completed successfully!")
        return 0
    else:
        print("\n💥 Build failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
