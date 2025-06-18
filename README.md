Data Transfer via Ethernet
A Flask-based web application for efficient file and folder transfers over local Ethernet networks. Featuring a user-friendly interface with drag-and-drop functionality, real-time performance metrics, and a custom file transfer protocol, this project supports reliable transfers of large files up to 10GB with minimal latency.
Features

Drag-and-Drop Uploads: Intuitive file and folder uploads via a modern web interface.
Performance Metrics: Displays real-time download/upload speed and transfer time.
Large File Support: Handles files and folders up to 10GB with a custom protocol for reliability.
Responsive Design: Built with Tailwind CSS for a clean, mobile-friendly UI.
Local Network Optimization: Designed for high-speed, low-latency transfers over Ethernet.

Technologies

Backend: Flask, Python
Frontend: HTML, JavaScript, Tailwind CSS
Libraries: os, shutil, time (Python standard libraries)
Network: Runs on local networks (e.g., 192.168.1.100:5002)

Setup Instructions
Prerequisites

Python 3.8 or higher
Git
Two laptops connected to the same Ethernet network (via switch/router)
Administrative access to configure network settings

Step-by-Step Setup

Check or Configure Ethernet IPv4 Address:

On the host laptop (where the app will run):
Windows:
Open Control Panel > Network and Internet > Network and Sharing Center.
Click Change adapter settings, right-click Ethernet, and select Properties.
Select Internet Protocol Version 4 (TCP/IPv4) and click Properties.
Ensure Obtain an IP address automatically is selected, or manually set an IP (e.g., 192.168.1.100, Subnet mask: 255.255.255.0).
Run ipconfig in Command Prompt to confirm the IP (look for Ethernet adapter’s IPv4 address, e.g., 192.168.1.100).


Linux:
Open Settings > Network or use nmcli.
Check Ethernet connection and note the IPv4 address (e.g., ip addr show eth0).
If needed, set a static IP: sudo nmcli con mod "Wired connection 1" ipv4.addresses 192.168.1.100/24 ipv4.method manual.




Ensure the second laptop is on the same network (e.g., IP 192.168.1.101).


Clone the Repository:
git clone https://github.com/Harshverma893/Data-Transfer-via-Ethernet.git
cd Data-Transfer-via-Ethernet


Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install flask


Run the Application:

Replace 192.168.1.100 with your host laptop’s Ethernet IPv4 address.

python app.py --host 192.168.1.100 --port 5002


Note: Ensure port 5002 is open (check firewall settings).



Usage

Connect Both Laptops to the Same Ethernet Network:

Physically connect both laptops to the same Ethernet switch or router.
Verify connectivity by pinging the host from the second laptop:ping 192.168.1.100




Access the Web App:

On the host laptop, open a browser and navigate to http://192.168.1.100:5002.
On the second laptop (same network), open a browser and visit the same URL: http://192.168.1.100:5002.
Ensure firewalls allow traffic on port 5002.


Upload Files:

Use the drag-and-drop area or click to select files/folders for upload.
Monitor upload progress and real-time metrics (speed, time) on the UI.


Download Files:

View uploaded files in the app’s file list.
Click download links to retrieve files, with speed metrics displayed.


Monitor Performance:

Both laptops can upload/download simultaneously, with real-time speed metrics (e.g., MB/s) shown.
The custom protocol ensures reliable transfers for files up to 10GB.



Troubleshooting

Cannot Access URL:
Verify both laptops are on the same Ethernet network (same subnet, e.g., 192.168.1.x).
Check firewall settings: Allow Flask (python) and port 5002.
Confirm the correct IP/port (run ipconfig or ip addr on the host).


Slow Transfers:
Ensure Ethernet cables are Cat5e/Cat6 for high-speed transfers.
Check network congestion or switch/router performance.


Port Conflict:
If 5002 is in use, change the port in app.py or the run command (e.g., --port 5003).



Screenshots
Coming soon: UI screenshot and drag-and-drop demo video.
Contributing
Contributions are welcome! Fork the repository, create a branch, and submit a pull request with your changes. Follow PEP 8 guidelines.
License
MIT License
Contact

GitHub: Harshverma893
LinkedIn: Harsh Verma

