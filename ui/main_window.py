"""
Main Window for PC Troubleshooter Application
"""

import sys
import os
import subprocess
import threading
from datetime import datetime
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QGridLayout, QPushButton, QTextEdit, QLabel, 
                            QTabWidget, QScrollArea, QFrame, QMessageBox,
                            QFileDialog, QMenuBar, QMenu, QStatusBar, QProgressBar,
                            QSplitter, QGroupBox, QSpacerItem, QSizePolicy, QApplication,
                            QGraphicsDropShadowEffect, QToolTip, QSystemTrayIcon, QStyle)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer, QPropertyAnimation, QEasingCurve, QRect, QParallelAnimationGroup
from PyQt6.QtGui import QFont, QPixmap, QAction, QPalette, QLinearGradient, QColor, QPainter, QPainterPath, QCursor, QKeySequence, QShortcut

class ProfessionalButton(QPushButton):
    """A professional button with hover animations and effects"""
    
    def __init__(self, text="", icon="", parent=None):
        super().__init__(text, parent)
        self.icon_text = icon
        self.is_hovered = False
        self.setup_animation()
        self.setup_styling()
    
    def setup_animation(self):
        """Setup hover animations"""
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(200)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def setup_styling(self):
        """Setup professional styling"""
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
    def enterEvent(self, event):
        """Handle mouse enter event"""
        self.is_hovered = True
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        """Handle mouse leave event"""
        self.is_hovered = False
        super().leaveEvent(event)

class StatusCard(QFrame):
    """A professional status card with real-time updates"""
    
    def __init__(self, title, value, icon="", parent=None):
        super().__init__(parent)
        self.title = title
        self.value = value
        self.icon = icon
        self.setup_ui()
        self.setup_styling()
    
    def setup_ui(self):
        """Setup the card UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)
        
        # Icon and title row
        header_layout = QHBoxLayout()
        
        if self.icon:
            icon_label = QLabel(self.icon)
            icon_label.setFont(QFont("Segoe UI", 16))
            icon_label.setFixedSize(24, 24)
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            header_layout.addWidget(icon_label)
        
        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.title_label.setObjectName("cardTitle")
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        
        # Value label
        self.value_label = QLabel(str(self.value))
        self.value_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.value_label.setObjectName("cardValue")
        
        layout.addLayout(header_layout)
        layout.addWidget(self.value_label)
    
    def setup_styling(self):
        """Setup card styling"""
        self.setObjectName("statusCard")
        self.setFixedHeight(80)
        
    def update_value(self, new_value):
        """Update the card value with animation"""
        self.value = new_value
        self.value_label.setText(str(new_value))

class ScriptRunner(QThread):
    """Enhanced thread for running scripts with better progress tracking"""
    output_received = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)
    progress_update = pyqtSignal(int)
    
    def __init__(self, script_path, script_name):
        super().__init__()
        self.script_path = script_path
        self.script_name = script_name
        self.progress = 0
    
    def run(self):
        try:
            # Run the script and capture output
            process = subprocess.Popen(
                [self.script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                shell=True,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            # Simulate progress updates
            self.progress_update.emit(10)
            
            # Read output line by line
            line_count = 0
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    line_count += 1
                    self.output_received.emit(output.strip())
                    # Update progress based on output lines
                    progress = min(90, 10 + (line_count * 5))
                    self.progress_update.emit(progress)
            
            # Wait for process to complete
            return_code = process.wait()
            self.progress_update.emit(100)
            
            if return_code == 0:
                self.finished_signal.emit(True, f"✅ {self.script_name} completed successfully")
            else:
                self.finished_signal.emit(False, f"❌ {self.script_name} failed with return code {return_code}")
                
        except Exception as e:
            self.finished_signal.emit(False, f"💥 Error running {self.script_name}: {str(e)}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PC Troubleshooter v1.0 - Professional System Diagnostics [DARK MODE]")
        self.setGeometry(100, 100, 1400, 900)
        self.setMinimumSize(1200, 800)
        
        # Set window icon (using built-in style)
        self.setWindowIcon(self.style().standardIcon(self.style().StandardPixmap.SP_ComputerIcon))
        
        # Initialize variables
        self.current_theme = "dark"
        self.scripts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts")
        self.logs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        self.current_log = []
        
        # Setup UI
        self.setup_ui()
        self.setup_menu()
        self.setup_status_bar()
        self.setup_system_tray()
        self.setup_keyboard_shortcuts()
        self.apply_professional_theme()
        
        # Ensure scripts and logs directories exist
        os.makedirs(self.scripts_path, exist_ok=True)
        os.makedirs(self.logs_path, exist_ok=True)
        
        # Show startup message
        self.show_startup_message()
        
        # Setup status monitoring
        self.setup_status_monitoring()
    
    def show_startup_message(self):
        """Show a professional startup message"""
        startup_msg = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                         PC TROUBLESHOOTER v1.0                              ║
║                    Professional System Diagnostics Tool                     ║
║                             >>> DARK MODE <<<                               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  🌐 Network          📶 Bluetooth         🔊 Audio                          ║
║  🖥️  Display          💾 Storage           ⚡ Performance                    ║
║                                                                              ║
║  >> DARK THEME ACTIVE - Professional diagnostics ready                      ║
║  >> Select a category from the left panel to begin troubleshooting          ║
║                                                                              ║
║  💡 Tip: Run as Administrator for full functionality                        ║
║  🎨 Current Theme: Complete Black Dark Mode                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

🕐 Session started at """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """ [DARK MODE]

"""
        if hasattr(self, 'console_output'):
            self.console_output.setText(startup_msg)
            QTimer.singleShot(100, lambda: self.current_log.append("Session started - PC Troubleshooter v1.0"))
    
    def setup_system_tray(self):
        """Setup system tray integration for professional experience"""
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray_icon = QSystemTrayIcon(self)
            
            # Create tray icon from application icon
            icon = self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
            self.tray_icon.setIcon(icon)
            
            # Create context menu for tray
            tray_menu = QMenu()
            
            show_action = tray_menu.addAction("Show PC Troubleshooter")
            show_action.triggered.connect(self.show)
            
            tray_menu.addSeparator()
            
            quick_scan_action = tray_menu.addAction("🔍 Quick System Scan")
            quick_scan_action.triggered.connect(self.quick_system_scan)
            
            tray_menu.addSeparator()
            
            quit_action = tray_menu.addAction("Exit")
            quit_action.triggered.connect(QApplication.instance().quit)
            
            self.tray_icon.setContextMenu(tray_menu)
            self.tray_icon.activated.connect(self.tray_icon_activated)
            
            # Show tray icon
            self.tray_icon.show()
            
            # Set tooltip
            self.tray_icon.setToolTip("PC Troubleshooter - System Diagnostic Tool")
    
    def setup_keyboard_shortcuts(self):
        """Setup professional keyboard shortcuts"""
        # Quick scan shortcut
        quick_scan_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quick_scan_shortcut.activated.connect(self.quick_system_scan)
        
        # Emergency stop shortcut
        emergency_stop_shortcut = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
        emergency_stop_shortcut.activated.connect(self.emergency_stop)
        
        # Clear output shortcut
        clear_output_shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        clear_output_shortcut.activated.connect(lambda: self.console_output.clear() if hasattr(self, 'console_output') else None)
        
        # Refresh shortcut
        refresh_shortcut = QShortcut(QKeySequence("F5"), self)
        refresh_shortcut.activated.connect(self.refresh_system_status)
        
        # Show help shortcut
        help_shortcut = QShortcut(QKeySequence("F1"), self)
        help_shortcut.activated.connect(self.show_help_dialog)
    
    def setup_status_monitoring(self):
        """Setup real-time status monitoring"""
        # Status update timer
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_system_status)
        self.status_timer.start(5000)  # Update every 5 seconds
        
        # Performance monitoring
        self.performance_timer = QTimer()
        self.performance_timer.timeout.connect(self.update_performance_metrics)
        self.performance_timer.start(2000)  # Update every 2 seconds
        
        # Initialize counters
        self.scripts_run_count = 0
        self.successful_scripts = 0
        self.active_tasks_count = 0
    
    def setup_ui(self):
        """Setup the enhanced professional user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout with enhanced spacing
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Add status dashboard at top
        status_dashboard = self.create_status_dashboard()
        main_layout.addWidget(status_dashboard)
        
        # Content layout with splitter
        content_layout = QHBoxLayout()
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Troubleshooting categories
        left_panel = self.create_professional_left_panel()
        splitter.addWidget(left_panel)
        
        # Right panel - Output console
        right_panel = self.create_professional_right_panel()
        splitter.addWidget(right_panel)
        
        # Set initial splitter sizes (40% left, 60% right)
        splitter.setSizes([560, 840])
        splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #333333;
                width: 3px;
                border-radius: 1px;
                margin: 2px;
            }
            QSplitter::handle:hover {
                background-color: #555555;
            }
        """)
        
        content_layout.addWidget(splitter)
        main_layout.addLayout(content_layout)
    
    def create_status_dashboard(self):
        """Create a professional status dashboard"""
        dashboard = QFrame()
        dashboard.setObjectName("statusDashboard")
        dashboard.setMaximumHeight(100)
        
        layout = QHBoxLayout(dashboard)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(20)
        
        # System status cards
        self.system_status_card = StatusCard("System Status", "Ready", "🖥️")
        self.scripts_run_card = StatusCard("Scripts Run", "0", "🔧")
        self.success_rate_card = StatusCard("Success Rate", "100%", "✅")
        self.active_tasks_card = StatusCard("Active Tasks", "0", "⚡")
        
        layout.addWidget(self.system_status_card)
        layout.addWidget(self.scripts_run_card)
        layout.addWidget(self.success_rate_card)
        layout.addWidget(self.active_tasks_card)
        layout.addStretch()
        
        # Quick action buttons
        quick_buttons_layout = QHBoxLayout()
        
        emergency_stop_btn = ProfessionalButton("🛑 Emergency Stop", "🛑")
        emergency_stop_btn.setObjectName("emergencyButton")
        emergency_stop_btn.clicked.connect(self.emergency_stop)
        emergency_stop_btn.setMaximumWidth(120)
        
        refresh_btn = ProfessionalButton("🔄 Refresh", "🔄")
        refresh_btn.setObjectName("refreshButton")
        refresh_btn.clicked.connect(self.refresh_system_status)
        refresh_btn.setMaximumWidth(100)
        
        quick_buttons_layout.addWidget(emergency_stop_btn)
        quick_buttons_layout.addWidget(refresh_btn)
        
        layout.addLayout(quick_buttons_layout)
        
        return dashboard
    
    def create_professional_left_panel(self):
        """Create the professional left panel with troubleshooting categories"""
        # Main container
        container = QWidget()
        container.setObjectName("leftPanel")
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header section
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 20, 20, 20)
        
        # App title with icon
        title_layout = QHBoxLayout()
        
        # Icon (using emoji as placeholder)
        icon_label = QLabel("🔧")
        icon_label.setFont(QFont("Segoe UI", 24))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_layout.addWidget(icon_label)
        
        # Title and subtitle
        title_container = QVBoxLayout()
        title = QLabel("PC Troubleshooter")
        title.setObjectName("mainTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        title.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        
        subtitle = QLabel("Professional System Diagnostics")
        subtitle.setObjectName("subtitle")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        title_container.addWidget(title)
        title_container.addWidget(subtitle)
        title_layout.addLayout(title_container)
        title_layout.addStretch()
        
        header_layout.addLayout(title_layout)
        main_layout.addWidget(header_frame)
        
        # Create scroll area for categories
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setObjectName("categoryScrollArea")
        
        # Categories container
        categories_widget = QWidget()
        categories_layout = QVBoxLayout(categories_widget)
        categories_layout.setContentsMargins(10, 10, 10, 10)
        categories_layout.setSpacing(15)
        
        # Professional categories with icons and better organization
        categories = [
            ("🌐", "Network", "Connectivity & Internet", "#4CAF50", [
                ("Reset Network Stack", "network_reset.bat"),
                ("Flush DNS Cache", "flush_dns.bat"),
                ("Reset Network Adapter", "reset_adapter.bat"),
                ("Network Diagnostics", "network_diagnostics.bat")
            ]),
            ("📶", "Bluetooth", "Wireless Device Management", "#2196F3", [
                ("Restart Bluetooth Service", "bluetooth_restart.bat"),
                ("Check Bluetooth Drivers", "bluetooth_drivers.bat"),
                ("Reset Bluetooth Stack", "bluetooth_reset.bat")
            ]),
            ("🔊", "Audio", "Sound & Audio Devices", "#FF9800", [
                ("Restart Audio Services", "audio_restart.bat"),
                ("Audio Device Detection", "audio_detect.bat"),
                ("Audio Troubleshooter", "audio_troubleshoot.bat")
            ]),
            ("🖥️", "Display", "Graphics & Monitor Setup", "#9C27B0", [
                ("Display Settings Check", "display_check.bat"),
                ("Reset Graphics Driver", "graphics_reset.bat"),
                ("Monitor Detection", "monitor_detect.bat")
            ]),
            ("💾", "Storage", "Disk Space & Cleanup", "#607D8B", [
                ("Clear Temp Files", "clear_temp.bat"),
                ("Disk Cleanup", "disk_cleanup.bat"),
                ("Check Disk Space", "disk_space.bat")
            ]),
            ("⚡", "Performance", "System Optimization", "#E91E63", [
                ("List Startup Programs", "startup_programs.bat"),
                ("Memory Usage Check", "memory_check.bat"),
                ("System File Check", "sfc_scan.bat"),
                ("Performance Monitor", "performance_monitor.bat")
            ])
        ]
        
        for icon, category_name, category_desc, color, tools in categories:
            category_widget = self.create_professional_category_card(icon, category_name, category_desc, color, tools)
            categories_layout.addWidget(category_widget)
        
        # Quick actions section
        quick_actions_frame = QFrame()
        quick_actions_frame.setObjectName("quickActionsFrame")
        quick_actions_layout = QVBoxLayout(quick_actions_frame)
        quick_actions_layout.setContentsMargins(15, 15, 15, 15)
        
        quick_label = QLabel("⚡ Quick Actions")
        quick_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        quick_label.setObjectName("sectionLabel")
        quick_actions_layout.addWidget(quick_label)
        
        # Run All Basic Fixes button with professional styling
        run_all_btn = QPushButton("� Run All Basic Fixes")
        run_all_btn.setObjectName("primaryButton")
        run_all_btn.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        run_all_btn.setMinimumHeight(50)
        run_all_btn.clicked.connect(self.run_all_basic_fixes)
        quick_actions_layout.addWidget(run_all_btn)
        
        categories_layout.addWidget(quick_actions_frame)
        categories_layout.addStretch()
        
        scroll_area.setWidget(categories_widget)
        main_layout.addWidget(scroll_area)
        
        return container
    
    def create_professional_category_card(self, icon, name, description, color, tools):
        """Create a professional-looking category card"""
        card = QFrame()
        card.setObjectName("categoryCard")
        card.setFrameStyle(QFrame.Shape.NoFrame)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        
        # Header with icon and title
        header_layout = QHBoxLayout()
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setFont(QFont("Segoe UI", 20))
        icon_label.setFixedSize(40, 40)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet(f"""
            QLabel {{
                background-color: {color};
                border-radius: 20px;
                color: white;
            }}
        """)
        header_layout.addWidget(icon_label)
        
        # Title and description
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        
        title_label = QLabel(name)
        title_label.setFont(QFont("Segoe UI", 13, QFont.Weight.Bold))
        title_label.setObjectName("categoryTitle")
        
        desc_label = QLabel(description)
        desc_label.setFont(QFont("Segoe UI", 9))
        desc_label.setObjectName("categoryDescription")
        desc_label.setWordWrap(True)
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(desc_label)
        header_layout.addLayout(text_layout)
        header_layout.addStretch()
        
        layout.addLayout(header_layout)
        
        # Tools grid layout for better organization
        tools_grid = QGridLayout()
        tools_grid.setSpacing(8)
        
        row, col = 0, 0
        for tool_name, script_file in tools:
            btn = QPushButton(tool_name)
            btn.setObjectName("toolButton")
            btn.setFont(QFont("Segoe UI", 9))
            btn.setMinimumHeight(32)
            btn.setMaximumHeight(32)
            btn.clicked.connect(lambda checked, sf=script_file, tn=tool_name: self.run_script(sf, tn))
            
            tools_grid.addWidget(btn, row, col)
            col += 1
            if col > 1:  # 2 columns max
                col = 0
                row += 1
        
        layout.addLayout(tools_grid)
        
        return card
    
    def create_professional_right_panel(self):
        """Create the professional right panel with output console"""
        container = QWidget()
        container.setObjectName("rightPanel")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Console header with professional styling
        header_frame = QFrame()
        header_frame.setObjectName("consoleHeader")
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)
        
        # Console icon and title
        console_icon = QLabel("📋")
        console_icon.setFont(QFont("Segoe UI", 16))
        header_layout.addWidget(console_icon)
        
        console_label = QLabel("Output Console")
        console_label.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        console_label.setObjectName("consoleTitle")
        header_layout.addWidget(console_label)
        
        # Status indicator
        self.status_indicator = QLabel("🟢 Ready")
        self.status_indicator.setFont(QFont("Segoe UI", 9))
        self.status_indicator.setObjectName("statusIndicator")
        header_layout.addWidget(self.status_indicator)
        
        header_layout.addStretch()
        
        # Action buttons with professional styling
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        clear_btn = QPushButton("🗑️ Clear")
        clear_btn.setObjectName("secondaryButton")
        clear_btn.setFont(QFont("Segoe UI", 9))
        clear_btn.setMinimumHeight(32)
        clear_btn.clicked.connect(self.clear_console)
        button_layout.addWidget(clear_btn)
        
        export_btn = QPushButton("📄 Export Logs")
        export_btn.setObjectName("secondaryButton")
        export_btn.setFont(QFont("Segoe UI", 9))
        export_btn.setMinimumHeight(32)
        export_btn.clicked.connect(self.export_logs)
        button_layout.addWidget(export_btn)
        
        header_layout.addLayout(button_layout)
        layout.addWidget(header_frame)
        
        # Console output with professional styling
        console_frame = QFrame()
        console_frame.setObjectName("consoleFrame")
        console_layout = QVBoxLayout(console_frame)
        console_layout.setContentsMargins(1, 1, 1, 1)
        
        self.console_output = QTextEdit()
        self.console_output.setObjectName("consoleOutput")
        self.console_output.setReadOnly(True)
        self.console_output.setFont(QFont("JetBrains Mono", 10))
        
        # Add welcome message
        welcome_msg = """
╔══════════════════════════════════════════════════════════════╗
║                    PC TROUBLESHOOTER v1.0                   ║
║              Professional System Diagnostics Tool           ║
╚══════════════════════════════════════════════════════════════╝

>> SYSTEM READY - DARK MODE ACTIVE
>> Select a troubleshooting category from the left panel to begin.
>> All script outputs will appear here in real-time.
>> 
>> Status: ONLINE | Mode: PROFESSIONAL | Theme: DARK
>> Ready to diagnose and fix system issues...
"""
        self.console_output.setText(welcome_msg)
        
        console_layout.addWidget(self.console_output)
        layout.addWidget(console_frame)
        
        # Enhanced progress bar
        progress_container = QFrame()
        progress_container.setObjectName("progressContainer")
        progress_layout = QHBoxLayout(progress_container)
        progress_layout.setContentsMargins(10, 10, 10, 10)
        
        self.progress_label = QLabel("")
        self.progress_label.setFont(QFont("Segoe UI", 9))
        self.progress_label.setObjectName("progressLabel")
        progress_layout.addWidget(self.progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setObjectName("modernProgressBar")
        self.progress_bar.setMinimumHeight(8)
        self.progress_bar.setVisible(False)
        progress_layout.addWidget(self.progress_bar)
        
        progress_container.setVisible(False)
        self.progress_container = progress_container
        layout.addWidget(progress_container)
        
        return container
    
    def create_category_frame(self, name, description, tools):
        """Legacy method - kept for compatibility"""
        return self.create_professional_category_card("🔧", name, description, "#607D8B", tools)
    
    def create_right_panel(self):
        """Legacy method - kept for compatibility"""
        return self.create_professional_right_panel()
    
    def setup_menu(self):
        """Setup the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        export_action = QAction("Export Logs", self)
        export_action.triggered.connect(self.export_logs)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # View menu
        view_menu = menubar.addMenu("View")
        
        toggle_theme_action = QAction("Switch to Light Theme", self)
        toggle_theme_action.triggered.connect(self.toggle_theme)
        view_menu.addAction(toggle_theme_action)
        self.toggle_theme_action = toggle_theme_action
        
        clear_console_action = QAction("Clear Console", self)
        clear_console_action.triggered.connect(self.clear_console)
        view_menu.addAction(clear_console_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_status_bar(self):
        """Setup the status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
    
    def run_script(self, script_file, tool_name):
        """Run a troubleshooting script with enhanced professional feedback"""
        script_path = os.path.join(self.scripts_path, script_file)
        
        if not os.path.exists(script_path):
            self.log_message(f"❌ Script not found: {script_file}")
            QMessageBox.warning(self, "Script Not Found", 
                              f"The script '{script_file}' was not found in the scripts directory.")
            return
        
        # Confirm before running
        reply = QMessageBox.question(self, "Confirm Action", 
                                   f"Are you sure you want to run '{tool_name}'?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            # Update active tasks counter
            self.active_tasks_count += 1
            self.update_performance_metrics()
            
            # Enhanced status feedback
            self.log_message(f"🚀 Starting: {tool_name}")
            self.status_bar.showMessage(f"Running: {tool_name}")
            self.status_indicator.setText("🟡 Running...")
            self.progress_container.setVisible(True)
            self.progress_bar.setVisible(True)
            self.progress_bar.setRange(0, 0)  # Indeterminate progress
            self.progress_label.setText(f"Executing: {tool_name}")
            
            # Create and start the script runner thread
            self.script_runner = ScriptRunner(script_path, tool_name)
            self.script_runner.output_received.connect(self.log_message)
            self.script_runner.finished_signal.connect(self.script_finished)
            self.script_runner.progress_update.connect(self.update_progress)
            self.script_runner.start()
    
    def update_progress(self, value):
        """Update progress bar with current value"""
        if hasattr(self, 'progress_bar'):
            if value >= 0:
                self.progress_bar.setRange(0, 100)
                self.progress_bar.setValue(value)
            else:
                self.progress_bar.setRange(0, 0)  # Indeterminate
    
    def run_all_basic_fixes(self):
        """Run all basic troubleshooting fixes"""
        basic_scripts = [
            ("flush_dns.bat", "Flush DNS Cache"),
            ("clear_temp.bat", "Clear Temp Files"),
            ("network_reset.bat", "Reset Network Stack"),
            ("audio_restart.bat", "Restart Audio Services")
        ]
        
        reply = QMessageBox.question(self, "Confirm Action", 
                                   "This will run multiple troubleshooting scripts. Continue?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log_message("🔧 Starting Basic Fixes Suite...")
            self.status_indicator.setText("🟡 Running Suite...")
            self.progress_container.setVisible(True)
            self.progress_bar.setVisible(True)
            self.progress_bar.setRange(0, len(basic_scripts))
            self.progress_bar.setValue(0)
            self.run_script_sequence(basic_scripts, 0)
    
    def run_script_sequence(self, scripts, index):
        """Run a sequence of scripts"""
        if index >= len(scripts):
            self.log_message("✅ All basic fixes completed!")
            self.status_bar.showMessage("All basic fixes completed")
            self.status_indicator.setText("🟢 Ready")
            self.progress_container.setVisible(False)
            self.progress_bar.setVisible(False)
            return
        
        script_file, tool_name = scripts[index]
        script_path = os.path.join(self.scripts_path, script_file)
        
        if os.path.exists(script_path):
            self.log_message(f"🚀 Running: {tool_name}")
            self.status_bar.showMessage(f"Running: {tool_name} ({index + 1}/{len(scripts)})")
            self.progress_label.setText(f"Executing: {tool_name} ({index + 1}/{len(scripts)})")
            self.progress_bar.setValue(index)
            
            # Create script runner for this script
            self.script_runner = ScriptRunner(script_path, tool_name)
            self.script_runner.output_received.connect(self.log_message)
            self.script_runner.finished_signal.connect(
                lambda success, msg, scripts=scripts, idx=index: self.script_sequence_finished(success, msg, scripts, idx)
            )
            self.script_runner.start()
        else:
            self.log_message(f"⚠️ Skipping {tool_name} - script not found")
            # Continue with next script
            QTimer.singleShot(100, lambda: self.run_script_sequence(scripts, index + 1))
    
    def script_sequence_finished(self, success, message, scripts, index):
        """Handle completion of a script in a sequence"""
        self.log_message(message)
        # Continue with next script
        QTimer.singleShot(500, lambda: self.run_script_sequence(scripts, index + 1))
    
    def script_finished(self, success, message):
        """Handle script completion with enhanced feedback"""
        self.scripts_run_count += 1
        if success:
            self.successful_scripts += 1
        
        self.active_tasks_count = max(0, self.active_tasks_count - 1)
        
        # Update performance metrics
        self.update_performance_metrics()
        
        # Log completion
        self.log_message(message)
        
        # Update status indicators
        self.status_bar.showMessage("Ready")
        self.status_indicator.setText("🟢 Ready")
        self.progress_container.setVisible(False)
        self.progress_bar.setVisible(False)
        self.progress_label.setText("")
        
        # Update status bar with detailed metrics
        success_rate = (self.successful_scripts / self.scripts_run_count * 100) if self.scripts_run_count > 0 else 100
        status_msg = f"Scripts: {self.scripts_run_count} | Success Rate: {success_rate:.0f}% | Active: {self.active_tasks_count}"
        self.status_bar.showMessage(status_msg, 5000)  # Show for 5 seconds
    
    def log_message(self, message):
        """Add a message to the console output"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        
        self.console_output.append(formatted_message)
        self.current_log.append(formatted_message)
        
        # Auto-scroll to bottom
        self.console_output.verticalScrollBar().setValue(
            self.console_output.verticalScrollBar().maximum()
        )
    
    def clear_console(self):
        """Clear the console output"""
        self.console_output.clear()
        self.current_log.clear()
        self.log_message("Console cleared")
    
    def export_logs(self):
        """Export console logs to a file"""
        if not self.current_log:
            QMessageBox.information(self, "No Logs", "No logs to export.")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"pc_troubleshooter_log_{timestamp}.txt"
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Export Logs", default_filename, "Text Files (*.txt);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("PC Troubleshooter Log Export\n")
                    f.write("=" * 50 + "\n")
                    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    
                    for log_entry in self.current_log:
                        f.write(log_entry + "\n")
                
                QMessageBox.information(self, "Export Successful", f"Logs exported to:\n{filename}")
                self.log_message(f"📄 Logs exported to: {filename}")
                
            except Exception as e:
                QMessageBox.critical(self, "Export Failed", f"Failed to export logs:\n{str(e)}")
    
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_professional_theme()
        
        # Update menu text and window title
        if self.current_theme == "dark":
            self.toggle_theme_action.setText("Switch to Light Theme")
            self.setWindowTitle("PC Troubleshooter v1.0 - Professional System Diagnostics [DARK MODE]")
        else:
            self.toggle_theme_action.setText("Switch to Dark Theme")
            self.setWindowTitle("PC Troubleshooter v1.0 - Professional System Diagnostics [LIGHT MODE]")
        
        # Update console message
        theme_msg = f"🎨 Theme switched to: {'Complete Black Dark Mode' if self.current_theme == 'dark' else 'Professional Light Mode'}"
        self.log_message(theme_msg)
    
    def quick_system_scan(self):
        """Perform a quick system scan"""
        if hasattr(self, 'console_output'):
            self.console_output.append("\n🔍 Starting Quick System Scan...")
        
        # Run basic network connectivity test
        network_script = os.path.join(self.scripts_path, "network", "reset_network_stack.bat")
        if os.path.exists(network_script):
            self.run_script("network/reset_network_stack.bat", "Quick Network Test")
    
    def emergency_stop(self):
        """Emergency stop all running operations"""
        if hasattr(self, 'script_runner') and self.script_runner.isRunning():
            self.script_runner.terminate()
            if hasattr(self, 'console_output'):
                self.console_output.append("\n🛑 Emergency stop activated - All operations halted")
            self.active_tasks_count = 0
            if hasattr(self, 'active_tasks_card'):
                self.active_tasks_card.update_value(0)
    
    def refresh_system_status(self):
        """Refresh system status display"""
        if hasattr(self, 'console_output'):
            self.console_output.append("\n🔄 Refreshing system status...")
        self.update_system_status()
        self.update_performance_metrics()
    
    def update_system_status(self):
        """Update system status information"""
        try:
            import platform
            system_info = f"OS: {platform.system()} {platform.release()}"
            if hasattr(self, 'system_status_card'):
                self.system_status_card.update_value("Online")
            
            # Log status update
            self.current_log.append(f"Status update: {system_info}")
        except Exception as e:
            if hasattr(self, 'system_status_card'):
                self.system_status_card.update_value("Error")
            self.current_log.append(f"Status error: {str(e)}")
    
    def update_performance_metrics(self):
        """Update performance metrics"""
        try:
            # Update status cards if they exist
            if hasattr(self, 'scripts_run_card'):
                self.scripts_run_card.update_value(self.scripts_run_count)
            
            if hasattr(self, 'success_rate_card'):
                success_rate = 100 if self.scripts_run_count == 0 else (self.successful_scripts / self.scripts_run_count * 100)
                self.success_rate_card.update_value(f"{success_rate:.0f}%")
            
            if hasattr(self, 'active_tasks_card'):
                self.active_tasks_card.update_value(self.active_tasks_count)
            
            # Try to get system performance if psutil is available
            try:
                import psutil
                cpu_percent = psutil.cpu_percent(interval=0.1)
                memory_percent = psutil.virtual_memory().percent
                
                if hasattr(self, 'system_status_card'):
                    if cpu_percent > 80 or memory_percent > 80:
                        self.system_status_card.update_value("High Load")
                    else:
                        self.system_status_card.update_value("Normal")
            except ImportError:
                # psutil not available, use basic metrics
                pass
        except Exception as e:
            self.current_log.append(f"Performance error: {str(e)}")
    
    def tray_icon_activated(self, reason):
        """Handle system tray icon activation"""
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()
                self.raise_()
                self.activateWindow()
    
    def show_help_dialog(self):
        """Show help dialog with keyboard shortcuts"""
        help_text = """
<div style='font-family: Segoe UI; color: #ffffff; background-color: #000000;'>
<h3 style='color: #00ff00;'>PC Troubleshooter - Keyboard Shortcuts</h3>
<hr style='border-color: #333333;'>
<table style='color: #cccccc;'>
<tr><td><b>Ctrl+Q</b></td><td>Quick System Scan</td></tr>
<tr><td><b>Ctrl+Shift+S</b></td><td>Emergency Stop</td></tr>
<tr><td><b>Ctrl+L</b></td><td>Clear Output</td></tr>
<tr><td><b>F5</b></td><td>Refresh Status</td></tr>
<tr><td><b>F1</b></td><td>Show This Help</td></tr>
</table>
<hr style='border-color: #333333;'>
<p style='color: #aaaaaa;'><i>Professional System Diagnostics Tool</i></p>
</div>
"""
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Keyboard Shortcuts")
        msg_box.setTextFormat(Qt.TextFormat.RichText)
        msg_box.setText(help_text)
        msg_box.exec()

    def apply_professional_theme(self):
        """Apply professional theme styling"""
        if self.current_theme == "dark":
            self.apply_dark_professional_theme()
        else:
            self.apply_light_professional_theme()
    
    def apply_light_professional_theme(self):
        """Apply light professional theme"""
        self.setStyleSheet("""
            /* Main Window */
            QMainWindow {
                background-color: #f8f9fa;
                color: #2c3e50;
            }
            
            /* Left Panel */
            QWidget#leftPanel {
                background-color: #ffffff;
                border-right: 1px solid #e9ecef;
            }
            
            /* Right Panel */
            QWidget#rightPanel {
                background-color: #ffffff;
            }
            
            /* Header Frame */
            QFrame#headerFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #667eea, stop:1 #764ba2);
                border-radius: 12px;
                color: white;
            }
            
            QLabel#mainTitle {
                color: white;
            }
            
            QLabel#subtitle {
                color: rgba(255, 255, 255, 0.9);
            }
            
            /* Category Cards */
            QFrame#categoryCard {
                background-color: #ffffff;
                border: 1px solid #e9ecef;
                border-radius: 12px;
                margin: 5px;
            }
            
            QFrame#categoryCard:hover {
                border: 1px solid #007acc;
                background-color: #f8f9fa;
            }
            
            QLabel#categoryTitle {
                color: #2c3e50;
                font-weight: bold;
            }
            
            QLabel#categoryDescription {
                color: #6c757d;
            }
            
            /* Buttons */
            QPushButton#primaryButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #007acc, stop:1 #0099ff);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                font-weight: bold;
            }
            
            QPushButton#primaryButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #0066aa, stop:1 #0088dd);
            }
            
            QPushButton#primaryButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #005599, stop:1 #0077cc);
            }
            
            QPushButton#secondaryButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
            }
            
            QPushButton#secondaryButton:hover {
                background-color: #5a6268;
            }
            
            QPushButton#toolButton {
                background-color: #f8f9fa;
                color: #495057;
                border: 1px solid #dee2e6;
                border-radius: 6px;
                padding: 6px 12px;
                text-align: left;
            }
            
            QPushButton#toolButton:hover {
                background-color: #e9ecef;
                border-color: #007acc;
                color: #007acc;
            }
            
            QPushButton#toolButton:pressed {
                background-color: #dee2e6;
            }
            
            /* Console Styling */
            QFrame#consoleHeader {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #495057, stop:1 #6c757d);
                border-radius: 8px 8px 0 0;
                color: white;
            }
            
            QLabel#consoleTitle {
                color: white;
            }
            
            QLabel#statusIndicator {
                color: rgba(255, 255, 255, 0.9);
                font-weight: bold;
            }
            
            QFrame#consoleFrame {
                background-color: #ffffff;
                border: 1px solid #dee2e6;
                border-radius: 0 0 8px 8px;
            }
            
            QTextEdit#consoleOutput {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: none;
                font-family: 'JetBrains Mono', 'Consolas', monospace;
                selection-background-color: #264f78;
                selection-color: #ffffff;
            }
            
            /* Progress Bar */
            QFrame#progressContainer {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 6px;
            }
            
            QProgressBar#modernProgressBar {
                border: none;
                background-color: #e9ecef;
                border-radius: 4px;
                text-align: center;
            }
            
            QProgressBar#modernProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #007acc, stop:1 #0099ff);
                border-radius: 4px;
            }
            
            /* Quick Actions */
            QFrame#quickActionsFrame {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
            }
            
            QLabel#sectionLabel {
                color: #495057;
                font-weight: bold;
            }
            
            /* Scroll Areas */
            QScrollArea#categoryScrollArea {
                border: none;
                background-color: transparent;
            }
            
            QScrollBar:vertical {
                background-color: #f8f9fa;
                width: 12px;
                border-radius: 6px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #ced4da;
                border-radius: 6px;
                min-height: 20px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #adb5bd;
            }
            
            /* Menu Bar */
            QMenuBar {
                background-color: #ffffff;
                color: #2c3e50;
                border-bottom: 1px solid #e9ecef;
                padding: 4px;
            }
            
            QMenuBar::item {
                background-color: transparent;
                padding: 8px 12px;
                border-radius: 4px;
            }
            
            QMenuBar::item:selected {
                background-color: #f8f9fa;
                color: #007acc;
            }
            
            QMenu {
                background-color: #ffffff;
                color: #2c3e50;
                border: 1px solid #dee2e6;
                border-radius: 6px;
                padding: 4px;
            }
            
            QMenu::item {
                padding: 8px 20px;
                border-radius: 4px;
            }
            
            QMenu::item:selected {
                background-color: #f8f9fa;
                color: #007acc;
            }
            
            /* Status Bar */
            QStatusBar {
                background-color: #f8f9fa;
                color: #6c757d;
                border-top: 1px solid #e9ecef;
            }
        """)
    
    def apply_dark_professional_theme(self):
        """Apply complete black dark professional theme"""
        self.setStyleSheet("""
            /* Main Window */
            QMainWindow {
                background-color: #000000;
                color: #ffffff;
            }
            
            /* Left Panel */
            QWidget#leftPanel {
                background-color: #0a0a0a;
                border-right: 1px solid #1a1a1a;
            }
            
            /* Right Panel */
            QWidget#rightPanel {
                background-color: #0a0a0a;
            }
            
            /* Header Frame */
            QFrame#headerFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #1a1a1a, stop:1 #333333);
                border: 1px solid #333333;
                border-radius: 12px;
                color: #ffffff;
            }
            
            QLabel#mainTitle {
                color: #ffffff;
                font-weight: bold;
            }
            
            QLabel#subtitle {
                color: #cccccc;
            }
            
            /* Category Cards */
            QFrame#categoryCard {
                background-color: #111111;
                border: 1px solid #222222;
                border-radius: 12px;
                margin: 5px;
            }
            
            QFrame#categoryCard:hover {
                border: 1px solid #444444;
                background-color: #1a1a1a;
            }
            
            QLabel#categoryTitle {
                color: #ffffff;
                font-weight: bold;
            }
            
            QLabel#categoryDescription {
                color: #aaaaaa;
            }
            
            /* Buttons */
            QPushButton#primaryButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #1a1a1a, stop:1 #333333);
                color: #ffffff;
                border: 1px solid #444444;
                border-radius: 8px;
                padding: 12px 20px;
                font-weight: bold;
            }
            
            QPushButton#primaryButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #333333, stop:1 #555555);
                border-color: #666666;
            }
            
            QPushButton#primaryButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #0a0a0a, stop:1 #1a1a1a);
            }
            
            QPushButton#secondaryButton {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333333;
                border-radius: 6px;
                padding: 8px 16px;
            }
            
            QPushButton#secondaryButton:hover {
                background-color: #333333;
                border-color: #555555;
            }
            
            QPushButton#toolButton {
                background-color: #111111;
                color: #cccccc;
                border: 1px solid #222222;
                border-radius: 6px;
                padding: 6px 12px;
                text-align: left;
            }
            
            QPushButton#toolButton:hover {
                background-color: #1a1a1a;
                border-color: #444444;
                color: #ffffff;
            }
            
            QPushButton#toolButton:pressed {
                background-color: #0a0a0a;
            }
            
            /* Console Styling */
            QFrame#consoleHeader {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #111111, stop:1 #1a1a1a);
                border: 1px solid #333333;
                border-radius: 8px 8px 0 0;
                color: #ffffff;
            }
            
            QLabel#consoleTitle {
                color: #ffffff;
                font-weight: bold;
            }
            
            QLabel#statusIndicator {
                color: #ffffff;
                font-weight: bold;
            }
            
            QFrame#consoleFrame {
                background-color: #000000;
                border: 1px solid #222222;
                border-radius: 0 0 8px 8px;
            }
            
            QTextEdit#consoleOutput {
                background-color: #000000;
                color: #00ff00;
                border: none;
                font-family: 'JetBrains Mono', 'Consolas', monospace;
                selection-background-color: #333333;
                selection-color: #ffffff;
            }
            
            /* Progress Bar */
            QFrame#progressContainer {
                background-color: #111111;
                border: 1px solid #222222;
                border-radius: 6px;
            }
            
            QProgressBar#modernProgressBar {
                border: none;
                background-color: #1a1a1a;
                border-radius: 4px;
                text-align: center;
                color: #ffffff;
            }
            
            QProgressBar#modernProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #333333, stop:1 #555555);
                border-radius: 4px;
            }
            
            /* Quick Actions */
            QFrame#quickActionsFrame {
                background-color: #111111;
                border: 1px solid #222222;
                border-radius: 8px;
            }
            
            QLabel#sectionLabel {
                color: #ffffff;
                font-weight: bold;
            }
            
            QLabel#progressLabel {
                color: #cccccc;
            }
            
            /* Scroll Areas */
            QScrollArea#categoryScrollArea {
                border: none;
                background-color: transparent;
            }
            
            QScrollBar:vertical {
                background-color: #111111;
                width: 12px;
                border-radius: 6px;
                border: 1px solid #222222;
            }
            
            QScrollBar::handle:vertical {
                background-color: #333333;
                border-radius: 6px;
                min-height: 20px;
                border: 1px solid #444444;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: #555555;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background-color: #1a1a1a;
                border: 1px solid #333333;
            }
            
            /* Menu Bar */
            QMenuBar {
                background-color: #000000;
                color: #ffffff;
                border-bottom: 1px solid #222222;
                padding: 4px;
            }
            
            QMenuBar::item {
                background-color: transparent;
                padding: 8px 12px;
                border-radius: 4px;
            }
            
            QMenuBar::item:selected {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            
            QMenu {
                background-color: #111111;
                color: #ffffff;
                border: 1px solid #333333;
                border-radius: 6px;
                padding: 4px;
            }
            
            QMenu::item {
                padding: 8px 20px;
                border-radius: 4px;
            }
            
            QMenu::item:selected {
                background-color: #1a1a1a;
                color: #ffffff;
            }
            
            /* Status Bar */
            QStatusBar {
                background-color: #000000;
                color: #cccccc;
                border-top: 1px solid #222222;
            }
            
            /* Message Boxes */
            QMessageBox {
                background-color: #111111;
                color: #ffffff;
            }
            
            QMessageBox QPushButton {
                background-color: #1a1a1a;
                color: #ffffff;
                border: 1px solid #333333;
                border-radius: 4px;
                padding: 6px 12px;
            }
            
            QMessageBox QPushButton:hover {
                background-color: #333333;
            }
            
            /* File Dialog */
            QFileDialog {
                background-color: #111111;
                color: #ffffff;
            }
            
            /* Splitter */
            QSplitter::handle {
                background-color: #222222;
                width: 3px;
                border-radius: 1px;
            }
            
            QSplitter::handle:hover {
                background-color: #444444;
            }
        """)
    
    def show_about(self):
        """Show professional about dialog"""
        about_text = f"""
<div style='text-align: center; background-color: #111111; color: #ffffff; padding: 20px;'>
<h2 style='color: #ffffff;'>🌑 PC Troubleshooter v1.0</h2>
<h3 style='color: #cccccc;'>Professional System Diagnostics Tool</h3>
<h4 style='color: #aaaaaa;'>COMPLETE BLACK DARK MODE</h4>
<hr style='border-color: #333333;'>
<p style='color: #ffffff;'><b>Features:</b></p>
<ul style='text-align: left; color: #cccccc;'>
<li>🌐 Network connectivity troubleshooting</li>
<li>📶 Bluetooth device management</li>
<li>🔊 Audio system diagnostics</li>
<li>🖥️ Display and graphics fixes</li>
<li>💾 Storage cleanup and optimization</li>
<li>⚡ Performance monitoring and tuning</li>
</ul>
<hr style='border-color: #333333;'>
<p style='color: #ffffff;'><b>Technology Stack:</b><br>
<span style='color: #aaaaaa;'>Python 3.13 • PyQt6 • Windows Batch Scripts</span></p>
<p style='color: #ffffff;'><b>Compatibility:</b><br>
<span style='color: #aaaaaa;'>Windows 10/11 • Administrator privileges recommended</span></p>
<p style='color: #ffffff;'><b>Current Theme:</b><br>
<span style='color: #00ff00;'>{'Complete Black Dark Mode' if self.current_theme == 'dark' else 'Professional Light Mode'}</span></p>
<hr style='border-color: #333333;'>
<p style='color: #aaaaaa;'><i>Built for IT professionals and power users</i></p>
</div>
"""
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("About PC Troubleshooter")
        msg_box.setTextFormat(Qt.TextFormat.RichText)
        msg_box.setText(about_text)
        msg_box.setIconPixmap(self.style().standardIcon(
            self.style().StandardPixmap.SP_ComputerIcon).pixmap(64, 64))
        msg_box.exec()
    
    def closeEvent(self, event):
        """Handle application close event"""
        reply = QMessageBox.question(self, "Exit Application", 
                                   "Are you sure you want to exit?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
