const cards = document.querySelectorAll(".service-card");

function showCards() {
    cards.forEach(card => {
        const top = card.getBoundingClientRect().top;
        if (top < window.innerHeight - 80) {
            card.classList.add("show");
        }
    });
}

window.addEventListener("scroll", showCards);
window.addEventListener("load", showCards);

/* click animation */
cards.forEach(card => {
    card.addEventListener("click", () => {
        card.style.transform = "scale(0.97)";
        setTimeout(() => {
            card.style.transform = "";
        }, 150);
    });
});