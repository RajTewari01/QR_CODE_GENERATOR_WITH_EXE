import sys
import os
import urllib.parse
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QComboBox, QFrame, QGraphicsDropShadowEffect, 
                             QScrollArea, QColorDialog, QFormLayout)
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import (QColor, QLinearGradient, QRadialGradient, QPalette, 
                         QBrush, QPainter, QFont, QPixmap, QImage, QPen)

# Dependencies
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import (
    RadialGradiantColorMask, VerticalGradiantColorMask,
    HorizontalGradiantColorMask, SquareGradiantColorMask
)
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import ImageQt

# ======================= DATA MAPPING =========================
INPUT_MAP = {
    "Website/URL": ["Paste URL"],
    "Wi-Fi Config": ["SSID (Network Name)", "Password", "Type (WPA/WEP)"],
    "Plain Text": ["Enter Text"],
    "vCard (Contact)": ["Full Name", "Phone", "Email", "Organization"],
    "Send SMS": ["Phone Number", "Message"],
    "Send Email": ["To Email", "Subject", "Body"],
    "WhatsApp Msg": ["Phone (w/ Country Code)", "Message"],
    "YouTube Video": ["Video ID"],
    "UPI (India)": ["UPI ID", "Payee Name", "Amount (Optional)"],
    "Geo Coords": ["Latitude", "Longitude"],
}

# ======================= LOGIC ENGINE =========================
class QrLogic:
    def format_data(self, mode, i):
        try:
            if not i or not i[0]: return "Empty" # Prevent crash on empty input
            if mode == "Website/URL" or mode == "Plain Text": return i[0]
            if mode == "Wi-Fi Config": return f"WIFI:S:{i[0]};T:{i[2]};P:{i[1]};;"
            if mode == "Send SMS": return f"SMSTO:{i[0]}:{i[1]}"
            if mode == "Send Email": return f"mailto:{i[0]}?subject={i[1]}&body={i[2]}"
            if mode == "WhatsApp Msg": return f"https://wa.me/{i[0]}?text={urllib.parse.quote(i[1])}"
            if mode == "UPI (India)": return f"upi://pay?pa={i[0]}&pn={urllib.parse.quote(i[1])}"
            return i[0]
        except:
            return "Error"

    def generate_image(self, data, gradient_type, colors):
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(data)
        qr.make(fit=True)

        mask_map = {
            "Radial": RadialGradiantColorMask, "Vertical": VerticalGradiantColorMask,
            "Horizontal": HorizontalGradiantColorMask, "Square": SquareGradiantColorMask
        }
        
        # Convert QColors or Hex to RGB Tuple
        rgb_colors = []
        for c in colors:
            if isinstance(c, str):
                c = c.lstrip('#')
                rgb_colors.append(tuple(int(c[i:i+2], 16) for i in (0, 2, 4)))
            else:
                rgb_colors.append((c.red(), c.green(), c.blue()))

        bg = rgb_colors[0]
        c_start = rgb_colors[1] # Core/Top/Left
        c_end = rgb_colors[2]   # Edge/Bottom/Right

        mask_cls = mask_map.get(gradient_type, RadialGradiantColorMask)

        # LOGIC FIX: Initialize mask based on type to avoid keyword errors
        if gradient_type == "Vertical":
            mask = mask_cls(back_color=bg, top_color=c_start, bottom_color=c_end)
        elif gradient_type == "Horizontal":
            mask = mask_cls(back_color=bg, left_color=c_start, right_color=c_end)
        else:
            # Radial and Square
            mask = mask_cls(back_color=bg, center_color=c_start, edge_color=c_end)

        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=mask
        )
        return img

# ======================= UI COMPONENTS =========================

class GlassFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(30, 30, 45, 180); 
                border: 1px solid rgba(255, 255, 255, 30);
                border-radius: 20px;
            }
        """)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 15)
        self.setGraphicsEffect(shadow)

class NeonButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(50)
        self.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00f260, stop:1 #0575e6);
                color: white;
                font-weight: bold;
                font-size: 16px;
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00e055, stop:1 #0465c5);
                margin-top: -2px;
            }
            QPushButton:pressed {
                margin-top: 2px;
            }
        """)

class GalaxyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = QrLogic()
        self.colors = [QColor("white"), QColor("#00f260"), QColor("#0575e6")] # BG, Center, Edge
        
        self.setWindowTitle("Galaxy AI | QR Core")
        self.resize(1000, 700)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout(self.central_widget)
        
        self.glass_panel = GlassFrame()
        self.glass_panel_layout = QHBoxLayout(self.glass_panel)
        self.glass_panel_layout.setContentsMargins(30, 30, 30, 30)
        self.glass_panel_layout.setSpacing(30)
        
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.glass_panel)
        self.main_layout.addStretch()
        
        # LEFT PANEL
        self.left_panel = QVBoxLayout()
        title = QLabel("SYSTEM CONFIG")
        title.setStyleSheet("color: #00f260; font-weight: bold; font-size: 14px; letter-spacing: 2px;")
        self.left_panel.addWidget(title)
        
        lbl_mode = QLabel("Data Protocol")
        lbl_mode.setStyleSheet("color: #aaa; margin-top: 10px;")
        self.left_panel.addWidget(lbl_mode)
        
        self.combo_mode = QComboBox()
        self.combo_mode.addItems(INPUT_MAP.keys())
        self.combo_mode.setStyleSheet(self.get_input_style())
        self.combo_mode.currentIndexChanged.connect(self.update_inputs)
        self.left_panel.addWidget(self.combo_mode)
        
        lbl_grad = QLabel("Gradient Field")
        lbl_grad.setStyleSheet("color: #aaa; margin-top: 10px;")
        self.left_panel.addWidget(lbl_grad)
        
        self.combo_grad = QComboBox()
        self.combo_grad.addItems(["Radial", "Vertical", "Horizontal", "Square"])
        self.combo_grad.setStyleSheet(self.get_input_style())
        self.left_panel.addWidget(self.combo_grad)

        lbl_col = QLabel("Visual Spectrum")
        lbl_col.setStyleSheet("color: #aaa; margin-top: 10px;")
        self.left_panel.addWidget(lbl_col)
        
        btn_layout = QHBoxLayout()
        self.btn_bg = self.create_color_btn("BG", 0)
        self.btn_c = self.create_color_btn("Core", 1)
        self.btn_e = self.create_color_btn("Edge", 2)
        btn_layout.addWidget(self.btn_bg)
        btn_layout.addWidget(self.btn_c)
        btn_layout.addWidget(self.btn_e)
        self.left_panel.addLayout(btn_layout)

        self.left_panel.addStretch()
        self.glass_panel_layout.addLayout(self.left_panel, 35)
        
        # RIGHT PANEL
        self.right_panel = QVBoxLayout()
        self.input_widget = QWidget()
        self.input_layout = QVBoxLayout(self.input_widget)
        self.input_layout.setContentsMargins(0,0,0,0)
        self.right_panel.addWidget(self.input_widget)
        
        self.preview_lbl = QLabel()
        self.preview_lbl.setAlignment(Qt.AlignCenter)
        self.preview_lbl.setStyleSheet("""
            QLabel {
                background-color: rgba(0,0,0,0.3);
                border: 2px solid rgba(255,255,255,0.1);
                border-radius: 10px;
            }
        """)
        self.preview_lbl.setMinimumSize(250, 250)
        self.right_panel.addWidget(self.preview_lbl)
        
        self.btn_gen = NeonButton("INITIALIZE GENERATION")
        self.btn_gen.clicked.connect(self.generate)
        self.right_panel.addWidget(self.btn_gen)
        
        self.glass_panel_layout.addLayout(self.right_panel, 65)

        self.update_inputs()

    def get_input_style(self):
        return """
            QWidget {
                background-color: rgba(0, 0, 0, 0.4);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: white;
                padding: 8px;
                border-radius: 5px;
                font-size: 14px;
            }
            QWidget:focus {
                border: 1px solid #00f260;
            }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #2b2b2b;
                color: white;
                selection-background-color: #0575e6;
            }
        """

    def create_color_btn(self, text, idx):
        btn = QPushButton(text)
        btn.setStyleSheet(f"background-color: {self.colors[idx].name()}; color: black; border-radius: 5px; padding: 5px;")
        btn.clicked.connect(lambda: self.pick_color(idx, btn))
        return btn

    def pick_color(self, idx, btn):
        col = QColorDialog.getColor()
        if col.isValid():
            self.colors[idx] = col
            txt_col = "black" if (col.red()*0.299 + col.green()*0.587 + col.blue()*0.114) > 186 else "white"
            btn.setStyleSheet(f"background-color: {col.name()}; color: {txt_col}; border-radius: 5px; padding: 5px;")

    def update_inputs(self):
        for i in reversed(range(self.input_layout.count())): 
            self.input_layout.itemAt(i).widget().setParent(None)
        
        mode = self.combo_mode.currentText()
        fields = INPUT_MAP.get(mode, ["Input"])
        
        self.current_entries = []
        for f in fields:
            l = QLabel(f.upper())
            l.setStyleSheet("color: #00f260; font-size: 10px; font-weight: bold; margin-top: 5px;")
            self.input_layout.addWidget(l)
            
            e = QLineEdit()
            e.setPlaceholderText(f"Enter {f}...")
            e.setStyleSheet(self.get_input_style())
            self.input_layout.addWidget(e)
            self.current_entries.append(e)
        
        self.right_panel.addStretch()

    def generate(self):
        inputs = [e.text() for e in self.current_entries]
        mode = self.combo_mode.currentText()
        grad = self.combo_grad.currentText()
        
        data_str = self.logic.format_data(mode, inputs)
        pil_img = self.logic.generate_image(data_str, grad, self.colors)
        
        im_data = pil_img.convert("RGBA").tobytes("raw", "RGBA")
        qim = QImage(im_data, pil_img.size[0], pil_img.size[1], QImage.Format_RGBA8888)
        pix = QPixmap.fromImage(qim)
        
        self.preview_lbl.setPixmap(pix.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        gradient = QRadialGradient(self.width()/2, self.height(), self.width())
        gradient.setColorAt(0, QColor("#1b2735"))
        gradient.setColorAt(1, QColor("#090a0f"))
        painter.fillRect(self.rect(), gradient)
        
        import random
        painter.setPen(Qt.white)
        for _ in range(100):
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            opacity = random.randint(50, 255)
            painter.setPen(QColor(255, 255, 255, opacity))
            size = random.randint(1, 3)
            painter.drawEllipse(x, y, size, size)
            
        glow = QRadialGradient(self.width(), self.height(), 400)
        glow.setColorAt(0, QColor(5, 117, 230, 80))
        glow.setColorAt(1, Qt.transparent)
        painter.setBrush(QBrush(glow))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPoint(self.width(), self.height()), 600, 600)

        glow2 = QRadialGradient(0, 0, 400)
        glow2.setColorAt(0, QColor(0, 242, 96, 60))
        glow2.setColorAt(1, Qt.transparent)
        painter.setBrush(QBrush(glow2))
        painter.drawEllipse(QPoint(0, 0), 500, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    window = GalaxyWindow()
    window.show()
    sys.exit(app.exec_())