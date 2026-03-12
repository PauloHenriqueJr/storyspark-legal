import re

# Update index.html and styles.css for a perfect match with the reference screenshot

with open("portfolio/styles.css", "r") as f:
    css = f.read()

# Add specific styles for the pill navbar and project icons
new_css = """
/* Exact Pill Navbar matching screenshot */
.navbar {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 95%;
    max-width: 1100px;
    height: 64px;
    background: rgba(10, 10, 10, 0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 100px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 24px;
    z-index: 1000;
}

.nav-left {
    display: flex;
    align-items: center;
}

.nav-center {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 24px;
}

.nav-right {
    display: flex;
    align-items: center;
    gap: 20px;
}

.nav-item {
    color: #a3a3a3;
    transition: color 0.2s, transform 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nav-item:hover {
    color: #ffffff;
    transform: translateY(-2px);
}

.nav-item svg {
    width: 20px;
    height: 20px;
}

/* Project Card Images Fix */
.project-card {
    background: #141414;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 24px;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    overflow: hidden;
}

.project-card:hover {
    transform: translateY(-8px);
    border-color: rgba(255, 255, 255, 0.15);
}

.project-image-container {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    margin-bottom: 20px;
    overflow: hidden;
    background: #1a1a1a;
    display: flex;
    align-items: center;
    justify-content: center;
}

.project-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Text Highlights for Stone etc */
.text-stone { color: #00d382; }
.text-highlight { color: #ffffff; font-weight: 500; }
.text-muted { color: #737373; }
"""

# Append or replace if exists
if ".navbar {" in css:
    css = re.sub(r'/\* Desktop Pill Navbar \*/.*?/\* Stat Grid Updates \*/', new_css, css, flags=re.DOTALL)
else:
    css += new_css

with open("portfolio/styles.css", "w") as f:
    f.write(css)

with open("portfolio/index.html", "r") as f:
    html = f.read()

# Update Navbar to use the exact structure from the screenshot
navbar_html = """<header class="navbar">
      <div class="nav-left">
        <a href="/" class="nav-item">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        </a>
      </div>
      
      <nav class="nav-center">
        <a href="#projects" class="nav-item" title="Projects">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
        </a>
        <a href="#experience" class="nav-item" title="Experience">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
        </a>
        <a href="#terminal" class="nav-item" title="Terminal">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
        </a>
        <a href="#blog" class="nav-item" title="Blog">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        </a>
      </nav>

      <div class="nav-right">
        <a href="#" class="nav-item" title="Language">
          <svg width="20" height="20" viewBox="0 0 24 24"><path d="M2.5 4v16h19V4H2.5zm1.5 1.5h16v13H4v-13zm2 2v2h2v-2H6zm3 0v2h2v-2H9zm3 0v2h2v-2h-2zm3 0v2h2v-2h-2zm-9 3v2h2v-2H6zm3 0v2h2v-2H9zm3 0v2h2v-2h-2zm3 0v2h2v-2h-2zm-9 3v2h2v-2H6zm3 0v2h2v-2H9zm3 0v2h2v-2h-2zm3 0v2h2v-2h-2z" fill="currentColor"/></svg>
        </a>
        <a href="#" class="nav-item" title="Theme">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
        </a>
        <a href="https://x.com/PHenriqueJr_" target="_blank" class="nav-item" title="X (Twitter)">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
        </a>
      </div>
    </header>"""

html = re.sub(r'<header class="navbar">.*?</header>', navbar_html, html, flags=re.DOTALL)

# Update Projects to use the WebP icons
projects_html = """<section id="projects" class="projects-section">
          <h2>Projects</h2>
          <div class="projects-grid">
            <div class="project-card">
              <div class="project-image-container">
                <img src="./fresta.webp" alt="Fresta App">
              </div>
              <h3>Fresta</h3>
              <p class="text-muted">A modern solution for logistics and delivery tracking.</p>
              <a href="https://fresta.com.br" class="project-link">View Project →</a>
            </div>
            <div class="project-card">
              <div class="project-image-container">
                <img src="./senda.webp" alt="Senda App">
              </div>
              <h3>Senda</h3>
              <p class="text-muted">Streamlining communication and connectivity.</p>
              <a href="https://senda.com.br" class="project-link">View Project →</a>
            </div>
            <div class="project-card">
              <div class="project-image-container">
                <img src="./omniwell.webp" alt="OmniWell App">
              </div>
              <h3>OmniWell</h3>
              <p class="text-muted">Health and wellness management at your fingertips.</p>
              <a href="https://omniwell.com.br" class="project-link">View Project →</a>
            </div>
          </div>
        </section>"""

html = re.sub(r'<section id="projects".*?</section>', projects_html, html, flags=re.DOTALL)

with open("portfolio/index.html", "w") as f:
    f.write(html)
