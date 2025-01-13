window.addEventListener("DOMContentLoaded", (event) => {
    let contentres = document.getElementById("rest");
    let showres = document.getElementById("res");
    let contentcul = document.getElementById("culture");
    let showcul = document.getElementById("cul");
    let contentabout = document.getElementById("about");
    let showabout = document.getElementById("abo");

    showres?.addEventListener("click", () => {
        contentres.style.display = "block";
        contentcul.style.display = "none";
        contentabout.style.display = "none";
    })

    showcul?.addEventListener("click", () => {
        contentcul.style.display = "block";
        contentres.style.display = "none";
        contentabout.style.display = "none";
    })
    showabout?.addEventListener("click", () => {
        contentabout.style.display = "block";
        contentres.style.display = "none";
        contentcul.style.display = "none";
    })
})