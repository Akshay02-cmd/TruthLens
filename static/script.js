document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById("news");
    const checkButton = document.querySelector("button[type='submit']");

    // Disable button if textarea is empty
    textarea.addEventListener("input", function () {
        if (textarea.value.trim().length === 0) {
            checkButton.disabled = true;
        } else {
            checkButton.disabled = false;
        }
    });

    // Trigger animation on prediction display
    const alertBox = document.querySelector(".alert-info");
    if (alertBox) {
        alertBox.classList.add("fade-in");
    }
});
