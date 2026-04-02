document.addEventListener('DOMContentLoaded', () => {

    // --- 1. PHOTOSHOOT SCROLLER (Upcoming Sessions) ---
    const track = document.getElementById('sessionsTrack'); 
    const btnPrev = document.getElementById('slidePrev');
    const btnNext = document.getElementById('slideNext');

    if (track && btnPrev && btnNext) {
        const scrollAmount = 450; 

        btnNext.addEventListener('click', () => {
            track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        btnPrev.addEventListener('click', () => {
            track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        track.addEventListener('scroll', () => {
            const maxScroll = track.scrollWidth - track.clientWidth;
            // Додаємо невеликий запас (1px) для точності рендерингу
            btnPrev.style.opacity = track.scrollLeft <= 1 ? "0.3" : "1";
            btnNext.style.opacity = track.scrollLeft >= maxScroll - 1 ? "0.3" : "1";
        });
    }

    // --- 2. CUSTOM DELETION MODAL (For Cart & Dashboard CRUD) ---
    const modal = document.getElementById('confirmModal');
    const modalConfirm = document.getElementById('modalConfirm');
    const modalCancel = document.getElementById('modalCancel');
    const modalMessage = document.getElementById('modalMessage');
    
    let activeTrigger = null;

    // Використовуємо делегування подій для всіх кнопок видалення
    document.addEventListener('click', (e) => {
        const trigger = e.target.closest('.confirm-delete');
        if (!trigger) return;

        e.preventDefault(); // Зупиняємо миттєве видалення
        activeTrigger = trigger;

        // Отримуємо кастомне повідомлення з атрибута data-message
        const message = trigger.getAttribute('data-message') || "Are you sure you want to delete this item?";
        if (modalMessage) modalMessage.textContent = message;

        // Показуємо модальне вікно
        if (modal) modal.style.display = 'flex';
    });

    if (modalCancel) {
        modalCancel.onclick = () => {
            modal.style.display = 'none';
            activeTrigger = null;
        };
    }

    if (modalConfirm) {
        modalConfirm.onclick = () => {
            if (activeTrigger) {
                // ЛОГІКА CRUD: 
                // 1. Якщо кнопка всередині форми (для POST видалення в Dashboard)
                const form = activeTrigger.closest('form');
                if (form) {
                    form.submit();
                } else {
                    // 2. Якщо це просто посилання (для видалення з Cart)
                    const targetUrl = activeTrigger.getAttribute('href');
                    if (targetUrl) window.location.href = targetUrl;
                }
            }
            modal.style.display = 'none';
        };
    }

    // Закриття модалки при кліку поза карткою
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
            activeTrigger = null;
        }
    });

    // --- 3. TOAST NOTIFICATIONS (Auto-hide & Manual close) ---
    const toasts = document.querySelectorAll('.toast-box');

    toasts.forEach(toast => {
        // Автоматичне зникнення через 5 секунд
        setTimeout(() => {
            if (toast && toast.parentNode) {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(20px)';
                setTimeout(() => toast.remove(), 500);
            }
        }, 5000);

        // Ручне закриття по кнопці X
        const closeBtn = toast.querySelector('.toast-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                toast.remove();
            });
        }
    });

    // --- 4. GLIGHTBOX (Single Initialization) ---
    if (typeof GLightbox !== 'undefined') {
        GLightbox({ 
            selector: '.glightbox',
            touchNavigation: true,
            loop: true,
            zoomable: true
        });
    }

    // --- 5. FILE INPUT STYLING (Custom Upload Buttons) ---
    document.querySelectorAll('input[type="file"]').forEach(input => {
        input.addEventListener('change', function () {
            const uploadText = this.parentElement.querySelector('#file-upload-text') || 
                               this.parentElement.querySelector('#preview-text') ||
                               this.parentElement.querySelector('#file-text') ||
                               this.parentElement.querySelector('span');
            
            if (uploadText && this.files.length > 0) {
                const fileName = this.files[0].name;
                uploadText.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${fileName}`;
            }
        });
    });
});