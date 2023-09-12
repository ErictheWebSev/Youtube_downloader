
document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formElement = event.target;
    const formData = new FormData(formElement);

    document.getElementById('loader').style.display = 'block';

    fetch('/download/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loader').style.display = 'none';

        if (data.error) {
            document.getElementById('message').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('message').innerText = data.message;
            document.getElementById('message').innerText += `\nDownloaded file path: ${data.file_path}`;
        }

        document.getElementById('message').style.display = 'block';
    })
    .catch(error => {
        document.getElementById('loader').style.display = 'none';
        document.getElementById('message').innerText = 'An error occurred.';
        document.getElementById('message').style.display = 'block';
    });
});