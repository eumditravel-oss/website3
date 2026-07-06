css_content = """
/* ==========================================================
   V4 Subpage Global Redesign Layout
========================================================== */
.subpage-new-layout {
    display: flex;
    max-width: 1400px;
    margin: 0 auto;
    padding: 100px 24px 80px;
    gap: 40px;
    align-items: flex-start;
}

/* Sidebar Styles */
.sidebar-new {
    flex: 0 0 260px;
    position: sticky;
    top: 100px;
}
.sidebar-header {
    background: linear-gradient(135deg, var(--color-primary), #1e3a8a);
    color: #fff;
    padding: 40px 20px;
    text-align: center;
    border-radius: var(--radius-md) var(--radius-md) 0 0;
}
.sidebar-header h2 {
    font-size: 24px;
    font-weight: 800;
    margin: 0 0 5px 0;
    color: #fff;
}
.sidebar-header .en {
    font-size: 13px;
    color: rgba(255,255,255,0.7);
    letter-spacing: 1px;
}
.sidebar-menu-new {
    list-style: none;
    padding: 0;
    margin: 0;
    border-left: 1px solid var(--color-border);
    border-right: 1px solid var(--color-border);
    border-bottom: 1px solid var(--color-border);
    background: #fff;
}
.sidebar-menu-new li {
    border-bottom: 1px solid var(--color-border);
}
.sidebar-menu-new li:last-child {
    border-bottom: none;
}
.sidebar-menu-new a {
    display: flex;
    align-items: center;
    padding: 18px 20px;
    font-size: 16px;
    color: var(--color-text-muted);
    transition: all 0.2s;
    font-weight: 500;
    text-decoration: none;
}
.sidebar-menu-new a i {
    width: 24px;
    font-size: 18px;
    margin-right: 10px;
    color: #ccc;
    text-align: center;
    transition: all 0.2s;
}
.sidebar-menu-new a:hover {
    color: var(--color-text-main);
    background: #f8fafc;
}
.sidebar-menu-new li.active a {
    border-left: 4px solid var(--color-primary);
    background: #f0f7ff;
    color: var(--color-primary);
    font-weight: 700;
}
.sidebar-menu-new li.active a i {
    color: var(--color-primary);
}

/* Sidebar Contact Info */
.sidebar-contact {
    margin-top: 30px;
    background: #fff;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    padding: 30px 20px;
    text-align: center;
}
.sidebar-contact .contact-icon {
    width: 50px;
    height: 50px;
    background: #f0f7ff;
    color: var(--color-point);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin: 0 auto 15px;
}
.sidebar-contact h3 {
    font-size: 18px;
    color: var(--color-text-main);
    margin: 0 0 10px 0;
}
.sidebar-contact p {
    font-size: 14px;
    color: var(--color-text-muted);
    line-height: 1.5;
    margin-bottom: 20px;
}
.sidebar-contact .phone {
    font-size: 22px;
    font-weight: 800;
    color: var(--color-primary);
    margin-bottom: 5px;
}
.sidebar-contact .hours {
    font-size: 13px;
    color: #999;
}

/* Content Area */
.content-wrapper {
    flex: 1;
    min-width: 0;
}
.breadcrumb-new {
    display: flex;
    align-items: center;
    font-size: 14px;
    color: #999;
    margin-bottom: 40px;
    padding-bottom: 15px;
    border-bottom: 1px solid var(--color-border);
}
.breadcrumb-new i {
    font-size: 12px;
    margin-right: 5px;
}
.breadcrumb-new span {
    margin: 0 10px;
}
.breadcrumb-new span.current {
    color: var(--color-text-main);
    font-weight: 600;
}
.content-main {
    min-height: 600px;
}

/* V4 Greeting Page Specific Layout */
.greeting-header-new {
    margin-bottom: 40px;
}
.greeting-header-new .en-title {
    display: block;
    font-size: 14px;
    color: var(--color-primary);
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 10px;
}
.greeting-header-new h2 {
    font-size: 32px;
    font-weight: 800;
    color: #111;
    line-height: 1.4;
    margin: 0;
}
.greeting-header-new h2::after {
    content: '';
    display: block;
    width: 40px;
    height: 3px;
    background-color: var(--color-primary);
    margin-top: 20px;
}
.greeting-body {
    display: flex;
    gap: 50px;
    margin-bottom: 60px;
    align-items: stretch;
}
.greeting-text {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.greeting-text p {
    font-size: 16px;
    color: #555;
    line-height: 1.8;
    margin-bottom: 20px;
    word-break: keep-all;
}
.greeting-img {
    flex: 0 0 50%;
    border-radius: 0 0 0 60px;
    overflow: hidden;
}
.greeting-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    min-height: 350px;
}

.greeting-strengths {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    background: #f8fafc;
    border-radius: var(--radius-md);
    padding: 40px 20px;
    margin-bottom: 60px;
}
.greeting-strengths .strength-item {
    text-align: center;
    padding: 0 20px;
    border-right: 1px solid var(--color-border);
}
.greeting-strengths .strength-item:last-child {
    border-right: none;
}
.greeting-strengths .icon {
    font-size: 36px;
    color: var(--color-point);
    margin-bottom: 20px;
}
.greeting-strengths h4 {
    font-size: 16px;
    color: var(--color-text-main);
    margin-bottom: 15px;
    font-weight: 700;
}
.greeting-strengths p {
    font-size: 13px;
    color: var(--color-text-muted);
    line-height: 1.6;
    margin: 0;
    word-break: keep-all;
}

.greeting-footer p {
    font-size: 16px;
    color: #555;
    line-height: 1.8;
    margin-bottom: 30px;
    word-break: keep-all;
}
.greeting-sign {
    text-align: right;
    font-size: 18px;
    font-weight: 600;
    color: #333;
}
.greeting-sign .sign-name {
    font-family: 'Great Vibes', cursive, serif;
    font-size: 40px;
    color: var(--color-primary);
    margin-left: 15px;
    font-weight: normal;
}

@media(max-width: 1024px) {
    .subpage-new-layout {
        flex-direction: column;
    }
    .sidebar-new {
        flex: none;
        width: 100%;
        position: relative;
        top: 0;
    }
    .greeting-body {
        flex-direction: column-reverse;
    }
    .greeting-img {
        border-radius: 20px;
    }
    .greeting-strengths {
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }
    .greeting-strengths .strength-item {
        border-right: none;
    }
}
@media(max-width: 768px) {
    .greeting-strengths {
        grid-template-columns: 1fr;
    }
}
"""

with open("f:/website3/css/redesign_main.css", "a", encoding="utf-8") as f:
    f.write(css_content)

print("CSS added successfully.")
