from flask import Flask, request, send_from_directory, render_template_string
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

html_template = '''
<h2>Upload File</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
<br>
<h2>Files</h2>
<ul>
{% for file in files %}
  <li><a href="/download/{{file}}">{{file}}</a></li>
{% endfor %}
</ul>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(html_template, files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    # Set host to your Ethernet IP (e.g., 192.168.1.102), port can be 3000 or any
    app.run(host='192.168.1.160', port=4000)
