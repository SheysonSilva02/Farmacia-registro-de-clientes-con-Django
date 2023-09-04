(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Está seguro de eliminar el Cliente?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();