document.addEventListener('DOMContentLoaded', () => {
    // Lightbox ініціалізація з покращеними налаштуваннями
    const lightbox = GLightbox({
        selector: '.glightbox',
        touchNavigation: true,
        loop: true,
        zoomable: true // Дозволяє зум для великого перегляду
    });

    // Slider Logic для кнопок-стрілок
    const slider = document.getElementById('photo-slider');
    const btnLeft = document.getElementById('slide-left');
    const btnRight = document.getElementById('slide-right');

    if (slider && btnLeft && btnRight) {
        btnLeft.onclick = () => {
            slider.scrollBy({ left: -320, behavior: 'smooth' });
        };
        btnRight.onclick = () => {
            slider.scrollBy({ left: 320, behavior: 'smooth' });
        };
    }
});