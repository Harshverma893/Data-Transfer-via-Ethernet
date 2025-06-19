# 📁 Data Transfer via Ethernet

A **Flask-based web application** for efficient file and folder transfers over a local Ethernet network. Built for high-speed, low-latency communication, this project features drag-and-drop uploads, real-time transfer performance metrics, and support for large file handling with reliability.

---

## 🚀 Features

- **🔼 Drag-and-Drop Uploads**: Simple and modern interface for easy file and folder selection.
- **📊 Real-Time Metrics**: Displays upload/download speed and estimated transfer time.
- **📂 Large File Support**: Handles large files using a custom protocol for reliability.
- **📡 Optimized for LAN**: Designed specifically for fast, stable Ethernet-based networks.

---

## 🧰 Technologies Used

- **Backend**: Flask, Python  
- **Frontend**: HTML, CSS, JavaScript  
- **Libraries**: `os`, `shutil`, `time` (standard Python libraries)

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8 or higher  
- Git  
- Two laptops connected via the same Ethernet network  
- Admin access to set IP addresses

---

## 🛠️ Step-by-Step Setup

### 1. 🔌 Configure Ethernet IP (Host System)

#### On **Windows**:
- Go to: Control Panel → Network and Sharing Center → Change Adapter Settings
- Right-click **Ethernet** → Properties → Select **IPv4** → Properties
- Set:
  - IP address: `192.168.1.100`
  - Subnet mask: `255.255.255.0`
- Confirm using: `ipconfig`

#### On **Linux**:
```bash
sudo nmcli con mod "Wired connection 1" ipv4.addresses 192.168.1.100/24 ipv4.method manual
```
> Use `ip addr` or `nmcli` to confirm your IP.

Make sure the second laptop is on the same subnet (e.g., `192.168.1.101`).

---

### 2. 📥 Clone the Repository

```bash
git clone https://github.com/Harshverma893/Data-Transfer-via-Ethernet.git
cd Data-Transfer-via-Ethernet
```

### 3. 🧪 Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 4. 📦 Install Dependencies

```bash
pip install flask
```

### 5. ▶️ Run the Application

```bash
python app.py --host 192.168.1.100 --port 5002
```

> Replace the host IP with your actual IP. Make sure port `5002` is allowed through the firewall.

---

## 🌐 Usage Instructions

### 🖥 Access the Web App

- On both laptops: open `http://192.168.1.100:5002` in a browser

### 📁 Upload Files

- Drag and drop files/folders or use the file selector
- View progress bar and speed in real time

### 📤 Download Files

- See all uploaded files in the list
- Click download links to retrieve them

### 📊 Monitor Metrics

- Real-time upload/download speeds shown in MB/s
- Custom protocol ensures reliability on large files

---

## 🧪 Troubleshooting

### ❌ Can’t Access the Web App?
- Ensure both devices are on same subnet
- Confirm firewall allows port 5002
- Use `ipconfig` or `ip addr` to check IPs

### ❗ Port Already in Use?
```bash
python app.py --port 5003
```

---

## 🖼 Screenshots & Demo

Coming soon: UI screenshots and drag-and-drop demo video.

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new feature branch  
3. Submit a pull request following **PEP 8** guidelines

---

## 📄 License

MIT License

Copyright (c) 2025 Harsh Verma

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

---

## 📬 Contact

- GitHub: [@Harshverma893](https://github.com/Harshverma893)
