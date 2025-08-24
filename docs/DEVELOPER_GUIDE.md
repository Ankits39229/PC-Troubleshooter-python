# PC Troubleshooter v1.0 - Developer Documentation

## 📚 Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Project Structure](#project-structure)
3. [API Reference](#api-reference)
4. [Core Components](#core-components)
5. [Extension Development](#extension-development)
6. [Build Process](#build-process)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [Troubleshooting Development Issues](#troubleshooting-development-issues)

---

## 🏗️ Architecture Overview

### Technology Stack
- **Frontend**: PyQt6 for cross-platform GUI
- **Backend**: Python 3.8+ with threading support
- **Scripts**: Windows Batch (.bat) and PowerShell (.ps1)
- **Logging**: Python logging module with file rotation
- **Configuration**: JSON-based configuration files

### Design Patterns
- **Model-View-Controller (MVC)**: Separation of UI, logic, and data
- **Observer Pattern**: Real-time status updates and notifications
- **Command Pattern**: Script execution with undo/redo capabilities
- **Factory Pattern**: Dynamic script loading and execution
- **Singleton Pattern**: Application configuration and logging

### Core Architecture

```
PC Troubleshooter Application
├── main.py (Entry Point)
├── ui/ (User Interface Layer)
│   ├── main_window.py (Main GUI Controller)
│   ├── custom_widgets.py (Custom UI Components)
│   └── themes/ (UI Themes and Styling)
├── core/ (Business Logic Layer)
│   ├── script_runner.py (Script Execution Engine)
│   ├── config_manager.py (Configuration Management)
│   └── logger.py (Logging System)
├── scripts/ (Diagnostic Scripts)
│   ├── network/ (Network Troubleshooting)
│   ├── audio/ (Audio Troubleshooting)
│   ├── display/ (Display Troubleshooting)
│   ├── bluetooth/ (Bluetooth Troubleshooting)
│   ├── storage/ (Storage Troubleshooting)
│   └── performance/ (Performance Optimization)
└── utils/ (Utility Functions)
    ├── system_info.py (System Information)
    ├── admin_check.py (Privilege Verification)
    └── file_utils.py (File Operations)
```

---

## 📁 Project Structure

### Directory Layout

```
app3/
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── README.md                  # Project overview
├── LICENSE                    # License information
├── setup.py                   # Installation script
├── ui/                        # User Interface Module
│   ├── __init__.py
│   ├── main_window.py         # Main application window
│   ├── custom_widgets.py      # Custom UI components
│   ├── dialogs/               # Dialog windows
│   │   ├── about_dialog.py
│   │   ├── settings_dialog.py
│   │   └── help_dialog.py
│   └── themes/                # UI themes
│       ├── dark_theme.qss
│       └── light_theme.qss
├── core/                      # Core Business Logic
│   ├── __init__.py
│   ├── script_runner.py       # Script execution engine
│   ├── config_manager.py      # Configuration management
│   ├── logger.py              # Logging system
│   └── exceptions.py          # Custom exceptions
├── scripts/                   # Diagnostic Scripts
│   ├── network/               # Network troubleshooting
│   │   ├── reset_network_stack.bat
│   │   ├── flush_dns_cache.bat
│   │   ├── reset_tcpip_settings.bat
│   │   └── network_troubleshooter.bat
│   ├── audio/                 # Audio troubleshooting
│   │   ├── restart_audio_service.bat
│   │   ├── reset_audio_devices.bat
│   │   ├── audio_troubleshooter.bat
│   │   └── microphone_troubleshooter.bat
│   ├── display/               # Display troubleshooting
│   │   ├── reset_display_settings.bat
│   │   ├── graphics_driver_refresh.bat
│   │   ├── multi_monitor_setup.bat
│   │   └── display_troubleshooter.bat
│   ├── bluetooth/             # Bluetooth troubleshooting
│   │   ├── restart_bluetooth_service.bat
│   │   ├── reset_bluetooth_stack.bat
│   │   └── bluetooth_troubleshooter.bat
│   ├── storage/               # Storage optimization
│   │   ├── disk_cleanup.bat
│   │   ├── registry_cleanup.bat
│   │   ├── temp_files_cleanup.bat
│   │   └── system_file_checker.bat
│   └── performance/           # Performance optimization
│       ├── memory_optimization.bat
│       ├── startup_manager.bat
│       ├── performance_scan.bat
│       └── resource_monitor.bat
├── utils/                     # Utility Functions
│   ├── __init__.py
│   ├── system_info.py         # System information gathering
│   ├── admin_check.py         # Administrator privilege checking
│   ├── file_utils.py          # File operation utilities
│   └── registry_utils.py      # Windows registry operations
├── tests/                     # Test Suite
│   ├── __init__.py
│   ├── test_script_runner.py
│   ├── test_config_manager.py
│   └── test_ui_components.py
├── docs/                      # Documentation
│   ├── USER_MANUAL.md
│   ├── DEVELOPER_GUIDE.md
│   ├── API_REFERENCE.md
│   └── DEPLOYMENT_GUIDE.md
├── build/                     # Build artifacts
│   ├── windows/
│   ├── portable/
│   └── installer/
└── config/                    # Configuration files
    ├── settings.json
    ├── script_definitions.json
    └── themes.json
```

---

## 📖 API Reference

### Core Classes

#### MainWindow Class
```python
class MainWindow(QMainWindow):
    """Main application window controller"""
    
    def __init__(self):
        """Initialize the main window"""
        
    def setup_ui(self):
        """Setup the user interface components"""
        
    def run_script(self, script_file: str, tool_name: str):
        """Execute a diagnostic script"""
        
    def update_status(self, status: str):
        """Update the application status"""
```

#### ScriptRunner Class
```python
class ScriptRunner(QThread):
    """Thread-based script execution engine"""
    
    # Signals
    output_received = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)
    progress_update = pyqtSignal(int)
    
    def __init__(self, script_path: str, script_name: str):
        """Initialize script runner"""
        
    def run(self):
        """Execute the script in a separate thread"""
```

#### ProfessionalButton Class
```python
class ProfessionalButton(QPushButton):
    """Custom button with professional styling and animations"""
    
    def __init__(self, text: str = "", icon: str = "", parent=None):
        """Initialize professional button"""
        
    def setup_animation(self):
        """Setup hover animations"""
        
    def setup_styling(self):
        """Apply professional styling"""
```

#### StatusCard Class
```python
class StatusCard(QFrame):
    """Real-time status monitoring card"""
    
    def __init__(self, title: str, value: str, icon: str, parent=None):
        """Initialize status card"""
        
    def update_value(self, new_value: str):
        """Update card value with animation"""
```

### Utility Functions

#### System Information
```python
def get_system_info() -> dict:
    """Get comprehensive system information"""
    return {
        'os_version': str,
        'python_version': str,
        'architecture': str,
        'memory_total': int,
        'memory_available': int,
        'cpu_count': int,
        'disk_space': dict
    }

def is_admin() -> bool:
    """Check if running with administrator privileges"""
    
def get_installed_software() -> list:
    """Get list of installed software"""
```

#### File Operations
```python
def ensure_directory_exists(path: str) -> bool:
    """Ensure directory exists, create if necessary"""
    
def safe_file_operation(operation: callable, *args, **kwargs):
    """Safely perform file operations with error handling"""
    
def backup_file(file_path: str, backup_dir: str) -> str:
    """Create backup of file before modification"""
```

#### Registry Operations
```python
def read_registry_value(key: str, value_name: str) -> str:
    """Read value from Windows registry"""
    
def write_registry_value(key: str, value_name: str, value: str) -> bool:
    """Write value to Windows registry"""
    
def delete_registry_value(key: str, value_name: str) -> bool:
    """Delete value from Windows registry"""
```

---

## 🧩 Core Components

### Script Execution Engine

#### Design
The script execution engine is built around the `ScriptRunner` class that inherits from `QThread` for non-blocking execution:

```python
class ScriptRunner(QThread):
    """Enhanced thread for running scripts with progress tracking"""
    
    # Signal definitions
    output_received = pyqtSignal(str)      # Real-time output
    finished_signal = pyqtSignal(bool, str)  # Completion status
    progress_update = pyqtSignal(int)      # Progress percentage
    
    def __init__(self, script_path, script_name):
        super().__init__()
        self.script_path = script_path
        self.script_name = script_name
        self.progress = 0
    
    def run(self):
        """Execute script with real-time output capture"""
        try:
            # Create process with proper settings
            process = subprocess.Popen(
                self.script_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Capture output in real-time
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.output_received.emit(output.strip())
                    self.progress += 5  # Simulated progress
                    self.progress_update.emit(min(self.progress, 95))
            
            # Wait for completion and emit final status
            return_code = process.wait()
            self.progress_update.emit(100)
            
            if return_code == 0:
                self.finished_signal.emit(True, f"✅ {self.script_name} completed successfully")
            else:
                self.finished_signal.emit(False, f"❌ {self.script_name} failed with return code {return_code}")
                
        except Exception as e:
            self.finished_signal.emit(False, f"💥 Error running {self.script_name}: {str(e)}")
```

### Configuration Management

#### Configuration Structure
```json
{
  "application": {
    "theme": "dark",
    "auto_scroll": true,
    "confirm_actions": true,
    "log_level": "INFO",
    "max_log_files": 10,
    "backup_before_changes": true
  },
  "ui": {
    "window_geometry": {
      "x": 100,
      "y": 100,
      "width": 1400,
      "height": 900
    },
    "splitter_sizes": [560, 840],
    "status_cards_enabled": true,
    "system_tray_enabled": true
  },
  "scripts": {
    "timeout_seconds": 300,
    "require_admin": true,
    "backup_registry": true,
    "create_restore_point": false
  },
  "logging": {
    "console_level": "INFO",
    "file_level": "DEBUG",
    "max_file_size": "10MB",
    "log_directory": "%APPDATA%\\PCTroubleshooter\\logs"
  }
}
```

#### Configuration Manager Class
```python
class ConfigManager:
    """Manages application configuration"""
    
    def __init__(self, config_file: str = "config/settings.json"):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> dict:
        """Load configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.get_default_config()
    
    def save_config(self):
        """Save configuration to file"""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value != {} else default
    
    def set(self, key: str, value):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            config = config.setdefault(k, {})
        config[keys[-1]] = value
        self.save_config()
```

### Logging System

#### Logger Configuration
```python
import logging
import logging.handlers
from datetime import datetime

class PCTroubleshooterLogger:
    """Enhanced logging system for PC Troubleshooter"""
    
    def __init__(self, log_directory: str, max_file_size: int = 10*1024*1024):
        self.log_directory = log_directory
        self.max_file_size = max_file_size
        self.setup_loggers()
    
    def setup_loggers(self):
        """Setup multiple loggers for different purposes"""
        os.makedirs(self.log_directory, exist_ok=True)
        
        # Application logger
        self.app_logger = self.create_logger(
            'application',
            os.path.join(self.log_directory, 'application.log')
        )
        
        # Operations logger
        self.ops_logger = self.create_logger(
            'operations',
            os.path.join(self.log_directory, 'operations.log')
        )
        
        # Error logger
        self.error_logger = self.create_logger(
            'errors',
            os.path.join(self.log_directory, 'errors.log')
        )
    
    def create_logger(self, name: str, log_file: str) -> logging.Logger:
        """Create a logger with file rotation"""
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        # File handler with rotation
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=self.max_file_size,
            backupCount=5
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def log_operation(self, operation: str, status: str, details: str = ""):
        """Log operation with structured format"""
        self.ops_logger.info(f"OPERATION: {operation} | STATUS: {status} | DETAILS: {details}")
    
    def log_error(self, error: str, context: str = ""):
        """Log error with context"""
        self.error_logger.error(f"ERROR: {error} | CONTEXT: {context}")
    
    def log_system_info(self, info: dict):
        """Log system information"""
        self.app_logger.info(f"SYSTEM_INFO: {json.dumps(info, indent=2)}")
```

---

## 🔧 Extension Development

### Creating New Diagnostic Scripts

#### Script Template
```batch
@echo off
REM PC Troubleshooter Script Template
REM Script Name: [SCRIPT_NAME]
REM Category: [CATEGORY]
REM Description: [DESCRIPTION]
REM Author: [AUTHOR]
REM Version: 1.0

echo ======================================
echo PC Troubleshooter - [SCRIPT_NAME]
echo ======================================
echo.

REM Check for administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ERROR: This script requires administrator privileges.
    echo Please run as administrator.
    pause
    exit /b 1
)

echo Starting [SCRIPT_NAME]...
echo.

REM Main script logic goes here
REM Example:
REM echo Step 1: Performing action...
REM [command] >nul 2>&1
REM if %errorLevel% equ 0 (
REM     echo SUCCESS: Action completed
REM ) else (
REM     echo ERROR: Action failed
REM )

REM Final status
echo.
echo ======================================
echo [SCRIPT_NAME] completed
echo ======================================
pause
```

#### Script Registration
Add new scripts to `config/script_definitions.json`:

```json
{
  "scripts": {
    "new_category": {
      "name": "New Category",
      "icon": "🔧",
      "description": "Description of new category",
      "scripts": {
        "new_script": {
          "name": "New Script",
          "description": "Description of what this script does",
          "file": "new_category/new_script.bat",
          "requires_admin": true,
          "estimated_time": "30 seconds",
          "risk_level": "low"
        }
      }
    }
  }
}
```

### Custom Widget Development

#### Creating Custom Widgets
```python
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, QPropertyAnimation, QRect
from PyQt6.QtGui import QFont

class CustomStatusWidget(QWidget):
    """Custom widget for displaying status information"""
    
    status_changed = pyqtSignal(str)  # Custom signal
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_animations()
    
    def setup_ui(self):
        """Setup widget UI"""
        layout = QVBoxLayout(self)
        
        self.title_label = QLabel("Status")
        self.title_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        
        self.value_label = QLabel("Ready")
        self.value_label.setFont(QFont("Segoe UI", 10))
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        
        self.setObjectName("customStatusWidget")
        self.apply_styling()
    
    def setup_animations(self):
        """Setup animations for the widget"""
        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(300)
    
    def apply_styling(self):
        """Apply custom styling"""
        self.setStyleSheet("""
            #customStatusWidget {
                background-color: #2d2d2d;
                border-radius: 8px;
                padding: 10px;
            }
            QLabel {
                color: white;
                border: none;
            }
        """)
    
    def update_status(self, new_status: str):
        """Update status with animation"""
        self.value_label.setText(new_status)
        self.status_changed.emit(new_status)
        
        # Trigger fade animation
        self.fade_animation.setStartValue(0.7)
        self.fade_animation.setEndValue(1.0)
        self.fade_animation.start()
```

### Plugin System

#### Plugin Interface
```python
from abc import ABC, abstractmethod

class PluginInterface(ABC):
    """Interface for PC Troubleshooter plugins"""
    
    @abstractmethod
    def get_name(self) -> str:
        """Return plugin name"""
        pass
    
    @abstractmethod
    def get_version(self) -> str:
        """Return plugin version"""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Return plugin description"""
        pass
    
    @abstractmethod
    def initialize(self, main_window):
        """Initialize plugin with main window reference"""
        pass
    
    @abstractmethod
    def get_menu_items(self) -> list:
        """Return list of menu items to add"""
        pass
    
    @abstractmethod
    def cleanup(self):
        """Cleanup when plugin is unloaded"""
        pass

class ExamplePlugin(PluginInterface):
    """Example plugin implementation"""
    
    def get_name(self) -> str:
        return "Example Plugin"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def get_description(self) -> str:
        return "An example plugin for demonstration"
    
    def initialize(self, main_window):
        self.main_window = main_window
        print(f"Initializing {self.get_name()}")
    
    def get_menu_items(self) -> list:
        return [
            {
                "text": "Example Action",
                "callback": self.example_action,
                "shortcut": "Ctrl+E"
            }
        ]
    
    def example_action(self):
        """Example plugin action"""
        print("Example plugin action executed")
    
    def cleanup(self):
        print(f"Cleaning up {self.get_name()}")
```

---

## 🔨 Build Process

### Development Environment Setup

#### Prerequisites
```bash
# Install Python 3.8+
python --version

# Install required packages
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

#### Development Dependencies (`requirements-dev.txt`)
```
pytest>=7.0.0
pytest-qt>=4.0.0
black>=22.0.0
flake8>=4.0.0
mypy>=0.950
sphinx>=4.0.0
sphinx-rtd-theme>=1.0.0
```

### Building Distributions

#### Standalone Executable
```bash
# Install PyInstaller
pip install pyinstaller

# Create standalone executable
pyinstaller --onefile --windowed --icon=assets/icon.ico main.py

# Create directory-based distribution
pyinstaller --onedir --windowed --icon=assets/icon.ico main.py
```

#### Windows Installer
```bash
# Install NSIS (Nullsoft Scriptable Install System)
# Create installer script (installer.nsi)

# Build installer
makensis installer.nsi
```

#### Portable Version
```python
# build_portable.py
import shutil
import os
import zipfile

def create_portable():
    """Create portable version of PC Troubleshooter"""
    
    # Create build directory
    build_dir = "build/portable"
    os.makedirs(build_dir, exist_ok=True)
    
    # Copy application files
    shutil.copytree(".", f"{build_dir}/PCTroubleshooter", 
                   ignore=shutil.ignore_patterns('build', '.git', '__pycache__'))
    
    # Create launcher script
    launcher_script = """
@echo off
cd /d "%~dp0"
python main.py
pause
"""
    
    with open(f"{build_dir}/PCTroubleshooter/launch.bat", "w") as f:
        f.write(launcher_script)
    
    # Create ZIP archive
    with zipfile.ZipFile(f"{build_dir}/PCTroubleshooter_Portable.zip", "w") as zip_file:
        for root, dirs, files in os.walk(f"{build_dir}/PCTroubleshooter"):
            for file in files:
                zip_file.write(os.path.join(root, file))

if __name__ == "__main__":
    create_portable()
```

---

## 🧪 Testing

### Test Structure

#### Unit Tests
```python
# tests/test_script_runner.py
import unittest
from unittest.mock import Mock, patch
from core.script_runner import ScriptRunner

class TestScriptRunner(unittest.TestCase):
    """Test cases for ScriptRunner class"""
    
    def setUp(self):
        """Setup test environment"""
        self.script_path = "test_script.bat"
        self.script_name = "Test Script"
        self.runner = ScriptRunner(self.script_path, self.script_name)
    
    def test_initialization(self):
        """Test ScriptRunner initialization"""
        self.assertEqual(self.runner.script_path, self.script_path)
        self.assertEqual(self.runner.script_name, self.script_name)
        self.assertEqual(self.runner.progress, 0)
    
    @patch('subprocess.Popen')
    def test_successful_execution(self, mock_popen):
        """Test successful script execution"""
        # Mock process
        mock_process = Mock()
        mock_process.stdout.readline.side_effect = ["Output line 1", "Output line 2", ""]
        mock_process.poll.return_value = None
        mock_process.wait.return_value = 0
        mock_popen.return_value = mock_process
        
        # Connect signal to capture results
        results = []
        self.runner.finished_signal.connect(lambda success, msg: results.append((success, msg)))
        
        # Run test
        self.runner.run()
        
        # Verify results
        self.assertTrue(results[0][0])  # Success
        self.assertIn("completed successfully", results[0][1])
    
    @patch('subprocess.Popen')
    def test_failed_execution(self, mock_popen):
        """Test failed script execution"""
        # Mock process with error
        mock_process = Mock()
        mock_process.stdout.readline.side_effect = ["Error occurred", ""]
        mock_process.poll.return_value = None
        mock_process.wait.return_value = 1
        mock_popen.return_value = mock_process
        
        # Connect signal to capture results
        results = []
        self.runner.finished_signal.connect(lambda success, msg: results.append((success, msg)))
        
        # Run test
        self.runner.run()
        
        # Verify results
        self.assertFalse(results[0][0])  # Failure
        self.assertIn("failed with return code", results[0][1])

if __name__ == "__main__":
    unittest.main()
```

#### GUI Tests
```python
# tests/test_ui_components.py
import pytest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow
from ui.custom_widgets import ProfessionalButton

@pytest.fixture
def app():
    """Create QApplication for testing"""
    return QApplication([])

@pytest.fixture
def main_window(app):
    """Create MainWindow for testing"""
    return MainWindow()

def test_main_window_initialization(main_window):
    """Test main window initialization"""
    assert main_window.windowTitle() == "PC Troubleshooter v1.0 - Professional System Diagnostics [DARK MODE]"
    assert main_window.isVisible() == False

def test_professional_button_creation():
    """Test ProfessionalButton creation"""
    button = ProfessionalButton("Test Button", "🔧")
    assert button.text() == "Test Button"
    assert button.icon_text == "🔧"

def test_button_click_signal(qtbot):
    """Test button click signal"""
    button = ProfessionalButton("Click Me")
    
    # Add to test framework
    qtbot.addWidget(button)
    
    # Track clicks
    clicked = False
    def on_click():
        nonlocal clicked
        clicked = True
    
    button.clicked.connect(on_click)
    
    # Simulate click
    QTest.mouseClick(button, Qt.MouseButton.LeftButton)
    
    assert clicked == True
```

### Integration Tests

#### End-to-End Testing
```python
# tests/test_integration.py
import unittest
import tempfile
import os
from unittest.mock import patch
from main import main
from ui.main_window import MainWindow

class TestIntegration(unittest.TestCase):
    """Integration tests for PC Troubleshooter"""
    
    def setUp(self):
        """Setup test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.temp_dir, "test_config.json")
    
    def test_application_startup(self):
        """Test complete application startup"""
        with patch('sys.argv', ['main.py']):
            # This should not raise any exceptions
            try:
                app = QApplication([])
                window = MainWindow()
                # Verify window is created successfully
                self.assertIsNotNone(window)
                self.assertEqual(window.current_theme, "dark")
            except Exception as e:
                self.fail(f"Application startup failed: {e}")
    
    def test_script_execution_flow(self):
        """Test complete script execution flow"""
        window = MainWindow()
        
        # Mock script file
        test_script = os.path.join(self.temp_dir, "test_script.bat")
        with open(test_script, "w") as f:
            f.write("@echo off\necho Test script executed\n")
        
        # Test script execution
        window.run_script(test_script, "Test Script")
        
        # Verify script runner is created
        self.assertIsNotNone(window.script_runner)
    
    def tearDown(self):
        """Cleanup test environment"""
        import shutil
        shutil.rmtree(self.temp_dir)
```

### Performance Tests

#### Load Testing
```python
# tests/test_performance.py
import time
import threading
from unittest import TestCase
from core.script_runner import ScriptRunner

class TestPerformance(TestCase):
    """Performance tests for PC Troubleshooter"""
    
    def test_multiple_script_execution(self):
        """Test concurrent script execution performance"""
        start_time = time.time()
        
        # Create multiple script runners
        runners = []
        for i in range(5):
            runner = ScriptRunner(f"test_script_{i}.bat", f"Test Script {i}")
            runners.append(runner)
        
        # Start all runners
        for runner in runners:
            runner.start()
        
        # Wait for completion
        for runner in runners:
            runner.wait()
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Performance assertion (should complete within reasonable time)
        self.assertLess(execution_time, 10.0, "Script execution took too long")
    
    def test_memory_usage(self):
        """Test memory usage during operation"""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Perform memory-intensive operations
        window = MainWindow()
        for i in range(100):
            window.update_performance_metrics()
        
        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Memory usage should not increase significantly
        self.assertLess(memory_increase, 50 * 1024 * 1024, "Memory usage increased too much")
```

---

## 🚀 Deployment

### Deployment Checklist

#### Pre-Deployment
- [ ] All tests pass
- [ ] Code review completed
- [ ] Documentation updated
- [ ] Version number incremented
- [ ] Changelog updated
- [ ] Dependencies verified
- [ ] Security scan completed

#### Build Process
- [ ] Clean build environment
- [ ] Generate executable
- [ ] Create installer
- [ ] Test installer on clean system
- [ ] Verify all features work
- [ ] Check file associations
- [ ] Validate shortcuts and registry entries

#### Post-Deployment
- [ ] Update download links
- [ ] Notify users of new version
- [ ] Monitor for issues
- [ ] Update documentation site
- [ ] Create release notes

### Continuous Integration

#### GitHub Actions Workflow
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Run linting
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Run type checking
      run: mypy --ignore-missing-imports .
    
    - name: Run tests
      run: pytest tests/ -v --cov=. --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
  
  build:
    needs: test
    runs-on: windows-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pyinstaller
    
    - name: Build executable
      run: |
        pyinstaller --onefile --windowed --icon=assets/icon.ico main.py
    
    - name: Create installer
      run: |
        # Add NSIS installer build commands here
        echo "Building installer..."
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: PC-Troubleshooter-Windows
        path: dist/
```

---

## 🤝 Contributing

### Development Guidelines

#### Code Style
- Follow PEP 8 for Python code
- Use type hints where appropriate
- Write docstrings for all public methods
- Keep functions small and focused
- Use meaningful variable and function names

#### Commit Guidelines
```
type(scope): short description

Longer description if needed

- Bullet points for changes
- Reference issues: Fixes #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

#### Pull Request Process
1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Update documentation
5. Submit pull request
6. Address review comments
7. Merge after approval

### Adding New Features

#### Feature Development Workflow
1. **Requirements Analysis**
   - Define feature scope
   - Identify dependencies
   - Plan UI/UX changes
   - Write technical specification

2. **Implementation**
   - Create feature branch
   - Implement core functionality
   - Add unit tests
   - Update documentation

3. **Testing**
   - Unit tests
   - Integration tests
   - UI tests
   - Performance tests

4. **Review**
   - Code review
   - Security review
   - Documentation review
   - UI/UX review

5. **Deployment**
   - Merge to develop
   - Test in staging
   - Merge to main
   - Deploy to production

---

## 🐛 Troubleshooting Development Issues

### Common Issues

#### PyQt6 Installation Problems
```bash
# Install Visual C++ Redistributable
# Download from Microsoft website

# Install PyQt6 with pip
pip install PyQt6

# If still failing, try conda
conda install pyqt
```

#### Script Execution Issues
```python
# Debug script execution
import subprocess
import sys

def debug_script_execution(script_path):
    """Debug script execution issues"""
    try:
        result = subprocess.run(
            script_path,
            capture_output=True,
            text=True,
            shell=True
        )
        print(f"Return code: {result.returncode}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
    except Exception as e:
        print(f"Exception: {e}")
```

#### UI Scaling Issues
```python
# Fix high DPI scaling issues
import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"

# Alternative approach
from PyQt6.QtWidgets import QApplication
QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
```

### Debugging Tools

#### Logging Debug Information
```python
import logging

# Enable debug logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

# Log Qt events
import sys
from PyQt6.QtCore import QLoggingCategory

QLoggingCategory.setFilterRules("qt.*=true")
```

#### Performance Profiling
```python
import cProfile
import pstats

def profile_application():
    """Profile application performance"""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run application code
    main()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(20)
```

---

**PC Troubleshooter v1.0 - Developer Documentation**  
*Comprehensive guide for developers and contributors*

*Last Updated: August 24, 2025*
