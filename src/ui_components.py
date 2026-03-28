from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QLabel,
                             QFrame, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QMouseEvent


# ── Apple premium font stack ──────────────────────────────────
FONT = '".AppleSystemUIFont", -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Arial, sans-serif'


class TrafficLightButton(QPushButton):
    """macOS-style traffic light window control."""

    def __init__(self, color, hover_color, icon_char="", parent=None):
        super().__init__(parent)
        self.setFixedSize(12, 12)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: 6px;
                border: 0.5px solid rgba(0,0,0,0.25);
                font-size: 8px;
                font-weight: 800;
                font-family: {FONT};
                color: transparent;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
                color: rgba(0,0,0,0.5);
            }}
        """)
        if icon_char:
            self.setText(icon_char)


class CustomTitleBar(QWidget):
    """Frameless title bar with macOS traffic lights."""

    def __init__(self, parent, theme_key):
        super().__init__(parent)
        self.parent_window = parent
        self.setFixedHeight(38)
        self.layout_box = QHBoxLayout(self)
        self.layout_box.setContentsMargins(16, 0, 16, 0)
        self.layout_box.setSpacing(0)

        # Traffic lights (macOS dimensions)
        self.btn_close = TrafficLightButton("#FF5F56", "#FF5F56", "✕", self)
        self.btn_min = TrafficLightButton("#FFBD2E", "#FFBD2E", "−", self)
        self.btn_max = TrafficLightButton("#27C93F", "#27C93F", "+", self)

        self.btn_close.clicked.connect(self.parent_window.close)
        self.btn_min.clicked.connect(self.parent_window.showMinimized)
        self.btn_max.clicked.connect(self.toggle_max)

        self.layout_box.addWidget(self.btn_close)
        self.layout_box.addSpacing(8)
        self.layout_box.addWidget(self.btn_min)
        self.layout_box.addSpacing(8)
        self.layout_box.addWidget(self.btn_max)

        self.title_label = QLabel(f"Galaxy QR Core", self)
        self.title_label.setStyleSheet(f"""
            color: rgba(255, 255, 255, 0.7);
            font-weight: 500;
            font-size: 13px;
            font-family: {FONT};
            letter-spacing: 0.5px;
        """)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.layout_box.addStretch()
        self.layout_box.addWidget(self.title_label)
        self.layout_box.addStretch()
        self.layout_box.addSpacing(56) # Keep label dead center

        self._is_tracking = False
        self._start_pos = None

    def toggle_max(self):
        if self.parent_window.isMaximized():
            self.parent_window.showNormal()
        else:
            self.parent_window.showMaximized()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._is_tracking = True
            self._start_pos = event.globalPos() - self.parent_window.frameGeometry().topLeft()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._is_tracking and self._start_pos is not None:
            self.parent_window.move(event.globalPos() - self._start_pos)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._is_tracking = False


class GlassPanel(QFrame):
    """Premium frosted glass panel with mirror border."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("GlassPanel")
        
        # Apple mirror glass aesthetic: very subtle translucent fill, glossy inner border
        self.setStyleSheet(f"""
            QFrame#GlassPanel {{
                background-color: rgba(20, 20, 25, 0.45);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-top: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 12px;
            }}
        """)
        
        # Soft environmental shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 8)
        self.setGraphicsEffect(shadow)


class PrimaryButton(QPushButton):
    """Premium macOS generic generation button."""

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(36)
        
        # Apple SF Pro Blue Gradient style
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: #0A84FF;
                color: white;
                font-weight: 600;
                font-family: {FONT};
                font-size: 13px;
                letter-spacing: 0.5px;
                border: 1px solid rgba(0, 0, 0, 0.15);
                border-top: 1px solid rgba(255, 255, 255, 0.25);
                border-radius: 8px;
            }}
            QPushButton:hover {{
                background-color: #1A8CFF;
            }}
            QPushButton:pressed {{
                background-color: #0074E8;
            }}
        """)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(10, 132, 255, 80))
        shadow.setOffset(0, 4)
        self.setGraphicsEffect(shadow)
