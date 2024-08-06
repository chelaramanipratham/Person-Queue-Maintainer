function addElement() {
    const element = document.getElementById('element').value;
    fetch('/queue/insert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ element })
    })
    .then(response => response.json())
    .then(data => displayResult(data.message));
}

function deleteElement() {
    fetch('/queue/delete', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => displayResult(data.message));
}

function displayQueue() {
    fetch('/queue/display')
    .then(response => response.json())
    .then(data => {
        const queue = data.queue.join(', ');
        displayResult(`The queue is: ${queue}`);
    });
}

function searchPerson() {
    const person = document.getElementById('searchPerson').value;
    fetch('/queue/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ person })
    })
    .then(response => response.json())
    .then(data => displayResult(data.message));
}

function displayResult(message) {
    document.getElementById('result').innerText = message;
}