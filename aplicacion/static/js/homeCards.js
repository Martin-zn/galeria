document.addEventListener('DOMContentLoaded', function() {
    var carouselElement = document.querySelector('#artistaCarousel')
    var carousel = new bootstrap.Carousel(carouselElement, {
        interval: false, // Desactiva la rotación automática
        wrap: false // Evita que el carrusel vuelva al principio al llegar al final
    })
})