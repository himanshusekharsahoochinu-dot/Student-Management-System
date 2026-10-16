
document.addEventListener("DOMContentLoaded", function () {
    const deleteForms = document.querySelectorAll("[data-confirm]");

    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const message = form.dataset.confirm;

            if (!confirm(message)) {
                event.preventDefault();
            }
        });
    });
});
