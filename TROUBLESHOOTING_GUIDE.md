# PC Troubleshooter Guide

## Quick Start

1. **Run as Administrator** (recommended)
   - Right-click on `launch.bat` and select "Run as administrator"
   - This ensures all troubleshooting scripts have proper permissions

2. **Select Category**
   - Choose from Network, Bluetooth, Audio, Display, Storage, or Performance
   - Each category contains specific troubleshooting tools

3. **Run Individual Tools**
   - Click on any tool button to run specific diagnostics or fixes
   - Confirm the action when prompted

4. **Monitor Output**
   - Watch the console output for real-time results
   - Look for SUCCESS/ERROR messages

5. **Export Logs**
   - Use the "Export Logs" button to save results for later analysis

## Common Issues and Solutions

### Network Problems
- **No Internet Connection**: Run "Reset Network Stack" then restart computer
- **Slow Internet**: Run "Flush DNS Cache" and "Network Diagnostics"
- **WiFi Issues**: Use "Reset Network Adapter"

### Audio Problems
- **No Sound**: Run "Restart Audio Services" and "Audio Device Detection"
- **Audio Stuttering**: Use "Audio Troubleshooter"

### Bluetooth Issues
- **Can't Pair Devices**: Run "Reset Bluetooth Stack"
- **Bluetooth Service Errors**: Use "Restart Bluetooth Service"

### Display Problems
- **Multiple Monitor Issues**: Run "Monitor Detection"
- **Graphics Issues**: Use "Reset Graphics Driver" (may cause temporary screen flicker)

### Performance Issues
- **Slow Startup**: Check "List Startup Programs" and disable unnecessary items
- **High Memory Usage**: Run "Memory Usage Check" to identify problematic processes
- **System Corruption**: Use "System File Check" to scan and repair

### Storage Issues
- **Low Disk Space**: Run "Clear Temp Files" and "Disk Cleanup"
- **Want Storage Analysis**: Use "Check Disk Space"

## Script Descriptions

### Network Scripts
- **network_reset.bat**: Resets Winsock catalog and TCP/IP stack
- **flush_dns.bat**: Clears DNS resolver cache
- **reset_adapter.bat**: Disables and re-enables network adapters
- **network_diagnostics.bat**: Comprehensive network connectivity tests

### Bluetooth Scripts
- **bluetooth_restart.bat**: Restarts all Bluetooth-related services
- **bluetooth_drivers.bat**: Checks Bluetooth device status and drivers
- **bluetooth_reset.bat**: Complete Bluetooth stack reset (removes pairings)

### Audio Scripts
- **audio_restart.bat**: Restarts Windows audio services
- **audio_detect.bat**: Detects and lists all audio devices
- **audio_troubleshoot.bat**: Runs Windows audio troubleshooter

### Display Scripts
- **display_check.bat**: Shows current display configuration
- **graphics_reset.bat**: Resets graphics drivers (TDR reset)
- **monitor_detect.bat**: Forces detection of connected monitors

### Storage Scripts
- **clear_temp.bat**: Removes temporary files and caches
- **disk_cleanup.bat**: Comprehensive disk cleanup including system files
- **disk_space.bat**: Analyzes disk usage and large files

### Performance Scripts
- **startup_programs.bat**: Lists all programs that start with Windows
- **memory_check.bat**: Analyzes RAM usage and potential memory leaks
- **sfc_scan.bat**: Scans for and repairs corrupt system files
- **performance_monitor.bat**: Real-time system performance overview

## Tips for Best Results

1. **Run as Administrator**: Many system-level operations require elevated privileges
2. **Close Running Applications**: Some fixes work better with minimal running programs
3. **Restart After Major Changes**: Network and driver resets often require a restart
4. **Backup Important Data**: Before running system file repairs or major cleanups
5. **Read Console Output**: Check for error messages and follow suggested actions

## When to Use Each Category

### Use Network Tools When:
- Internet connection is slow or not working
- Websites won't load or load slowly
- Network adapters show errors
- DNS resolution problems

### Use Bluetooth Tools When:
- Devices won't pair or connect
- Bluetooth audio is choppy
- Bluetooth service won't start
- Devices keep disconnecting

### Use Audio Tools When:
- No sound from speakers or headphones
- Audio quality issues or crackling
- Microphone not working
- Audio devices not detected

### Use Display Tools When:
- Multiple monitors not detected
- Display flickering or artifacts
- Wrong resolution or refresh rate
- Graphics driver crashes

### Use Storage Tools When:
- Computer running slow due to full disk
- Need to free up space quickly
- Want to analyze what's using disk space
- Regular maintenance cleanup

### Use Performance Tools When:
- Computer starts slowly
- High CPU or memory usage
- System feels sluggish
- Suspicious of system file corruption

## Safety Notes

- **Always backup important data** before running system-level fixes
- **Create a system restore point** before major changes
- **Run as administrator** for full functionality
- **Some operations may temporarily affect system performance**
- **Bluetooth reset will remove all paired devices**
- **Graphics reset may cause temporary screen flickering**

## Troubleshooting the Troubleshooter

If the application won't start:
1. Ensure Python 3.7+ is installed
2. Install PyQt6: `pip install PyQt6`
3. Check for error messages in the console
4. Try running from command line: `python main.py`

If scripts fail to run:
1. Run the application as administrator
2. Check Windows version compatibility
3. Ensure required services are running
4. Check for antivirus interference
