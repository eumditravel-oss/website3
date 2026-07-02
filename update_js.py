import os

js_path = 'f:/website3/js/redesign_motion.js'

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_js = """document.addEventListener('DOMContentLoaded', () => {
    // 0. Safe Fallback initialization for scroll animations
    // Add .js-hidden only to fade-up elements that are below the initial fold
    const fadeElements = document.querySelectorAll('.fade-up');
    fadeElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        // If element is below the fold, hide it for scroll animation
        if (rect.top > window.innerHeight - 100) {
            el.classList.add('js-hidden');
        }
    });

    // 1. Scroll Fade-up Observer
"""

if "// 0. Safe Fallback initialization" not in js_content:
    js_content = js_content.replace("document.addEventListener('DOMContentLoaded', () => {\n    // 1. Scroll Fade-up Observer", new_js)

    # Modify the fadeObserver logic to remove .js-hidden and add .visible
    old_observer_logic = """    const fadeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, observerOptions);"""

    new_observer_logic = """    const fadeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                entry.target.classList.remove('js-hidden');
            } else {
                // To keep reversing effect, add js-hidden back when scrolling up out of view
                entry.target.classList.remove('visible');
                // Only if it actually went below the viewport
                if (entry.boundingClientRect.top > 0) {
                    entry.target.classList.add('js-hidden');
                }
            }
        });
    }, observerOptions);"""
    
    js_content = js_content.replace(old_observer_logic, new_observer_logic)

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("JS updated successfully.")
else:
    print("JS already updated.")
