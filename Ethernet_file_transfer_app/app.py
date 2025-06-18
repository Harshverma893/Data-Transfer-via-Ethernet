import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('index'))
    return render_template('index.html', files=get_files_with_size())

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='192.168.1.160', port=3000, debug=True)