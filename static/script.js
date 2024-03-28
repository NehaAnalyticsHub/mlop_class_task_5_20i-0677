document.getElementById("userInfoForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    var formData = new FormData(document.getElementById("userInfoForm"));

    // Send data to backend
    fetch("/submit", {
        method: "POST",
        body: formData  // Send form data directly, no need to stringify or set content type
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
        document.getElementById("userInfoForm").reset();
    })
    .catch(error => console.error("Error:", error));
});
