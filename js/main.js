// Función principal que se ejecuta cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    // Obtener el botón de despliegue de mapa
    const mapButton = document.getElementById('show-map-button');
    // Agregar un event listener para el clic en el botón
    mapButton.addEventListener('click', showMap);
});

// Función para mostrar un mapa
function showMap() {
        // Definir el nivel de zoom deseado
    const zoomLevel = 11; // Puedes ajustar este valor según tus necesidades

    // Crear el mapa o agregar tu propio código para desplegar un mapa
    const mapContainer = document.getElementById('map-container');
    mapContainer.innerHTML = `<iframe src='https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d15777.194217423042!2d-83.926151!3d9.8599336!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2scr!4v1618781643343!5m2!1sen!2scr&z=${zoomLevel}' width='1000' height='500' style='border:0;' allowfullscreen='' loading='lazy'></iframe>`;
}