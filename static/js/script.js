document.addEventListener('DOMContentLoaded', () => {
    // Lightbox
    const lightbox = GLightbox({
        selector: '.glightbox',
        touchNavigation: true,
        loop: true,
        zoomable: true
    });

    // Slider Logic
    const slider = document.getElementById('photo-slider');
    const btnLeft = document.getElementById('slide-left');
    const btnRight = document.getElementById('slide-right');

    if (slider && btnLeft && btnRight) {
        const scrollAmount = 320; // card width + gap

        btnLeft.addEventListener('click', () => {
            slider.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        btnRight.addEventListener('click', () => {
            slider.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });
    }
});