# Linux Classroom in a Browser

**Linux Classroom** คือเว็บแอปพลิเคชันที่สร้างสภาพแวดล้อมการเรียนรู้ Linux แบบโต้ตอบได้ (Interactive) โดยตรงบนเว็บเบราว์เซอร์ เหมาะสำหรับใช้เป็นเครื่องมือฝึกสอน, จัด Workshop, หรือให้ผู้ที่สนใจได้ทดลองใช้คำสั่ง Linux, Python, และ Rust ได้อย่างปลอดภัยและสะดวกสบาย โดยไม่ต้องติดตั้งอะไรบนเครื่องคอมพิวเตอร์ของผู้เรียน

## update 2026-03-30

![image](https://github.com/nanofatdog/Linux-Classroom-pro/blob/main/image/demo1.png)

แต่ละเซสชันของผู้ใช้จะถูกแยกออกจากกันอย่างสมบูรณ์ใน Docker container ส่วนตัว ทำให้ผู้เรียนสามารถทดลองทุกอย่างได้อย่างอิสระโดยไม่ส่งผลกระทบต่อระบบหลักหรือผู้ใช้งานคนอื่น
![image](https://github.com/nanofatdog/Linux-Classroom-pro/blob/main/image/demo2.png)

## 🆕 Premium UI Release (2026-03-30)

### 🎨 **All-New Premium Student Interface**

**🌟 Premium Design Features:**
- **Dark/Light Theme System** with automatic switching
- **Modern Gradient Design** with glassmorphism effects
- **Smooth Animations** and interactive transitions
- **Professional Typography** using Inter & Fira Code fonts
- **Responsive Layout** optimized for all devices
- **Visual Feedback** for all user interactions

**🎯 Enhanced User Experience:**
- **Welcome Tutorial** with interactive onboarding
- **One-Click Command Copy** from beautifully designed cards
- **Visual Progress Tracking** with animated progress bar
- **Smart Tab System** with gradient-active indicators
- **Connection Status Indicator** with real-time feedback
- **Keyboard Shortcuts** for power users

**📱 Multiple Interface Options:**
- **`/`** - Premium UI with English lessons **(NEW DEFAULT)**
- **`/premium`** - Premium UI with English lessons
- **`/premium/thai`** - Premium UI with Thai lessons
- **`/thai`** - Premium UI with Thai lessons
- **`/improved`** - Previous improved UI
- **`/classic`** - Original classic UI

### 🚀 Major Student Experience Improvements

**🎯 Easier to Use Interface:**
- **Modern, intuitive design** with welcome tutorial for beginners
- **Tabbed sidebar** with Lessons, Help, Quick Commands, and Student Tools
- **One-click command copying** from help cards to terminal
- **Keyboard shortcuts**: Ctrl+L (clear), Ctrl+Space (toggle sidebar), Tab (auto-complete)
- **Terminal controls**: Clear, zoom, fullscreen buttons
- **Dual language support**: English (`/`) and Thai (`/thai`) lessons

**📚 Enhanced Learning Tools:**
- **Interactive beginner tutorial** (`linux-tutorial` command)
- **Quick help system** (`quick-help` command) with categorized commands
- **Classroom information** (`classroom-info` command) with container details
- **Built-in aliases**: `ll` (ls -la), `cls` (clear), `py` (python3), `rb` (cargo run)
- **20 new English lessons** covering Linux, Python, Rust basics to advanced
- **Step-by-step guidance** with practical examples

**🛠️ Student Assistance Features:**
- **Welcome message** on login with quick start tips
- **Help commands**: `quick-help`, `linux-tutorial`, `classroom-info`, `myip`, `helpme`
- **Shared folder**: `/shared` directory for class collaboration
- **Command history** and auto-complete in terminal
- **Visual feedback** when executing commands

**👨‍🏫 Teacher & Monitoring Features:**
- **Teacher Dashboard** (`/dashboard`) - Real-time monitoring of all active sessions
- **System resource tracking** (CPU, memory, Docker stats)
- **Session analytics** with IP addresses, duration, data transfer
- **Auto-refresh** for live updates (every 30 seconds)
- **JSON status API** (`/status`) for programmatic access

**🛡️ System & Security Improvements:**
- **Resource limits**: CPU (50% of core), Memory (512MB) per student
- **Network auto-creation** with graceful fallback
- **Enhanced logging** to `classroom.log` file
- **Robust error handling** and session cleanup
- **Isolated classroom network** (172.20.0.0/16)
- **Improved SSH configuration** for faster connections

### 🚀 Quick Start for Students
1. Visit `http://localhost:5000/` (or your server address)
2. Follow the welcome tutorial (or skip it)
3. Try `linux-tutorial` in the terminal
4. Explore lessons in the sidebar
5. Use help tabs when you need assistance

### 🔧 Installation & Upgrade
```bash
# Update existing installation
cd Linux-Classroom-in-a-Browser
pip install -r requirements.txt
python install.py
python app.py

# Or fresh installation
git clone https://github.com/nanofatdog/Linux-Classroom-in-a-Browser.git
cd Linux-Classroom-in-a-Browser
pip install -r requirements.txt
python install.py
python app.py
```

**Access Points:**
- **Premium UI**: `http://localhost:5000/` (English) or `/thai` (Thai)
- **Previous UIs**: `/improved` (improved) or `/classic` (original)
- **Teacher Dashboard**: `http://localhost:5000/dashboard`
- **Status API**: `http://localhost:5000/status`


## ✨ คุณสมบัติเด่น (Features)

* **🖥️ เทอร์มินัลเต็มรูปแบบ:** ใช้งาน Linux (Ubuntu 22.04) ได้จริงผ่านเทอร์มินัลบนหน้าเว็บ
* **🔒 สภาพแวดล้อมที่ปลอดภัย:** ผู้ใช้แต่ละคนจะได้ Container ส่วนตัวที่แยกขาดจากกัน
* **🐍 รองรับ Python:** ติดตั้ง Python 3 และ `pip` มาให้พร้อมใช้งาน สามารถติดตั้ง library เพิ่มเติมและรันสคริปต์ได้
* **🦀 รองรับ Rust:** ติดตั้ง Rust toolchain (rustc, cargo) มาให้พร้อมสำหรับเรียนรู้การพัฒนาโปรแกรมด้วย Rust
* **📚 บทเรียนในตัว:** มีพาเนลแสดงบทเรียนอยู่ข้างๆ เทอร์มินัล ทำให้ง่ายต่อการเรียนรู้ตาม
* **⚙️ ติดตั้งง่าย:** มีสคริปต์ `install.py` และ `uninstall.py` ช่วยให้การติดตั้งและลบทำได้ง่าย
* **💻 รองรับหลายระบบ:** สามารถติดตั้งและใช้งานได้ทั้งบน **Windows** และ **Linux**

## 🛠️ เทคโนโลยีที่ใช้ (Technology Stack)

* **Backend:** Python, Flask, Flask-Sock
* **Virtualization:** Docker
* **Frontend:** HTML, CSS, JavaScript
* **Terminal Emulation:** Xterm.js

## 🚀 การติดตั้งและใช้งาน (Installation and Usage)

ทำตามขั้นตอนเหล่านี้เพื่อเริ่มใช้งานโปรเจกต์บนเครื่องของคุณ

### **1. เตรียมความพร้อม (Prerequisites)**

คุณต้องติดตั้งโปรแกรมพื้นฐานต่อไปนี้ก่อน:

#### **สำหรับ Windows 10 / 11:**

1.  **Docker Desktop with WSL 2:**
    * ดาวน์โหลดและติดตั้ง **Docker Desktop** จาก [docker.com](https://www.docker.com/products/docker-desktop/)
    * **หมายเหตุ:** โปรแกรมติดตั้ง Docker อาจแจ้งให้คุณเปิดใช้งาน **WSL 2 (Windows Subsystem for Linux)** ซึ่งเป็นเทคโนโลยีที่จำเป็น กรุณาอนุญาตให้โปรแกรมดำเนินการตามขั้นตอนนั้น ซึ่งอาจมีการรีสตาร์ทเครื่อง
    * **สำคัญ:** หลังจากติดตั้งเสร็จสิ้น ต้องเปิดโปรแกรม Docker Desktop ขึ้นมา และรอจนไอคอนรูปวาฬที่ Taskbar นิ่งและขึ้นสถานะว่า "Running"

2.  **Python 3:**
    * **ทางเลือกที่ 1 (ใช้ Conda/Anaconda):** หากคุณใช้ Anaconda/Miniconda อยู่แล้ว คุณสามารถข้ามขั้นตอนนี้ไปได้เลย
    * **ทางเลือกที่ 2 (ใช้ Python ปกติ):**
        * **วิธีที่ 1 (แนะนำ):** ติดตั้งจาก **Microsoft Store** โดยค้นหา "Python 3.11" (หรือเวอร์ชันล่าสุด) แล้วกดติดตั้ง วิธีนี้จะตั้งค่า PATH ให้โดยอัตโนมัติ
        * **วิธีที่ 2:** ดาวน์โหลดและติดตั้งจาก [python.org](https://www.python.org/downloads/windows/)
            * **สำคัญ:** หากติดตั้งด้วยวิธีนี้ ในหน้าจอแรกของการติดตั้ง ให้ติ๊กช่อง **"Add Python to PATH"** ก่อนกด "Install Now"

#### **สำหรับ Linux (Ubuntu/Debian):**

1.  **Docker Engine:**
    ```bash
    sudo apt-get update
    sudo apt-get install docker.io -y
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER 
    # (ต้อง logout แล้ว login ใหม่เพื่อให้สิทธิ์ทำงาน)
    ```

2.  **Python 3 & Pip:**
    * **ทางเลือกที่ 1 (ใช้ Conda/Anaconda):** หากคุณใช้ Anaconda/Miniconda อยู่แล้ว คุณสามารถข้ามขั้นตอนนี้ไปได้เลย
    * **ทางเลือกที่ 2 (ใช้ Python ปกติ):**
    ```bash
    sudo apt-get install python3 python3-pip -y
    ```

### **2. ขั้นตอนการติดตั้งโปรเจกต์**

1.  **Clone a repository:**
    ```bash
    git clone https://github.com/nanofatdog/Linux-Classroom-pro.git
    cd inux-Classroom-pro
    ```

2.  **ตั้งค่า Environment และติดตั้ง Libraries:**
    * เลือกทำตามวิธีใดวิธีหนึ่งด้านล่างนี้

    #### **วิธี A: สำหรับผู้ใช้ Conda/Anaconda (แนะนำ)**
    * สร้าง environment ใหม่ชื่อ `linux-class` และติดตั้ง Python:
    ```bash
    conda create --name linux-class python=3.10 -y
    ```
    * เปิดใช้งาน environment:
    ```bash
    conda activate linux-class
    ```
    * ติดตั้ง libraries ที่จำเป็นด้วย pip ภายใน environment ของ conda:
    ```bash
    pip install -r requirements.txt
    ```

    #### **วิธี B: สำหรับผู้ใช้ Python ปกติ (pip)**
    * (แนะนำ) สร้างและเปิดใช้งาน Virtual Environment:
    ```bash
    # สำหรับ Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    
    # สำหรับ Windows
    python -m venv venv
    .\\venv\\Scripts\\activate
    ```
    * ติดตั้ง libraries ที่จำเป็น:
    ```bash
    pip install -r requirements.txt
    ```

3.  **รันสคริปต์ติดตั้ง:**
    * สคริปต์นี้จะทำการสร้าง Docker image ที่เป็นแม่แบบของห้องเรียนให้โดยอัตโนมัติ
    ```bash
    python install.py
    ```
    คุณจะเห็นขั้นตอนการดาวน์โหลดและติดตั้งโปรแกรมต่างๆ แสดงขึ้นมาบนหน้าจอ

### **3. เริ่มใช้งานเซิร์ฟเวอร์**

* **สำคัญ:** หากคุณใช้ Conda/venv อย่าลืม `conda activate linux-class` หรือ `source venv/bin/activate` ก่อนรันเซิร์ฟเวอร์ทุกครั้ง!

* **รันแบบปกติ (ที่ Port 5000):**
    ```bash
    python app.py
    ```

* **รันแบบกำหนดค่าเอง:**
    ```bash
    # เปลี่ยน Port เป็น 8080
    python app.py --port 8080
    
    # ใช้งานบน IP Address ที่กำหนด
    python app.py --host 127.0.0.1 --port 8080
    
    # (สำหรับขั้นสูง) เปิดใช้งาน HTTPS (ต้องมีไฟล์ cert.pem และ key.pem)
    python app.py --https
    ```

* **เข้าใช้งาน:**
    เปิดเว็บเบราว์เซอร์แล้วไปที่ `http://127.0.0.1:5000` (หรือ port ที่คุณกำหนด)

## 🗑️ การถอนการติดตั้ง (Uninstallation)

หากคุณต้องการลบ Docker image ที่โปรเจกต์นี้สร้างขึ้นเพื่อคืนพื้นที่ในเครื่อง ให้รันสคริปต์:
```bash
python uninstall.py
