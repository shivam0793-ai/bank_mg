document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const tableRows = document.querySelectorAll(".table-row");

    searchInput.addEventListener("keyup", function () {
        const value = this.value.toLowerCase();

        tableRows.forEach(row => {
            const sender = row.children[0].textContent.toLowerCase();
            const receiver = row.children[1].textContent.toLowerCase();

            if (sender.includes(value) || receiver.includes(value)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });

});