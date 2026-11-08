
document.addEventListener('DOMContentLoaded', () => {
    const loader = document.getElementById('pageLoader');

    // Hide loading screen after page loads
    window.addEventListener('load', () => {
        loader?.classList.add('hidden');
    });

    // Fallback in case the load event has already fired
    setTimeout(() => {
        loader?.classList.add('hidden');
    }, 1200);

    // Smooth navigation transitions
    document.querySelectorAll('a[href]').forEach(link => {
        link.addEventListener('click', event => {
            const url = new URL(link.href, window.location.href);

            if (
                url.origin === window.location.origin &&
                !link.target &&
                !event.ctrlKey &&
                !event.metaKey &&
                !event.shiftKey &&
                !event.altKey &&
                url.pathname !== window.location.pathname &&
                !url.hash
            ) {
                event.preventDefault();

                loader?.classList.remove('hidden');

                setTimeout(() => {
                    window.location.href = url.href;
                }, 180);
            }
        });
    });

    // Animate cards one by one
    const cards = document.querySelectorAll(
        '.movie-card, .person-card, .stat-card, .content-card'
    );

    cards.forEach((card, index) => {
        card.style.animation = `pageEnter .5s ease ${index * 0.07}s both`;
    });

    // Animated statistics
    const counters = document.querySelectorAll('[data-count]');

    const animateCounter = element => {
        const target = Number(element.dataset.count);
        const duration = 900;
        const start = performance.now();

        function update(now) {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);

            element.textContent = Math.round(target * eased);

            if (progress < 1) {
                requestAnimationFrame(update);
            }
        }

        requestAnimationFrame(update);
    };

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        });

        counters.forEach(counter => observer.observe(counter));
    } else {
        counters.forEach(animateCounter);
    }
});
