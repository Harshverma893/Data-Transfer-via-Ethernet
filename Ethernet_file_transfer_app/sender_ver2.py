import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_files_with_size():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        files.append((filename, size_mb))
    return files

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>File Transfer App</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .file-entry { margin-bottom: 10px; }
        .progress { width: 100%; background-color: #eee; height: 20px; border-radius: 5px; overflow: hidden; margin-top: 10px; display: none; }
        .progress-bar { height: 100%; background-color: #4caf50; width: 0%; text-align: center; color: white; }
        .loader { margin: 5px 0; color: #444; }
        #drop-area { border: 2px dashed #ccc; padding: 20px; margin-bottom: 10px; text-align: center; }
    </style>
</head>
<body>
    <h2>Upload File</h2>
    <div id="drop-area">
        <p>Drag & Drop files here or click to upload</p>
        <form id="uploadForm" method=post enctype=multipart/form-data>
            <input type=file name=file id="fileInput" required>
            <input type=submit value=Upload>
        </form>
    </div>

    <div class="progress" id="uploadProgressContainer">
        <div class="progress-bar" id="uploadProgressBar">0%</div>
    </div>
    <p id="uploadTimer"></p>
    <p id="uploadSummary"></p>
    <hr>

    <h2>Uploaded Files</h2>
    <ul>
    {% for file, size in files %}
        <li class="file-entry">
            {{ file }} ({{ '%.2f'|format(size) }} MB)
            <button onclick="downloadFile('{{file}}')">Download</button> |
            <a href="/delete/{{file}}" onclick="return confirm('Delete this file?');">Delete</a>
            <div class="loader" id="loader-{{file}}"></div>
            <div class="progress" id="progress-{{file}}">
                <div class="progress-bar" id="bar-{{file}}">0%</div>
            </div>
            <p id="summary-{{file}}"></p>
        </li>
    {% endfor %}
    </ul>

<script>
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const uploadProgressBar = document.getElementById('uploadProgressBar');
    const uploadProgressContainer = document.getElementById('uploadProgressContainer');
    const uploadTimer = document.getElementById('uploadTimer');
    const uploadSummary = document.getElementById('uploadSummary');

    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(uploadForm);
        const xhr = new XMLHttpRequest();

        uploadProgressContainer.style.display = 'block';
        let startTime = Date.now();

        xhr.upload.addEventListener('progress', function(e) {
            if (e.lengthComputable) {
                const percent = Math.round((e.loaded / e.total) * 100);
                uploadProgressBar.style.width = percent + '%';
                uploadProgressBar.textContent = percent + '%';

                const elapsed = (Date.now() - startTime) / 1000;
                const uploadedMB = (e.loaded / (1024 * 1024)).toFixed(2);
                const speedMBps = (e.loaded / 1024 / 1024 / elapsed).toFixed(2);
                uploadTimer.textContent = `Uploaded ${uploadedMB} MB at ${speedMBps} MBps in ${elapsed.toFixed(1)}s`;
            }
        });

        xhr.onload = function() {
            if (xhr.status === 200) {
                const totalTime = (Date.now() - startTime) / 1000;
                const totalMB = (fileInput.files[0].size / 1024 / 1024).toFixed(2);
                const avgSpeed = (totalMB / totalTime).toFixed(2);
                uploadSummary.textContent = `Upload complete. Avg Speed: ${avgSpeed} MBps`;
                location.reload();
            }
        };

        xhr.open('POST', '/');
        xhr.send(formData);
    });

    async function downloadFile(filename) {
        const url = `/download/${filename}`;
        const loader = document.getElementById('loader-' + filename);
        const progressDiv = document.getElementById('progress-' + filename);
        const bar = document.getElementById('bar-' + filename);
        const summary = document.getElementById('summary-' + filename);

        loader.textContent = 'Starting download...';
        progressDiv.style.display = 'block';

        const response = await fetch(url);
        const reader = response.body.getReader();
        const contentLength = +response.headers.get('Content-Length');

        let received = 0;
        let chunks = [];
        const startTime = Date.now();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            chunks.push(value);
            received += value.length;

            const percent = Math.round((received / contentLength) * 100);
            bar.style.width = percent + '%';
            bar.textContent = percent + '%';

            const elapsed = (Date.now() - startTime) / 1000;
            const receivedMB = (received / 1024 / 1024).toFixed(2);
            const totalMB = (contentLength / 1024 / 1024).toFixed(2);
            const speedMBps = (received / 1024 / 1024 / elapsed).toFixed(2);
            const eta = ((contentLength - received) / 1024 / 1024 / speedMBps).toFixed(1);

            loader.textContent = `Downloaded ${receivedMB} MB of ${totalMB} MB (${speedMBps} MBps, ETA: ${eta}s)`;
        }

        const totalTime = (Date.now() - startTime) / 1000;
        const avgSpeed = (contentLength / 1024 / 1024 / totalTime).toFixed(2);
        summary.textContent = `Download complete. Avg Speed: ${avgSpeed} MBps`;

        const blob = new Blob(chunks);
        const downloadUrl = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(downloadUrl);

        loader.textContent = 'Download complete!';
        setTimeout(() => {
            loader.textContent = '';
            progressDiv.style.display = 'none';
        }, 3000);
    }

    const dropArea = document.getElementById('drop-area');
    dropArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropArea.style.borderColor = '#000';
    });

    dropArea.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropArea.style.borderColor = '#ccc';
    });

    dropArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dropArea.style.borderColor = '#ccc';
        fileInput.files = e.dataTransfer.files;
    });
</script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('index'))
    return render_template_string(html_template, files=get_files_with_size())

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='192.168.1.160', port=3000, debug=True)
