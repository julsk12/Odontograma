// Obtén el modal y el botón de cerrar
var modal = document.querySelector('.modal1');
var closeBtn = document.querySelector('.close1');

// Añade un evento click al botón de cerrar para cerrar el modal
closeBtn.addEventListener('click', function() {
    modal.style.display = 'none';
});

// Añade un evento click a cualquier parte del modal para cerrarlo también
modal.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Función para abrir el modal
function openModal() {
    modal.style.display = 'block';
}
