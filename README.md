<div align="center">

# 🌌 GALAXY QR CORE 🌌

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=300&section=header&text=Galaxy%20QR%20Core&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Next-Generation%20QR%20Code%20Generation&descAlignY=55&descSize=25)

### ✨ *Cinematic Gradient QR Codes with Space-Age Technology* ✨

[![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)](https://python.org)
[![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://pypi.org/project/PyQt5/)
[![License](https://img.shields.io/badge/License-MIT-00F7FF?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-🌟_Production-00FF41?style=for-the-badge)]()

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📖 Docs](#-documentation) • [🤝 Contribute](#-contribute)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 🎬 Application Workflow

<div align="center">

![Workflow Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=System%20Flow&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 
  'primaryColor':'#1a0d2e',
  'primaryTextColor':'#00f7ff',
  'primaryBorderColor':'#00f7ff',
  'lineColor':'#ff00ff',
  'secondaryColor':'#0f0728',
  'tertiaryColor':'#1e1034',
  'fontSize':'14px'
}}}%%

graph TB
    START([🚀 Launch Galaxy QR]):::startNode
    
    subgraph INPUT [" 📡 DATA INPUT LAYER "]
        PROTOCOL{Select Protocol Type}:::decision
        URL[🔗 Website/URL]:::protocol
        WIFI[📶 Wi-Fi Config]:::protocol
        TEXT[📝 Plain Text]:::protocol
        VCARD[👤 vCard Contact]:::protocol
        SMS[💬 SMS Message]:::protocol
        EMAIL[📧 Email]:::protocol
        WHATSAPP[📱 WhatsApp]:::protocol
        YOUTUBE[🎥 YouTube]:::protocol
        UPI[💳 UPI Payment]:::protocol
        GEO[🌍 Geo Location]:::protocol
    end
    
    subgraph CUSTOM [" 🎨 CUSTOMIZATION ENGINE "]
        GRADIENT[🌈 Gradient Selection<br/>Radial • Vertical • Horizontal • Square]:::customize
        COLORS[🎭 Color Palette<br/>Background • Core • Edge]:::customize
        STYLE[✨ Module Design<br/>Rounded • Sharp • Custom]:::customize
    end
    
    subgraph PROCESS [" ⚛️ QUANTUM PROCESSOR "]
        VALIDATE[🛡️ Input Validation]:::process
        FORMAT[🔬 Data Formatting]:::process
        GENERATE[💫 QR Generation<br/>High Error Correction]:::process
        RENDER[🌈 Gradient Rendering]:::process
    end
    
    subgraph OUTPUT [" 💾 OUTPUT SYSTEM "]
        PREVIEW[👁️ Live Preview]:::output
        SAVE[📦 Export Options<br/>PNG • SVG • High-Res]:::output
    end
    
    DONE([🎉 QR Code Ready!]):::endNode
    
    START --> PROTOCOL
    PROTOCOL --> URL & WIFI & TEXT & VCARD & SMS & EMAIL & WHATSAPP & YOUTUBE & UPI & GEO
    URL & WIFI & TEXT & VCARD & SMS & EMAIL & WHATSAPP & YOUTUBE & UPI & GEO --> GRADIENT
    GRADIENT --> COLORS
    COLORS --> STYLE
    STYLE --> VALIDATE
    VALIDATE --> FORMAT
    FORMAT --> GENERATE
    GENERATE --> RENDER
    RENDER --> PREVIEW
    PREVIEW --> SAVE
    SAVE --> DONE
    
    classDef startNode fill:#1a0d2e,stroke:#00f7ff,stroke-width:4px,color:#00f7ff
    classDef endNode fill:#0f0728,stroke:#00ff41,stroke-width:4px,color:#00ff41
    classDef decision fill:#1e1034,stroke:#ff00ff,stroke-width:3px,color:#00f7ff
    classDef protocol fill:#0f0728,stroke:#00f7ff,stroke-width:2px,color:#00f7ff
    classDef customize fill:#1a0d2e,stroke:#ffd700,stroke-width:2px,color:#ffd700
    classDef process fill:#1e1034,stroke:#ff00ff,stroke-width:2px,color:#ff00ff
    classDef output fill:#0f0728,stroke:#00f7ff,stroke-width:2px,color:#00f7ff
```

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="700">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 🏗️ System Architecture

<div align="center">

![Architecture Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Core%20Architecture&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

```mermaid
%%{init: {'theme':'base', 'themeVariables': {
  'primaryColor':'#0f0728',
  'primaryTextColor':'#00f7ff',
  'primaryBorderColor':'#00f7ff',
  'lineColor':'#ff00ff',
  'secondaryColor':'#1a0d2e',
  'tertiaryColor':'#1e1034'
}}}%%

graph LR
    subgraph UI [" 🎮 USER INTERFACE LAYER "]
        GUI[Galaxy Window<br/>Glass Morphism Design]
        CONTROLS[Dynamic Controls<br/>ComboBox • Input Fields]
        COLORPICK[Color Picker System<br/>RGB Selection]
        CANVAS[Preview Canvas<br/>Real-time Display]
    end
    
    subgraph LOGIC [" 🧠 BUSINESS LOGIC CORE "]
        QRLOGIC[QR Logic Engine]
        FORMATTER[Protocol Formatter<br/>10+ Data Types]
        GENERATOR[Image Generator<br/>Gradient Engine]
    end
    
    subgraph LIBS [" 📚 LIBRARY STACK "]
        PYQT[PyQt5<br/>GUI Framework]
        QRCODE[qrcode<br/>QR Engine]
        PILLOW[Pillow<br/>Image Processing]
    end
    
    subgraph RENDER [" 🎨 RENDERING PIPELINE "]
        MASKS[Gradient Masks<br/>4 Types]
        DRAWER[Module Drawer<br/>Rounded Style]
        CONVERTER[Format Converter<br/>PIL → QPixmap]
    end
    
    GUI --> CONTROLS
    CONTROLS --> FORMATTER
    COLORPICK --> GENERATOR
    FORMATTER --> GENERATOR
    GENERATOR --> MASKS
    MASKS --> DRAWER
    DRAWER --> CONVERTER
    CONVERTER --> CANVAS
    
    PYQT -.->|Powers| GUI
    QRCODE -.->|Engine| GENERATOR
    PILLOW -.->|Processing| CONVERTER
    
    classDef uiStyle fill:#1a0d2e,stroke:#00f7ff,stroke-width:3px,color:#00f7ff
    classDef logicStyle fill:#0f0728,stroke:#ff00ff,stroke-width:3px,color:#ff00ff
    classDef libStyle fill:#1e1034,stroke:#ffd700,stroke-width:3px,color:#ffd700
    classDef renderStyle fill:#1a0d2e,stroke:#00ff41,stroke-width:3px,color:#00ff41
    
    class GUI,CONTROLS,COLORPICK,CANVAS uiStyle
    class QRLOGIC,FORMATTER,GENERATOR logicStyle
    class PYQT,QRCODE,PILLOW libStyle
    class MASKS,DRAWER,CONVERTER renderStyle
```

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## ✨ Features

<div align="center">

![Features Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Galaxy%20Features&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

<table>
<tr>
<td width="50%" valign="top">

### 🎨 Visual Excellence

- 🌌 Space-themed Galaxy UI
- 💎 Glass morphism effects
- ✨ Glowing neon buttons
- 🌠 Smooth animations
- 🎭 Custom color palettes
- 🖼️ Real-time preview
- 🌈 Dynamic gradients
- ⚡ Responsive design

</td>
<td width="50%" valign="top">

### 🔒 Privacy First

- 🛡️ 100% Offline operation
- 🔐 No cloud uploads
- 💻 Local processing only
- 🚫 No telemetry
- 🌐 No analytics
- 👤 Private by design
- 📊 No data collection
- ✅ GDPR compliant

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎭 Gradient Magic

- 🌈 Radial gradient
- 📊 Vertical gradient
- ↔️ Horizontal gradient
- ⬜ Square gradient
- 🎨 Custom RGB colors
- 🖌️ 3-point color mixing
- 👁️ Live preview
- 🌟 High contrast modes

</td>
<td width="50%" valign="top">

### ⚡ Smart Generation

- 💫 High error correction
- ⭕ Rounded modules
- 🔄 Auto-format protocols
- ⚡ Instant generation
- 📝 Dynamic input fields
- ✅ Input validation
- 🛡️ Crash prevention
- 🔍 Empty check safety

</td>
</tr>
</table>

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="700">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 📡 Supported Protocols

<div align="center">

![Protocols Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Data%20Protocols&fontSize=40&fontColor=fff&animation=fadeIn)

```
╔══════════════════════════════════════════════════════════════════════╗
║                     10+ PROTOCOL SUPPORT MATRIX                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

| Icon | Protocol | Format | Use Case |
|:----:|:---------|:-------|:---------|
| 🔗 | **Website/URL** | Standard URL | Direct web links |
| 📶 | **Wi-Fi Config** | `WIFI:S:SSID;T:WPA;P:password;;` | Network sharing |
| 📝 | **Plain Text** | Any text | General text data |
| 👤 | **vCard Contact** | VCF format | Business cards |
| 💬 | **SMS Message** | `SMSTO:phone:message` | Quick texting |
| 📧 | **Email** | `mailto:email@domain.com` | Email composition |
| 📱 | **WhatsApp** | `https://wa.me/number?text=msg` | WhatsApp chat |
| 🎥 | **YouTube** | Video URL | Video sharing |
| 💳 | **UPI Payment** | `upi://pay?pa=id@bank` | Indian payments |
| 🌍 | **Geo Location** | `geo:lat,long` | GPS coordinates |

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 🚀 Quick Start

<div align="center">

![Quick Start Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Installation&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

### 📋 Prerequisites

```yaml
Python: 3.8 or higher (Recommended: 3.10+)
RAM: 2GB minimum
Storage: 50MB free space
OS: Windows | macOS | Linux
```

### 🔧 Installation Steps

```bash
# ═══════════════════════════════════════════════════════
# STEP 1: Clone the repository
# ═══════════════════════════════════════════════════════
git clone https://github.com/RajTewari01/QR_CODE_GENERATOR_WITH_EXE.git
cd QR_CODE_GENERATOR_WITH_EXE

# ═══════════════════════════════════════════════════════
# STEP 2: Install dependencies
# ═══════════════════════════════════════════════════════
pip install -r requirements.txt

# Or install manually
pip install PyQt5 qrcode[pil] pillow

# ═══════════════════════════════════════════════════════
# STEP 3: Launch application
# ═══════════════════════════════════════════════════════
python qr.py
```

### 🔨 Build Executable (Optional)

```bash
# Install PyInstaller
pip install pyinstaller

# Build standalone executable
pyinstaller --noconsole --onefile --name "GalaxyQR" qr.py

# Find the executable in dist/ folder
```

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284094-e50ddb5f-e8b1-4e2c-a525-021e428c5018.gif" width="700">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 📖 Documentation

<div align="center">

![Docs Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Usage%20Guide&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

### 🎯 How to Use

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 → Launch Application                                    │
│           Run: python qr.py                                      │
│                                                                   │
│  STEP 2 → Select Protocol                                       │
│           Choose from 10+ data types                             │
│                                                                   │
│  STEP 3 → Enter Data                                            │
│           Fill in dynamic fields                                 │
│                                                                   │
│  STEP 4 → Customize Appearance                                  │
│           ├─ Select gradient type                                │
│           ├─ Pick background color                               │
│           ├─ Pick core color                                     │
│           └─ Pick edge color                                     │
│                                                                   │
│  STEP 5 → Generate QR Code                                      │
│           Click "INITIALIZE GENERATION"                          │
│                                                                   │
│  STEP 6 → Export                                                │
│           Save as PNG or SVG                                     │
└─────────────────────────────────────────────────────────────────┘
```

### 🎨 Gradient Types Explained

```
┌──────────────────────────────────────────────────────────────┐
│  RADIAL       VERTICAL      HORIZONTAL      SQUARE           │
│                                                                │
│    ●●●          ████           ██████         ■■■■■■         │
│   ●  ●         ████           ██████         ■    ■         │
│  ●    ●        ████           ██████         ■    ■         │
│   ●  ●         ░░░░           ░░░░░░         ■    ■         │
│    ●●●          ░░░░           ░░░░░░         ■■■■■■         │
│                                                                │
│  Center→Edge  Top→Bottom    Left→Right    Center→Corners     │
└──────────────────────────────────────────────────────────────┘
```

### 📂 Project Structure

```
QR_CODE_GENERATOR_WITH_EXE/
├── qr.py                      # 🚀 Main application
├── RAJ_UltimateQR.exe         # 💫 Pre-built executable
├── requirements.txt           # 📦 Dependencies
├── README.md                  # 📖 Documentation
├── LICENSE                    # 📜 MIT License
├── generated_assets/          # 💾 Output folder
│   └── qrcode/
│       ├── QrCode_SVG1.png
│       ├── LOGO/
│       └── SVG/
└── logs/                      # 📋 Application logs
    └── module_logs/
        ├── Qr_Log.log
        └── Qr_svg_Log.log
```

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284119-fbfd994d-8c2a-4a07-a75f-84e513833c33.gif" width="700">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 🎓 Code Example

<div align="center">

![Code Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Code%20Example&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

```python
from qrcode import QRCode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
import qrcode.constants

# ═══════════════════════════════════════════════════════
# Initialize QR code with high error correction
# ═══════════════════════════════════════════════════════
qr = QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://github.com/RajTewari01")
qr.make(fit=True)

# ═══════════════════════════════════════════════════════
# Generate with gradient styling
# ═══════════════════════════════════════════════════════
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        back_color=(255, 255, 255),    # White background
        center_color=(0, 242, 96),      # Green center
        edge_color=(5, 117, 230)        # Blue edge
    )
)

# ═══════════════════════════════════════════════════════
# Save the QR code
# ═══════════════════════════════════════════════════════
img.save("galaxy_qr.png")
```

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284145-bf2c01a8-c448-4f1a-b911-996024c84606.gif" width="400">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 🤝 Contribute

<div align="center">

![Contribute Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=Contribute&fontSize=40&fontColor=fff&animation=fadeIn)

```
╔════════════════════════════════════════════════════════╗
║         JOIN THE GALAXY QR DEVELOPMENT TEAM!           ║
╚════════════════════════════════════════════════════════╝
```

</div>

### 🛠️ How to Contribute

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/QR_CODE_GENERATOR_WITH_EXE.git

# 3. Create a feature branch
git checkout -b feature/amazing-feature

# 4. Make your changes
# 5. Commit changes
git commit -m "✨ Add amazing feature"

# 6. Push to fork
git push origin feature/amazing-feature

# 7. Open Pull Request
```

### 💡 Contribution Areas

```
┌─────────────────────────────────────────────────────────┐
│  🐛 Bug Fixes              📱 Mobile Export Formats     │
│  ✨ New Gradient Styles    🎨 UI/UX Improvements        │
│  📖 Documentation          🌍 Internationalization      │
│  🧪 Test Coverage          🚀 Performance Optimization  │
└─────────────────────────────────────────────────────────┘
```

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284161-3e4947cf-87cc-4d41-a331-6e3f1bdeb6e2.gif" width="700">

</div>

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 📜 License

<div align="center">

![License Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=100&section=header&text=MIT%20License&fontSize=40&fontColor=fff&animation=fadeIn)

</div>

```
MIT License

Copyright (c) 2024 Biswadeep Tewari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

![Space Divider](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=6,11,20&height=3)

</div>

## 👨‍💻 Author

<div align="center">

![Author Banner](https://capsule-render.vercel.app/api?type=cylinder&color=gradient&customColorList=6,11,20&height=120&section=header&text=Biswadeep%20Tewari&fontSize=40&fontColor=fff&animation=fadeIn&desc=Computer%20Science%20Engineering%20•%20Python%20Developer&descAlignY=75&descSize=18)

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="100">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="100">

<br><br>

[![GitHub](https://img.shields.io/badge/GitHub-RajTewari01-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RajTewari01)
[![Email](https://img.shields.io/badge/Email-tewari765@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tewari765@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-light__up__my__world01-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/light_up_my_world01)

<br>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">

### ⭐ Star this repository if you find it helpful!

**Made with 💜 and ☕ by Biswadeep Tewari**

<br>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=150&section=footer&text=Thank%20You!&fontSize=50&fontColor=fff&animation=twinkling)

</div>
