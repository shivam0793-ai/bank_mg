const card = document.querySelector(".transfer-card");

window.addEventListener("load", () => {
    setTimeout(() => {
        card.classList.add("show");
    }, 150);
});

const button = document.querySelector(".transfer-btn");

button.addEventListener("click", () => {
    button.innerText = "Processing...";
    button.style.opacity = "0.8";
});