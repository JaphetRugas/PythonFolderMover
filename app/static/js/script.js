function moveFolder() {
    const source = document.getElementById("sourceFolder").value;
    const destination = document.getElementById("destinationFolder").value;

    fetch('/move_folder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ source, destination })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}
 
