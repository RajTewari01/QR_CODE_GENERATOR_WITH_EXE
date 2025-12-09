<div align="center">

<pre>
██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗
██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   █████╗  
██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  
╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗
 ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
 
  Q R   C O D E   G E N E R A T O R   P R O
</pre>

[![License](https://img.shields.io/github/license/RajTewari01/QR_CODE_GENERATOR_WITH_EXE?style=for-the-badge&color=blue)](https://github.com/RajTewari01/QR_CODE_GENERATOR_WITH_EXE/blob/main/LICENSE)
[![GUI Framework](https://img.shields.io/badge/GUI-PyQt5-41cd52?style=for-the-badge&logo=qt)](https://pypi.org/project/PyQt5/)
[![Build](https://img.shields.io/badge/Build-PyInstaller-red?style=for-the-badge&logo=python)](https://pyinstaller.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://github.com/RajTewari01)

<br>

<h3><b>The Definitive Offline QR Solution.</b></h3>
<i>Built with the power of PyQt for a modern, responsive interface.</i>

<p>
<a href="#-workflow-architecture">View Architecture</a> •
<a href="#-build-executable">Build App</a> •
<a href="#-features">Features</a>
</p>

</div>

---

## 🏗️ Workflow Architecture

This application utilizes the **PyQt Event Loop** to handle user inputs asynchronously. The separation of GUI signals and the generation logic ensures the app remains freezing-free during rendering.

```mermaid
graph TD
    subgraph "PyQt User Interface"
    A[Start App] --> B{User Input}
    B -->|Link/Text| C[Deep Link Module]
    B -->|SSID/Pass| D[Wi-Fi Config Module]
    B -->|Contact Info| E[vCard Module]
    end

    subgraph "Backend Logic"
    C & D & E -->|Signal Emitted| F[Data Validator]
    F --> G[QR Engine (Python qrcode)]
    G --> H[Pillow Image Renderer]
    end

    subgraph "Output Pipeline"
    H -->|Pixmap| I[Update GUI Preview]
    H -->|Binary Write| J[Save .PNG/.SVG to Disk]
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#bbf,stroke:#333,stroke-width:2px
    style I fill:#bfb,stroke:#333,stroke-width:2px
