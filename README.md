# PC Troubleshooter

A Windows desktop application for diagnosing and fixing common computer problems.

## Features

- **Network Troubleshooting**: Reset network stack, flush DNS, restart adapters
- **Bluetooth Troubleshooting**: Restart services, check drivers, reset stack
- **Audio Troubleshooting**: Restart services, detect devices, run diagnostics
- **Display Troubleshooting**: Check settings, reset graphics drivers, detect monitors
- **Storage Cleanup**: Clear temp files, disk cleanup, check disk space
- **Performance Analysis**: Check startup programs, memory usage, system files

## Requirements

- Windows 10/11
- Python 3.7+
- PyQt6
- Administrator privileges (recommended for some operations)

## Installation

1. Clone or download this repository
2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Select a troubleshooting category from the left panel
3. Click on specific tools to run diagnostics or fixes
4. Monitor the output in the console on the right
5. Export logs if needed for further analysis

## Application Features

- **Dark/Light Theme Support**: Toggle between themes via View menu
- **Real-time Output**: See script results as they execute
- **Log Export**: Save troubleshooting logs as text files
- **Safety Confirmations**: Confirm before running potentially system-changing operations
- **Run All Basic Fixes**: Execute common fixes in sequence

## Script Categories

### Network

- Reset Network Stack
- Flush DNS Cache
- Reset Network Adapter
- Network Diagnostics

### Bluetooth

- Restart Bluetooth Service
- Check Bluetooth Drivers
- Reset Bluetooth Stack

### Audio

- Restart Audio Services
- Audio Device Detection
- Audio Troubleshooter

### Display

- Display Settings Check
- Reset Graphics Driver
- Monitor Detection

### Storage

- Clear Temp Files
- Disk Cleanup
- Check Disk Space

### Performance

- List Startup Programs
- Memory Usage Check
- System File Check
- Performance Monitor

## Important Notes

- Some operations require administrator privileges
- Always create a system backup before running major fixes
- The application uses Windows built-in tools and commands
- Some scripts may temporarily affect system performance during execution

## Troubleshooting

If you encounter issues:

1. Run as Administrator
2. Check Windows version compatibility
3. Ensure all dependencies are installed
4. Review the console output for error messages

## License

This project is provided as-is for educational and troubleshooting purposes.
