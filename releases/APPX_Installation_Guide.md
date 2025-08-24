# PC Troubleshooter APPX Installation Guide

## APPX Package Structure

The APPX package has been created in the `appx_package` folder. This contains all the necessary files for a Windows APPX package.

## Installation Methods

### Method 1: Using PowerShell (Recommended)

1. **Copy the entire `appx_package` folder** to your target location
2. **Open PowerShell as Administrator**
3. **Navigate to the parent directory** of the appx_package folder
4. **Run the installation command**:
   ```powershell
   Add-AppxPackage -Register "appx_package\AppxManifest.xml"
   ```

### Method 2: Create APPX file (Requires Windows SDK)

If you have Windows SDK installed:

1. **Install Windows 10/11 SDK** from Microsoft
2. **Use MakeAppx.exe** to create the APPX file:
   ```cmd
   "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\makeappx.exe" pack /d appx_package /p PCTroubleshooter.appx
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
   Add-AppxPackage -Register "appx_package\AppxManifest.xml"
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
Remove-AppxPackage -Package "PCTroubleshooter_1.0.0.0_x64__8wekyb3d8bbwe"
```

## Troubleshooting

- **Installation fails**: Ensure Developer Mode is enabled or run as Administrator
- **App won't start**: The executable should be self-contained
- **Permission errors**: Run installation commands as Administrator

## Notes

- This is an unsigned APPX package for testing/sideloading
- For Microsoft Store distribution, the package needs to be signed with a certificate
- The executable is self-contained and doesn't require Python installation
