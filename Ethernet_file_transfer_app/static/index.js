document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const fileList = document.getElementById('fileList');

    uploadForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const files = fileInput.files;
        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
            formData.append('file', files[i], files[i].webkitRelativePath || files[i].name);
        }

        fetch('/upload', {
            method: 'POST',
            body: formData
        }).then(response => response.text())
          .then(data => {
              alert(data);
              loadFileList();
          });
    });

    function loadFileList() {
        fetch('/uploads')
            .then(response => response.json())
            .then(files => {
                fileList.innerHTML = '';
                files.forEach(file => {
                    const li = document.createElement('li');
                    const link = document.createElement('a');
                    link.href = `/download/${file}`;
                    link.textContent = file;
                    li.appendChild(link);
                    fileList.appendChild(li);
                });
            });
    }

    loadFileList();
});
