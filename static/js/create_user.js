const cards = document.querySelectorAll(".info-box");

cards.forEach((card) => {

    card.addEventListener("mousemove", (e) => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        card.style.background = `
        radial-gradient(
            circle at ${x}px ${y}px,
            rgba(255,255,255,1),
            rgba(239,246,255,1)
        )
        `;

    });

    card.addEventListener("mouseleave", () => {
        card.style.background = "#fff";
    });

});


const inputs = document.querySelectorAll("input");

inputs.forEach((input) => {

    input.addEventListener("focus", () => {
        input.parentElement.style.transform = "translateY(-2px)";
    });

    input.addEventListener("blur", () => {
        input.parentElement.style.transform = "translateY(0px)";
    });

});