function saveData() {
    let casino_url = document.getElementById("casino_url").value;
    let username = document.getElementById("username").value;
    localStorage.setItem("casino_url", casino_url);
    localStorage.setItem("username", username);
    alert("Saved successfully!");
}

function startPrediction() {
    let casino_url = localStorage.getItem("casino_url");
    let username = localStorage.getItem("username");

    if (!casino_url || !username) {
        alert("Please enter and save details first.");
        return;
    }

    fetch(`http://127.0.0.1:5000/predict?url=${casino_url}&username=${username}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = JSON.stringify(data);
        })
        .catch(error => {
            document.getElementById("result").innerText = "Error fetching prediction.";
        });
}
