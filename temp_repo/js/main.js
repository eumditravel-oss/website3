// main.js - Vanilla JS interactions for Sinyoung SCM Clone

document.addEventListener('DOMContentLoaded', () => {
    // Sticky Header
    const header = document.getElementById('hd');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('sticky');
        } else {
            header.classList.remove('sticky');
        }
    });

    // GNB Dropdown
    const gnb = document.getElementById('gnb');
    const hdBg = document.querySelector('.hd_bg');
    const gnb2dul = document.querySelectorAll('.gnb_2dul');
    
    if (gnb && hdBg) {
        gnb.addEventListener('mouseenter', () => {
            hdBg.style.display = 'block';
            gnb2dul.forEach(el => el.style.display = 'block');
        });
        
        gnb.addEventListener('mouseleave', () => {
            hdBg.style.display = 'none';
            gnb2dul.forEach(el => el.style.display = 'none');
        });
        
        hdBg.addEventListener('mouseenter', () => {
            hdBg.style.display = 'block';
            gnb2dul.forEach(el => el.style.display = 'block');
        });
        
        hdBg.addEventListener('mouseleave', () => {
            hdBg.style.display = 'none';
            gnb2dul.forEach(el => el.style.display = 'none');
        });
    }

    // Swiper Initialization
    if (typeof Swiper !== 'undefined' && document.querySelector('.mySwiper')) {
        const vsMenu = ['01', '02', '03', '04', '05'];
        const swiper = new Swiper('.mySwiper', {
            speed: 1000,
            effect: "fade",
            centeredSlides: true,
            allowTouchMove: false,
            loop: true,
            autoplay: {
                delay: 7000,
                disableOnInteraction: false,
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
                renderBullet: function(index, className) {
                    return '<span class="' + className +
                        '"><svg viewBox="0 0 60 60" class="circle-svg"><circle class="circle" cx="30" cy="30" r="29" ></circle></svg>' +
                        (vsMenu[index]) + '</span>';
                }
            },
        });
    }
});
