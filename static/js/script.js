document.addEventListener('DOMContentLoaded', () => {
    // 1. Слайдер для фотосесій (Upcoming Photoshoots)
    const track = document.getElementById('sessionsTrack');
    const btnPrev = document.getElementById('slidePrev');
    const btnNext = document.getElementById('slideNext');

    if (track && btnPrev && btnNext) {
        const scrollAmount = 450; // На скільки пікселів прокручувати

        btnNext.addEventListener('click', () => {
            track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        btnPrev.addEventListener('click', () => {
            track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        // Перевірка, щоб приховати стрілки, якщо скролити нікуди (опціонально)
        track.addEventListener('scroll', () => {
            const maxScroll = track.scrollWidth - track.clientWidth;
            btnPrev.style.opacity = track.scrollLeft <= 0 ? "0.3" : "1";
            btnNext.style.opacity = track.scrollLeft >= maxScroll ? "0.3" : "1";
        });
    }

    // 2. Автоматичне зникнення Тостів
    const toasts = document.querySelectorAll('.toast-box');
    toasts.forEach(toast => {
        // Видалення через кнопку X
        const closeBtn = toast.querySelector('.toast-close');
        if (closeBtn) {
            closeBtn.onclick = () => toast.style.opacity = '0';
        }

        // Автоматичне видалення через 5 секунд
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(-10px)';
            setTimeout(() => toast.remove(), 500);
        }, 5000);
    });

    // 3. Ініціалізація GLightbox (якщо є на сторінці)
    if (typeof GLightbox !== 'undefined') {
        GLightbox({ selector: '.glightbox' });
    }
});

function scrollSessions(direction) {
    const scroller = document.getElementById('sessionsScroller');
    const scrollAmount = 470; // Ширина картки + gap
    scroller.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}

// Product

document.querySelectorAll('input[type="file"]').forEach(input => {
    input.addEventListener('change', function () {
        const span = this.parentElement.querySelector('span');
        if (this.files.length > 0) {
            span.innerHTML = `<i class="fa-solid fa-check"></i> ${this.files[0].name}`;
        }
    });
});