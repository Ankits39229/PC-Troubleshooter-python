#!/usr/bin/env python3
"""
PC Troubleshooter - Windows Desktop Application
Built with PyQt6 and Batch/PowerShell scripts
"""

import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    # Create the application
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("PC Troubleshooter")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("PC Troubleshooter")
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    # Run the application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
