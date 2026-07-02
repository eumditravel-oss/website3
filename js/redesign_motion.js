document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll Fade-up Observer
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -100px 0px',
        threshold: 0.15
    };

    const fadeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-up');
    fadeElements.forEach(el => fadeObserver.observe(el));

    // 2. Number Count-up Observer
    const countElements = document.querySelectorAll('.count-up');
    
    const countObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const targetNumber = parseInt(target.getAttribute('data-target'), 10);
                const duration = 2000; // 2 seconds
                let startTimestamp = null;
                
                const step = (timestamp) => {
                    if (!startTimestamp) startTimestamp = timestamp;
                    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                    // easeOutQuart
                    const easeProgress = 1 - Math.pow(1 - progress, 4);
                    
                    target.innerText = Math.floor(easeProgress * targetNumber).toLocaleString();
                    
                    if (progress < 1) {
                        window.requestAnimationFrame(step);
                    } else {
                        target.innerText = targetNumber.toLocaleString();
                    }
                };
                
                window.requestAnimationFrame(step);
            } else {
                // Reset when scrolling out of view
                entry.target.innerText = "0";
            }
        });
    }, observerOptions);

    countElements.forEach(el => countObserver.observe(el));

    // 3. Header Scroll Effect
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    // 4. Mobile Menu Toggle
    const btnMenuOpen = document.getElementById('btn-menu-open');
    const btnMenuClose = document.getElementById('btn-menu-close');
    const mobileNav = document.getElementById('mobile-nav');
    const mOverlay = document.getElementById('m-overlay');

    if (btnMenuOpen && btnMenuClose && mobileNav && mOverlay) {
        const openMenu = () => {
            mobileNav.classList.add('open');
            mOverlay.classList.add('open');
            document.body.style.overflow = 'hidden';
        };

        const closeMenu = () => {
            mobileNav.classList.remove('open');
            mOverlay.classList.remove('open');
            document.body.style.overflow = '';
        };

        btnMenuOpen.addEventListener('click', openMenu);
        btnMenuClose.addEventListener('click', closeMenu);
        mOverlay.addEventListener('click', closeMenu);
    }

    // 5. Megamenu Hover Logic
    const headerEl = document.getElementById('header');
    const gnbItems = document.querySelectorAll('.gnb > li');
    const megaPanel = document.querySelector('.mega-menu-panel');
    const megaCols = document.querySelectorAll('.mega-col');
    const megaOverlay = document.querySelector('.mega-overlay');
    let megaTimeout;

    if (headerEl && megaPanel) {
        const openMegaMenu = () => {
            clearTimeout(megaTimeout);
            megaPanel.classList.add('open');
            if(megaOverlay) megaOverlay.classList.add('open');
            headerEl.classList.add('megamenu-active');
        };

        const closeMegaMenu = () => {
            megaTimeout = setTimeout(() => {
                megaPanel.classList.remove('open');
                if(megaOverlay) megaOverlay.classList.remove('open');
                headerEl.classList.remove('megamenu-active');
                megaCols.forEach(col => col.classList.remove('highlight'));
            }, 150);
        };

        gnbItems.forEach(item => {
            item.addEventListener('mouseenter', () => {
                openMegaMenu();
                // Highlight corresponding column
                const targetId = item.getAttribute('data-target');
                megaCols.forEach(col => {
                    if (col.id === targetId) {
                        col.classList.add('highlight');
                    } else {
                        col.classList.remove('highlight');
                    }
                });
            });
            item.addEventListener('mouseleave', closeMegaMenu);
        });

        megaPanel.addEventListener('mouseenter', () => {
            clearTimeout(megaTimeout);
        });
        megaPanel.addEventListener('mouseleave', closeMegaMenu);
    }

    // 6. Mobile Accordion Menu
    const btnMenuOps = document.querySelectorAll('.btn_menu_op, .subOpen');
    btnMenuOps.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const parentLi = btn.closest('li');
            const subMenu = parentLi.querySelector('.gnb_2dul_mo');
            if (subMenu) {
                const isVisible = subMenu.style.display === 'block';
                // Close all others
                document.querySelectorAll('.gnb_2dul_mo').forEach(ul => {
                    ul.style.display = 'none';
                });
                if (!isVisible) {
                    subMenu.style.display = 'block';
                }
            }
        });
    });
});
