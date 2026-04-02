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

document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('file-upload');
    const uploadText = document.getElementById('file-upload-text');

    if (fileInput && uploadText) {
        fileInput.addEventListener('change', function () {
            if (this.files && this.files.length > 0) {
                // Показуємо назву файлу та міняємо іконку на "чек"
                const fileName = this.files[0].name;
                uploadText.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${fileName}`;
            } else {
                uploadText.innerHTML = `<i class="fa-solid fa-cloud-arrow-up"></i> Choose Session Image`;
            }
        });
    }
});

function scrollSessions(direction) {
    const scroller = document.getElementById('sessionsScroller');
    const scrollAmount = 470; // Ширина картки + gap
    scroller.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}