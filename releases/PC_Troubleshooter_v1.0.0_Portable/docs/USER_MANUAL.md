# PC Troubleshooter v1.0 - User Manual

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
5. [GUI Interface Guide](#gui-interface-guide)
6. [CLI Interface Guide](#cli-interface-guide)
7. [Troubleshooting Categories](#troubleshooting-categories)
8. [Advanced Features](#advanced-features)
9. [Keyboard Shortcuts](#keyboard-shortcuts)
10. [Troubleshooting](#troubleshooting)
11. [Support](#support)

---

## 📋 Introduction

PC Troubleshooter v1.0 is a professional system diagnostic and repair tool designed for IT professionals and power users. It provides automated solutions for common Windows system issues across multiple categories including network connectivity, audio problems, display issues, storage optimization, and performance tuning.

### Key Features
- **20+ Automated Diagnostic Scripts** across 6 categories
- **Professional Dark Theme Interface** with real-time monitoring
- **System Tray Integration** for background operation
- **Keyboard Shortcuts** for power users
- **Progress Tracking** with detailed logging
- **Administrator Privileges** support for system-level repairs

---

## 💻 System Requirements

### Minimum Requirements
- **Operating System**: Windows 10 (Build 1809) or Windows 11
- **Python**: Python 3.8 or higher
- **RAM**: 4 GB minimum, 8 GB recommended
- **Storage**: 500 MB free space
- **Display**: 1024x768 minimum resolution

### Recommended Requirements
- **Operating System**: Windows 11 (latest updates)
- **Python**: Python 3.11 or higher
- **RAM**: 8 GB or more
- **Storage**: 1 GB free space
- **Display**: 1920x1080 or higher
- **Privileges**: Administrator account for full functionality

### Dependencies
- **PyQt6**: GUI framework (automatically installed)
- **Windows PowerShell**: Built-in Windows component
- **Batch Script Support**: Native Windows support

---

## 🚀 Installation

### Method 1: Direct Installation
1. **Download** the PC Troubleshooter package
2. **Extract** to your desired location (e.g., `C:\Tools\PCTroubleshooter\`)
3. **Right-click** on `install_dependencies.bat` and select "Run as Administrator"
4. Wait for dependency installation to complete
5. **Launch** the application using `launch.bat`

### Method 2: Python Environment
1. **Open Command Prompt** as Administrator
2. **Navigate** to the application directory:
   ```cmd
   cd C:\path\to\app3
   ```
3. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```cmd
   python main.py
   ```

### Method 3: Standalone Executable (Coming Soon)
- Download the standalone `.exe` file
- No Python installation required
- Double-click to run

---

## 🎯 Getting Started

### First Launch
1. **Run as Administrator** for full functionality
2. The application will display a welcome screen with system status
3. **Review the status dashboard** at the top showing:
   - System Status (Ready/Running/Error)
   - Scripts Run counter
   - Success Rate percentage
   - Active Tasks count

### Quick Start Guide
1. **Select a category** from the left panel (Network, Audio, Display, etc.)
2. **Choose a specific tool** from the category list
3. **Click the tool button** to see description and run options
4. **Confirm execution** in the dialog box
5. **Monitor progress** in the console output area
6. **Review results** and logs for completion status

### Safety Features
- **Confirmation dialogs** before running any script
- **Progress tracking** with real-time output
- **Emergency stop** button (🛑) for immediate halt
- **Backup recommendations** before major changes
- **Detailed logging** of all operations

---

## 🖥️ GUI Interface Guide

### Main Interface Layout

#### 1. Status Dashboard (Top Panel)
- **System Status Card**: Current system state
- **Scripts Run Card**: Total executed scripts
- **Success Rate Card**: Percentage of successful operations
- **Active Tasks Card**: Currently running operations
- **Emergency Stop Button**: Immediate halt of all operations
- **Refresh Button**: Update system status

#### 2. Category Panel (Left Side)
Six main troubleshooting categories:

**🌐 Network**
- Reset Network Stack
- Flush DNS Cache
- Reset TCP/IP Settings
- Network Adapter Troubleshooter

**📶 Bluetooth**
- Restart Bluetooth Service
- Reset Bluetooth Stack
- Device Discovery Troubleshooter

**🔊 Audio**
- Restart Audio Service
- Reset Audio Devices
- Audio Troubleshooter
- Microphone Troubleshooter

**🖥️ Display**
- Reset Display Settings
- Graphics Driver Refresh
- Multi-Monitor Setup
- Display Troubleshooter

**💾 Storage**
- Disk Cleanup
- Registry Cleanup
- Temporary Files Cleanup
- System File Checker

**⚡ Performance**
- Memory Optimization
- Startup Program Manager
- System Performance Scan
- Resource Monitor

#### 3. Console Output (Right Side)
- **Real-time output** from running scripts
- **Colored status indicators**: ✅ Success, ❌ Error, 🔄 Running
- **Scrollable history** of all operations
- **Copy/paste support** for sharing logs
- **Auto-scroll** to latest output

#### 4. Status Bar (Bottom)
- **Current operation status**
- **Detailed metrics**: Scripts run, success rate, active tasks
- **Progress indicators** for running operations
- **Ready state** when idle

### Interface Interactions

#### Button Behaviors
- **Hover Effects**: Smooth color transitions and visual feedback
- **Click Animations**: Professional button press effects
- **Disabled States**: Grayed out when operations are running
- **Tooltip Support**: Detailed descriptions on hover

#### Window Management
- **Resizable Panels**: Drag the splitter to adjust panel sizes
- **Minimize to Tray**: Click the minimize button for background operation
- **Always on Top**: Available through system tray menu
- **Full Screen**: Maximize for detailed monitoring

---

## 💻 CLI Interface Guide

### Command Line Usage

#### Basic Syntax
```cmd
python main.py [options] [script_name]
```

#### Command Line Options
```cmd
--help, -h          Show help message and exit
--list, -l          List all available scripts
--category, -c      Filter scripts by category
--run, -r           Run specific script
--batch, -b         Run multiple scripts in sequence
--log, -L           Specify log file location
--silent, -s        Run without GUI (silent mode)
--admin, -a         Request administrator privileges
```

#### Examples

**List all available scripts:**
```cmd
python main.py --list
```

**List scripts by category:**
```cmd
python main.py --category network
```

**Run specific script:**
```cmd
python main.py --run "reset_network_stack"
```

**Run multiple scripts:**
```cmd
python main.py --batch "reset_dns,flush_cache,restart_audio"
```

**Silent mode with logging:**
```cmd
python main.py --silent --run "disk_cleanup" --log "C:\Logs\pc_troubleshooter.log"
```

### Batch Operations

#### Script Files
Create `.txt` files with script names (one per line):

**network_repair.txt:**
```
reset_network_stack
flush_dns_cache
reset_tcpip_settings
network_troubleshooter
```

**Run batch file:**
```cmd
python main.py --batch-file "network_repair.txt"
```

#### Return Codes
- **0**: Success - All operations completed successfully
- **1**: Partial Failure - Some operations failed
- **2**: Complete Failure - All operations failed
- **3**: User Cancelled - Operations cancelled by user
- **4**: Permission Error - Administrator privileges required

---

## 🔧 Troubleshooting Categories

### 🌐 Network Category

#### Reset Network Stack
**Purpose**: Resets Windows network stack to default settings
**Use Case**: When experiencing connection issues, IP conflicts, or network adapter problems
**Actions**:
- Resets Winsock catalog
- Resets TCP/IP stack
- Clears ARP cache
- Restarts network adapters

**Command**: `netsh winsock reset && netsh int ip reset`

#### Flush DNS Cache
**Purpose**: Clears DNS resolver cache
**Use Case**: When websites won't load or DNS resolution is slow
**Actions**:
- Flushes DNS cache
- Releases and renews IP configuration
- Registers DNS names

**Command**: `ipconfig /flushdns && ipconfig /release && ipconfig /renew`

#### Reset TCP/IP Settings
**Purpose**: Resets TCP/IP configuration to defaults
**Use Case**: When experiencing network connectivity issues or incorrect network settings
**Actions**:
- Resets TCP/IP stack
- Restores default firewall rules
- Resets network adapter settings

### 📶 Bluetooth Category

#### Restart Bluetooth Service
**Purpose**: Restarts Windows Bluetooth services
**Use Case**: When Bluetooth devices won't connect or are not discovered
**Actions**:
- Stops Bluetooth Support Service
- Clears Bluetooth cache
- Restarts Bluetooth services

#### Reset Bluetooth Stack
**Purpose**: Completely resets Bluetooth stack
**Use Case**: When Bluetooth is completely non-functional
**Actions**:
- Removes Bluetooth device cache
- Resets Bluetooth registry entries
- Reinstalls Bluetooth stack

### 🔊 Audio Category

#### Restart Audio Service
**Purpose**: Restarts Windows Audio services
**Use Case**: When audio devices are not working or producing no sound
**Actions**:
- Stops Windows Audio service
- Stops Windows Audio Endpoint Builder
- Restarts audio services in correct order

#### Reset Audio Devices
**Purpose**: Resets audio device configuration
**Use Case**: When audio devices are not recognized or misconfigured
**Actions**:
- Removes audio device cache
- Resets audio driver configuration
- Refreshes audio device list

### 🖥️ Display Category

#### Reset Display Settings
**Purpose**: Resets display configuration to defaults
**Use Case**: When experiencing display issues, incorrect resolution, or multi-monitor problems
**Actions**:
- Resets display scaling
- Restores default resolution
- Clears display cache

#### Graphics Driver Refresh
**Purpose**: Refreshes graphics driver without restart
**Use Case**: When experiencing graphics glitches or driver issues
**Actions**:
- Restarts graphics driver
- Clears graphics cache
- Refreshes display adapters

### 💾 Storage Category

#### Disk Cleanup
**Purpose**: Cleans temporary files and system cache
**Use Case**: When running low on disk space or system is slow
**Actions**:
- Cleans temporary files
- Removes system cache
- Empties recycle bin
- Cleans Windows update cache

#### System File Checker
**Purpose**: Scans and repairs system files
**Use Case**: When system files are corrupted or missing
**Actions**:
- Runs SFC scan
- Repairs corrupted files
- Checks system integrity

### ⚡ Performance Category

#### Memory Optimization
**Purpose**: Optimizes system memory usage
**Use Case**: When system is running slowly or using excessive memory
**Actions**:
- Clears memory cache
- Optimizes virtual memory
- Reduces memory fragmentation

#### Startup Program Manager
**Purpose**: Manages startup programs for faster boot
**Use Case**: When system takes too long to start or has too many startup programs
**Actions**:
- Lists startup programs
- Provides optimization recommendations
- Allows startup program management

---

## ⚡ Advanced Features

### System Tray Integration

#### Background Operation
- **Minimize to Tray**: Application continues running in background
- **Quick Access Menu**: Right-click tray icon for quick actions
- **Status Notifications**: Toast notifications for completed operations
- **Always Available**: Access troubleshooting tools without opening main window

#### Tray Menu Options
- **Show PC Troubleshooter**: Restore main window
- **Quick System Scan**: Run basic diagnostic scan
- **Recent Operations**: View last 5 operations
- **Exit**: Close application completely

### Real-Time Monitoring

#### Status Dashboard
- **Live Updates**: Status cards update every 5 seconds
- **Performance Metrics**: CPU and memory usage (when available)
- **Operation Tracking**: Real-time count of scripts run and success rate
- **System Health**: Overall system status indicator

#### Progress Tracking
- **Visual Progress Bars**: Show completion percentage
- **Real-Time Output**: Live command output in console
- **Operation History**: Complete log of all operations
- **Error Detection**: Automatic error highlighting and reporting

### Professional Features

#### Keyboard Shortcuts
- **Global Shortcuts**: Work even when application is minimized
- **Context Sensitive**: Different shortcuts in different modes
- **Customizable**: User can modify shortcut preferences
- **Help Integration**: F1 for context-sensitive help

#### Logging System
- **Comprehensive Logs**: Every operation is logged with timestamp
- **Log Rotation**: Automatic log file management
- **Export Options**: Export logs in multiple formats
- **Search Functionality**: Find specific operations in logs

---

## ⌨️ Keyboard Shortcuts

### Global Shortcuts (Work Anywhere)
| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl + Q` | Quick System Scan | Runs basic diagnostic scan |
| `Ctrl + Shift + S` | Emergency Stop | Immediately halts all operations |
| `F5` | Refresh Status | Updates system status and metrics |
| `F1` | Show Help | Displays help dialog with shortcuts |

### Application Shortcuts (When Window is Active)
| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl + L` | Clear Console | Clears the output console |
| `Ctrl + N` | New Operation | Shows operation selection dialog |
| `Ctrl + S` | Save Logs | Saves current logs to file |
| `Ctrl + O` | Open Logs | Opens existing log file |
| `Ctrl + E` | Export Report | Exports operation report |
| `Escape` | Cancel Operation | Cancels current running operation |

### Navigation Shortcuts
| Shortcut | Action | Description |
|----------|--------|-------------|
| `Tab` | Next Category | Moves to next troubleshooting category |
| `Shift + Tab` | Previous Category | Moves to previous category |
| `Enter` | Run Selected | Runs currently selected tool |
| `Space` | Toggle Selection | Toggles tool selection |
| `Ctrl + A` | Select All | Selects all tools in category |

### Window Management
| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl + M` | Minimize to Tray | Minimizes application to system tray |
| `Alt + F4` | Close Application | Closes the application |
| `F11` | Toggle Fullscreen | Toggles fullscreen mode |
| `Ctrl + +` | Increase Font Size | Makes console text larger |
| `Ctrl + -` | Decrease Font Size | Makes console text smaller |

---

## 🔧 Troubleshooting

### Common Issues

#### Application Won't Start
**Symptoms**: Double-clicking does nothing or error messages appear
**Solutions**:
1. **Check Python Installation**: Ensure Python 3.8+ is installed
2. **Run as Administrator**: Right-click and "Run as Administrator"
3. **Install Dependencies**: Run `pip install -r requirements.txt`
4. **Check System Requirements**: Verify Windows 10/11 compatibility

#### Scripts Fail to Execute
**Symptoms**: Scripts show error messages or don't complete
**Solutions**:
1. **Administrator Privileges**: Ensure application is run as Administrator
2. **Check Script Path**: Verify scripts folder exists and contains .bat files
3. **Antivirus Interference**: Temporarily disable antivirus or add exception
4. **Windows Updates**: Ensure Windows is up to date

#### GUI Issues
**Symptoms**: Interface appears corrupted or doesn't respond
**Solutions**:
1. **Update Graphics Drivers**: Install latest graphics drivers
2. **Check Display Scaling**: Set display scaling to 100% temporarily
3. **Reset Settings**: Delete settings file to restore defaults
4. **Clear Cache**: Clear application cache and restart

#### Performance Issues
**Symptoms**: Application runs slowly or uses excessive resources
**Solutions**:
1. **Close Other Applications**: Free up system resources
2. **Check Available Memory**: Ensure sufficient RAM is available
3. **Disk Space**: Verify adequate free disk space
4. **Background Processes**: Close unnecessary background processes

### Error Codes

#### Script Execution Errors
- **Error 1**: Permission Denied - Run as Administrator
- **Error 2**: File Not Found - Check script installation
- **Error 3**: Access Denied - Verify user permissions
- **Error 5**: System Error - Restart Windows and try again

#### Application Errors
- **GUI-001**: Interface Initialization Failed - Update PyQt6
- **NET-001**: Network Operation Failed - Check internet connection
- **SYS-001**: System Access Denied - Run as Administrator
- **LOG-001**: Logging Error - Check disk space and permissions

### Getting Help

#### Built-in Help
- Press `F1` for keyboard shortcuts
- Hover over buttons for tooltips
- Check status bar for operation details
- Review console output for detailed information

#### Log Files
Log files are stored in: `%APPDATA%\PCTroubleshooter\logs\`
- `application.log`: General application logs
- `operations.log`: Script execution logs
- `error.log`: Error and exception logs
- `debug.log`: Detailed debugging information

#### Support Resources
- **GitHub Repository**: Latest updates and issue tracking
- **Documentation**: Comprehensive guides and tutorials
- **Community Forum**: User discussions and solutions
- **Video Tutorials**: Step-by-step visual guides

---

## 📞 Support

### Contact Information
- **Project Repository**: [GitHub Link]
- **Documentation**: [Wiki Link]
- **Issue Tracker**: [Issues Link]
- **Community Forum**: [Forum Link]

### Reporting Issues
When reporting issues, please include:
1. **System Information**: Windows version, Python version
2. **Error Messages**: Complete error text or screenshots
3. **Steps to Reproduce**: Detailed steps that cause the issue
4. **Log Files**: Relevant log file contents
5. **Expected Behavior**: What should happen vs. what actually happens

### Contributing
We welcome contributions from the community:
- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality
- **Code Contributions**: Submit pull requests
- **Documentation**: Improve guides and tutorials
- **Testing**: Help test new features and releases

### License
PC Troubleshooter is released under the MIT License. See LICENSE file for details.

---

**PC Troubleshooter v1.0 - Professional System Diagnostics**  
*Making Windows troubleshooting simple and effective*

*Last Updated: August 24, 2025*
