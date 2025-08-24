@echo off
title PC Troubleshooter - Final Deployment Package Creator
echo =====================================================
echo PC Troubleshooter - Final Deployment Package Creator
echo =====================================================
echo.

echo 📦 Creating final deployment packages...
echo.

REM Create releases directory if it doesn't exist
if not exist "releases" mkdir "releases"

REM Create final deployment folder
set DEPLOY_DIR=releases\PC_Troubleshooter_v1.0_Final_Release
if exist "%DEPLOY_DIR%" rmdir /s /q "%DEPLOY_DIR%"
mkdir "%DEPLOY_DIR%"

echo 🔧 Copying EXE Package...
mkdir "%DEPLOY_DIR%\EXE_Package"
copy "dist\PC_Troubleshooter.exe" "%DEPLOY_DIR%\EXE_Package\"
copy "README.md" "%DEPLOY_DIR%\EXE_Package\"

echo 📦 Copying Portable Package...
xcopy "releases\PC_Troubleshooter_v1.0.0_Portable" "%DEPLOY_DIR%\Portable_Package\" /e /i /h /y

echo 🏪 Copying APPX Package...
xcopy "appx_package" "%DEPLOY_DIR%\APPX_Package\" /e /i /h /y
copy "Install_APPX.ps1" "%DEPLOY_DIR%\APPX_Package\"

echo 📚 Copying Documentation...
mkdir "%DEPLOY_DIR%\Documentation"
xcopy "docs" "%DEPLOY_DIR%\Documentation\" /e /i /h /y
copy "releases\BUILD_COMPLETE.md" "%DEPLOY_DIR%\"
copy "releases\APPX_Installation_Guide.md" "%DEPLOY_DIR%\Documentation\"

echo 🎨 Copying Assets...
mkdir "%DEPLOY_DIR%\Assets"
xcopy "assets" "%DEPLOY_DIR%\Assets\" /e /i /h /y

echo 📋 Creating deployment README...
(
echo # PC Troubleshooter v1.0 - Final Release Package
echo.
echo This package contains all deployment options for PC Troubleshooter:
echo.
echo ## Package Contents:
echo.
echo ### EXE_Package/
echo - PC_Troubleshooter.exe ^(34.7 MB^) - Standalone executable
echo - README.md - Quick start guide
echo.
echo ### Portable_Package/
echo - Complete portable application with launchers
echo - No installation required
echo - Administrator mode support
echo.
echo ### APPX_Package/
echo - Modern Windows app package
echo - Install_APPX.ps1 - PowerShell installer
echo - Professional app manifest
echo.
echo ### Documentation/
echo - Complete user and developer documentation
echo - Installation guides
echo - API references
echo.
echo ## Quick Start:
echo.
echo 1. **Simplest**: Run EXE_Package\PC_Troubleshooter.exe
echo 2. **Portable**: Use Portable_Package\Launch_PC_Troubleshooter_Admin.bat
echo 3. **Modern App**: Run APPX_Package\Install_APPX.ps1 as Administrator
echo.
echo ## System Requirements:
echo - Windows 10/11
echo - Administrator privileges ^(recommended^)
echo - 4GB RAM minimum
echo.
echo Built on: %date% %time%
echo Version: 1.0.0
) > "%DEPLOY_DIR%\README.txt"

echo.
echo ✅ Final deployment package created successfully!
echo 📁 Location: %DEPLOY_DIR%
echo.
echo 📊 Package Summary:
dir "%DEPLOY_DIR%" /s | find "File(s)"
echo.
echo 🎉 PC Troubleshooter v1.0 is ready for deployment!
echo.
pause
