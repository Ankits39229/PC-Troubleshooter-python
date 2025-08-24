"""
Custom widgets for professional UI styling
"""

from PyQt6.QtWidgets import QPushButton, QFrame, QLabel
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QPainter, QColor, QPalette

class AnimatedButton(QPushButton):
    """A button with hover animations"""
    
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                background-color: #007acc;
                color: white;
            }
            QPushButton:hover {
                background-color: #0088dd;
            }
            QPushButton:pressed {
                background-color: #0066aa;
            }
        """)

class ProfessionalCard(QFrame):
    """A professional-looking card widget"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Shape.NoFrame)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #e9ecef;
                border-radius: 12px;
                margin: 5px;
            }
            QFrame:hover {
                border-color: #007acc;
                background-color: #f8f9fa;
            }
        """)

class StatusIndicator(QLabel):
    """A status indicator with color coding"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(12, 12)
        self.setStyleSheet("""
            QLabel {
                border-radius: 6px;
                background-color: #28a745;
            }
        """)
    
    def set_status(self, status):
        """Set status: 'ready', 'running', 'error'"""
        colors = {
            'ready': '#28a745',   # Green
            'running': '#ffc107', # Yellow
            'error': '#dc3545'    # Red
        }
        
        color = colors.get(status, '#6c757d')
        self.setStyleSheet(f"""
            QLabel {{
                border-radius: 6px;
                background-color: {color};
            }}
        """)
