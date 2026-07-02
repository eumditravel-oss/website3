document.addEventListener('DOMContentLoaded', () => {
    // Check for reduced motion preference
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (prefersReducedMotion) {
        return; // Exit if user prefers reduced motion
    }

    // Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    const motionObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Unobserve after animating once
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Apply observer to all elements with motion-fade-up class
    const motionElements = document.querySelectorAll('.motion-fade-up');
    motionElements.forEach(el => {
        motionObserver.observe(el);
    });
    
    // Smooth scroll for top button
    const topBtn = document.getElementById('top_btn');
    if(topBtn) {
        // Replace existing click handler to ensure smooth scroll
        $(topBtn).off('click').on('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});
