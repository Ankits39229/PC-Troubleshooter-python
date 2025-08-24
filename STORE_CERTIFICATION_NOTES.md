# Microsoft Store Certification - PC Troubleshooter v1.0

## Application Summary
**PC Troubleshooter** is a professional Windows system diagnostic and repair tool providing 20+ automated diagnostic scripts across 6 categories.

## Dependencies Disclosure

### Non-Microsoft Dependencies: NONE
- Application is fully self-contained
- Uses only standard Windows built-in utilities
- No third-party drivers or external services required

### Windows Services Integration
The application interacts with standard Windows NT services:
- Windows Audio Service (Audiosrv) - for audio diagnostics
- Bluetooth Support Service (bthserv) - for Bluetooth troubleshooting  
- DHCP Client (Dhcp) - for network diagnostics
- DNS Client (Dnscache) - for network troubleshooting

### Required Capabilities
- runFullTrust - Required for executing system diagnostic commands
- internetClient - For network connectivity tests only
- privateNetworkClientServer - For local network diagnostics

## Test Account Information
**No special test accounts required**
- Standard Windows user account with administrator privileges is sufficient
- Domain accounts supported for enterprise testing

## Feature Access Instructions

### Administrator Mode Access
1. Right-click PC_Troubleshooter.exe
2. Select "Run as Administrator" 
3. Confirm UAC prompt
4. All advanced features now available (indicated in title bar)

### Core Feature Categories
1. **Network Troubleshooting** - Reset network stack, flush DNS, network diagnostics
2. **Bluetooth Management** - Service restart, driver check, stack reset
3. **Audio System Repair** - Service restart, device detection, troubleshooting
4. **Display & Graphics** - Settings reset, driver refresh, monitor detection
5. **Storage Optimization** - Disk cleanup, registry cleanup, temp file removal
6. **Performance Tuning** - Memory optimization, startup management, monitoring

### Hidden/Conditional Features
- **Registry Operations**: Only available with administrator privileges
- **Service Management**: Requires UAC elevation
- **System File Repair**: Admin access required for SFC/DISM operations
- **Advanced Cleanup**: Full cleanup features need elevation

## Background Usage Verification
**No background audio usage** - Application does not use audio in background
- System tray integration for UI access only
- No continuous audio processing
- Audio features only active during user-initiated diagnostics

## Security & Privacy
- **No data collection or transmission**
- **All operations performed locally**
- **No telemetry or usage statistics**
- **GDPR compliant - no personal data processed**

## System Requirements
- Windows 10 Build 1809+ or Windows 11
- x64 architecture only
- 4GB RAM minimum (8GB recommended)
- Administrator privileges recommended for full functionality

## Verification Steps
1. Install application via APPX package
2. Launch from Start Menu
3. Verify dark theme interface loads correctly
4. Test basic diagnostics without elevation
5. Run as administrator to verify full feature access
6. Confirm system tray integration works
7. Test keyboard shortcuts (Ctrl+Q, F5, F1)
8. Verify no background audio or network activity when idle

## Compliance Notes
- Passes Windows App Certification Kit (WACK)
- Code signing ready
- Accessibility features implemented
- High contrast theme support
- Keyboard navigation support
