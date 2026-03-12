import re

# Comprehensive update for the "iOS Apps" grid and "Web Apps" section using the user's REAL apps
with open("portfolio/styles.css", "r") as f:
    css = f.read()

# Add specific layouts for high-quality project cards
project_styles = """
/* --- REAL PROJECTS GRID --- */
.section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 60px;
    margin-bottom: 32px;
}

.section-header h2 {
    font-size: 24px;
    font-weight: 500;
}

.apps-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    margin-bottom: 80px;
}

.app-card {
    background: #0d0d0d;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    transition: transform 0.2s ease, border-color 0.2s ease;
    text-decoration: none;
    color: inherit;
}

.app-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 255, 255, 0.15);
}

.app-icon-wrapper {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    overflow: hidden;
    background: #1a1a1a;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
}

.app-icon-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.app-info h3 {
    font-size: 20px;
    color: #fff;
    margin-bottom: 4px;
}

.app-info p {
    font-size: 14px;
    color: #808080;
    line-height: 1.5;
}

.highlight-link {
    font-size: 13px;
    color: #3b82f6;
    margin-top: auto;
    font-weight: 500;
}

/* Response */
@media (max-width: 640px) {
    .apps-grid { grid-template-columns: 1fr; }
}
"""

if "REAL PROJECTS GRID" not in css:
    with open("portfolio/styles.css", "a") as f:
        f.write(project_styles)

with open("portfolio/index.html", "r") as f:
    html = f.read()

# Build the dynamic HTML using Fresta, Senda and OmniWell
real_projects_html = """<section id="projects" class="projects-section">
          <div class="section-header">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <h2>My Real Apps</h2>
          </div>

          <div class="apps-grid">
            <!-- App: Fresta -->
            <a href="https://fresta.com.br" target="_blank" class="app-card">
              <div class="app-icon-wrapper">
                <img src="./fresta.webp" alt="Fresta App Icon">
              </div>
              <div class="app-info">
                <h3>Fresta</h3>
                <p>A high-performance logistics and delivery tracking platform built to streamline operations.</p>
                <div class="highlight-link">fresta.com.br →</div>
              </div>
            </a>

            <!-- App: Senda -->
            <a href="https://senda.com.br" target="_blank" class="app-card">
              <div class="app-icon-wrapper">
                <img src="./senda.webp" alt="Senda App Icon">
              </div>
              <div class="app-info">
                <h3>Senda</h3>
                <p>Innovative communication and connectivity tools for seamless digital interactions.</p>
                <div class="highlight-link">senda.com.br →</div>
              </div>
            </a>

            <!-- App: OmniWell -->
            <a href="https://omniwell.com.br" target="_blank" class="app-card">
              <div class="app-icon-wrapper">
                <img src="./omniwell.webp" alt="OmniWell App Icon">
              </div>
              <div class="app-info">
                <h3>OmniWell</h3>
                <p>Empowering health and wellness management through intelligent tracking and insights.</p>
                <div class="highlight-link">omniwell.com.br →</div>
              </div>
            </a>

            <!-- Placeholder for Future Indie project -->
            <div class="app-card" style="border-style: dashed; background: transparent; opacity: 0.6;">
              <div class="app-icon-wrapper" style="border: 1px dashed #444; background: transparent; display:flex; align-items:center; justify-content:center;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              </div>
              <div class="app-info">
                <h3>Coming Soon...</h3>
                <p>Building something new with Flutter and Supabase. Keep an eye out!</p>
              </div>
            </div>
          </div>
        </section>"""

# Replace the previous grid with the user's real projects
html = re.sub(r'<section id="projects".*?</section>', real_projects_html, html, flags=re.DOTALL)

with open("portfolio/index.html", "w") as f:
    f.write(html)
