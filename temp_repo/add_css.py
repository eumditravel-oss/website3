import os

new_css = """
/* ==========================================================
   Megamenu Styles
========================================================== */
.gnb > li > a { position: relative; padding: 0 10px; }
.gnb > li > a.active { color: var(--color-point); }

.mega-menu-panel {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: #fff;
    border-top: 1px solid var(--color-border);
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s var(--easing);
    z-index: 999;
}

.mega-menu-panel.open {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.mega-container {
    display: flex;
    justify-content: space-between;
    padding: 40px 24px 60px;
}

.mega-cols {
    display: flex;
    gap: 40px;
    flex: 1;
}

.mega-col {
    flex: 1;
    min-width: 140px;
}
.mega-col.highlight .mega-title a { color: var(--color-point); }

.mega-title {
    font-size: 20px;
    margin-bottom: 24px;
    border-bottom: 2px solid var(--color-text-main);
    padding-bottom: 12px;
}
.mega-col.highlight .mega-title { border-bottom-color: var(--color-point); }

.mega-list { list-style: none; padding: 0; margin: 0; }
.mega-list li { margin-bottom: 12px; }
.mega-list a {
    display: inline-block;
    font-size: 16px;
    color: var(--color-text-muted);
    transition: color 0.2s;
}
.mega-list a:hover {
    color: var(--color-point);
    font-weight: 600;
}

.mega-cta {
    width: 300px;
    background: var(--color-bg-light);
    padding: 30px;
    border-radius: var(--radius-md);
    text-align: center;
    border: 1px solid var(--color-border);
    margin-left: 40px;
}
.mega-cta p { font-size: 16px; margin-top: 0; margin-bottom: 20px; font-weight: 600; }
.mega-cta .btn { width: 100%; margin-bottom: 16px; font-size: 16px; padding: 12px; min-height: auto; }
.mega-phone { font-size: 24px; font-weight: 800; color: var(--color-text-main); }

.mega-overlay {
    position: fixed;
    top: 80px; left: 0; width: 100%; height: 100vh;
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(2px);
    z-index: 998;
    opacity: 0; visibility: hidden;
    transition: all 0.3s var(--easing);
}
.mega-overlay.open { opacity: 1; visibility: visible; }
#header.scrolled + .mega-overlay { top: 70px; }

/* ==========================================================
   Subpage Template Styles
========================================================== */
.sub-hero {
    position: relative;
    height: 350px;
    background: var(--color-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #fff;
    margin-top: 80px; /* Header height */
}
.sub-hero-bg {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: url('../img/main01.jpg') center/cover;
    opacity: 0.3;
}
.sub-hero::after {
    content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(135deg, rgba(15,32,39,0.9) 0%, rgba(37,99,235,0.7) 100%);
}
.sub-hero-content {
    position: relative; z-index: 2;
}
.sub-hero-title {
    font-size: 48px !important;
    font-weight: 800;
    color: #fff !important;
    margin-bottom: 12px;
}
.sub-hero-desc {
    font-size: 20px;
    color: rgba(255,255,255,0.8);
    margin: 0;
}

/* Breadcrumb */
.breadcrumb {
    background: #fff;
    border-bottom: 1px solid var(--color-border);
    padding: 20px 0;
    font-size: 15px;
}
.breadcrumb .container {
    display: flex;
    gap: 12px;
    align-items: center;
    color: var(--color-text-muted);
}
.breadcrumb span.current { color: var(--color-text-main); font-weight: 600; }
.breadcrumb i { font-size: 12px; margin: 0 4px; }

/* Sub Layout */
.sub-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 60px;
    padding: 80px 24px;
    align-items: start;
}

/* Sidebar */
.sub-sidebar {
    position: sticky;
    top: 120px;
    background: #fff;
    border-radius: var(--radius-md);
    border: 1px solid var(--color-border);
    overflow: hidden;
}
.sidebar-title {
    background: var(--color-primary);
    color: #fff !important;
    margin: 0;
    padding: 24px;
    font-size: 22px;
    text-align: center;
}
.sidebar-menu { list-style: none; padding: 0; margin: 0; }
.sidebar-menu li { border-bottom: 1px solid var(--color-border); }
.sidebar-menu li:last-child { border-bottom: none; }
.sidebar-menu a {
    display: block;
    padding: 18px 24px;
    font-size: 17px;
    color: var(--color-text-muted);
    transition: all 0.2s;
    font-weight: 500;
}
.sidebar-menu a:hover {
    background: var(--color-bg-light);
    color: var(--color-text-main);
}
.sidebar-menu li.active a {
    background: var(--color-point);
    color: #fff;
    font-weight: 700;
}

/* Sub Content Area */
.sub-content { min-width: 0; } /* prevent flex/grid overflow */

/* Common Subpage Elements Typography override */
.content-body h2 {
    font-size: 32px !important;
    margin-top: 0;
    margin-bottom: 30px;
    padding-bottom: 16px;
    border-bottom: 2px solid var(--color-text-main);
}
.content-body h3 {
    font-size: 24px !important;
    margin-top: 40px;
    margin-bottom: 20px;
    color: var(--color-point) !important;
}
.content-body p {
    font-size: 17px;
    line-height: 1.8;
    margin-bottom: 20px;
    color: var(--color-text-muted);
}
.content-body img {
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    margin: 20px 0;
}

/* Sub CTA Bottom */
.sub-contact-cta {
    background: var(--color-bg-light);
    padding: 80px 0;
    text-align: center;
    border-top: 1px solid var(--color-border);
}
.cta-inner h2 { margin-bottom: 30px; font-size: 32px; }
.cta-actions { display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }
.btn-outline-white {
    background: #fff; border: 2px solid var(--color-border);
    color: var(--color-text-main) !important;
}
.btn-outline-white:hover { border-color: var(--color-primary); }

/* Mobile Adaptations */
@media (max-width: 1024px) {
    .sub-layout { grid-template-columns: 1fr; gap: 40px; padding: 60px 24px; }
    .sub-sidebar { position: relative; top: 0; }
    
    /* Mega menu is hidden on mobile anyway (gnb display none) */
    .mega-menu-panel, .mega-overlay { display: none !important; }
}
@media (max-width: 768px) {
    .sub-hero { height: 250px; }
    .sub-hero-title { font-size: 32px !important; }
    .sub-hero-desc { font-size: 16px; }
    .content-body h2 { font-size: 24px !important; }
}

/* Mobile Accordion Overrides */
.m-gnb > li > a.subOpen { display: flex; justify-content: space-between; align-items: center; }
.m-gnb .gnb_2dul_mo { display: none; background: var(--color-bg-light); padding: 10px 0; }
.m-gnb .gnb_2dul_mo li a { display: block; padding: 12px 20px; font-size: 16px; color: var(--color-text-muted); }
.m-gnb .gnb_2dul_mo li a:hover { color: var(--color-point); font-weight: 600; }
"""

with open('f:/website3/css/redesign_main.css', 'a', encoding='utf-8') as f:
    f.write(new_css)
