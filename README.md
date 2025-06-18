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



Network: Runs on local networks (e.g., 192.168.1.160:3000)

Setup Instructions

Prerequisites





Python 3.8+



Git



A local network environment

Installation





Clone the repository:

git clone https://github.com/Harshverma893/Data-Transfer-via-Ethernet.git
cd Data-Transfer-via-Ethernet



Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install dependencies:

pip install flask



Run the application:

python app.py



Access the app in your browser at http://192.168.1.160:3000 (adjust IP/port as needed).

Usage





Open the web app in a browser on the same local network.



Drag and drop files or folders into the upload area or click to browse.



Monitor upload progress and view real-time metrics (speed, time).



Download files via provided links, with performance metrics displayed.

Screenshots

Coming soon: UI screenshot and drag-and-drop demo video.

Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request with your changes. Ensure code follows PEP 8 guidelines.

License

MIT License
