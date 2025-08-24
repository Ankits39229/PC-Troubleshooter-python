# PC Troubleshooter - Python (PyQt6 + Batch)

I want you to generate a **Windows desktop application** called **"PC Troubleshooter"** using **Python + PyQt** for the UI, and **Batch scripts** for troubleshooting tasks.  

The application should allow users to diagnose and fix **common computer problems** (network, Bluetooth, audio, display, storage, performance issues, etc.).  

---

## Requirements

### UI/UX
- Built using **PyQt6**.  
- A main **dashboard window** with categorized troubleshooting options:  
  - **Network**
  - **Bluetooth**
  - **Audio**
  - **Display**
  - **Storage**
  - **Performance**
- Each category should have **buttons/cards** leading to troubleshooting tools.  
- A **console-like output window** (QTextEdit) to show script results in real-time.  
- Dark + Light theme support.  

### Functionality
- Each troubleshooting action is linked to a **Batch/PowerShell script** stored in a `scripts/` folder.  
- **Example Tasks**:  
  - **Network Troubleshooting**: Reset Winsock, flush DNS, restart adapter.  
  - **Bluetooth Troubleshooting**: Restart Bluetooth service, check driver status.  
  - **Audio Troubleshooting**: Restart Windows Audio service, detect audio devices.  
  - **Display Troubleshooting**: Detect display settings, reset graphics driver.  
  - **Storage/Performance**: Clear temp files, check disk usage, list startup apps.  

### Implementation Details
- Use **Python `subprocess`** to run scripts and capture their output in real-time.  
- All scripts should be placed inside the `scripts/` folder and called dynamically.  
- Provide a **“Run All Basic Fixes”** button that executes multiple scripts sequentially.  
- Add **export logs** functionality (save troubleshooting logs as `.txt`).  
- Error handling and confirmation dialogs before running sensitive commands.  

---

