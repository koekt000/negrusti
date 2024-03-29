function onTakeQuizButtonClick() {
    const user_id = document.getElementById("user_id").value;

    const url = 'http://localhost:8000/draw';
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "user_id": user_id
        }),
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
    })
    .catch(error => console.error(error));
}

function onStartQuizButtonClick() {
    const url = 'http://localhost:8000/draw';
    fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
    })
    .catch(error => console.error(error));
}
