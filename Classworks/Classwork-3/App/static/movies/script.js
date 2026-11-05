
document.addEventListener("DOMContentLoaded", function () {

    const elements = document.querySelectorAll(
        ".movie-card, .person-card, .stat-card, .rating-row"
    );

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.1
        }
    );

    elements.forEach((element) => {
        observer.observe(element);
    });

});
