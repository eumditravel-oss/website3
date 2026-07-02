import os

new_js = """
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
"""

with open('f:/website3/js/redesign_motion.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Insert before the last });
insert_pos = js_content.rfind('});')
if insert_pos != -1:
    js_content = js_content[:insert_pos] + new_js + js_content[insert_pos:]

with open('f:/website3/js/redesign_motion.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
