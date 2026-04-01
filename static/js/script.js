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

document.addEventListener('DOMContentLoaded', () => {
    const toasts = document.querySelectorAll('.toast-box');
    
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(20px)';
            setTimeout(() => {
                toast.remove();
            }, 500); 
        }, 5000);
    });
});