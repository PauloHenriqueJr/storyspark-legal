import re

# Update Styles for Experience Timeline
with open("portfolio/styles.css", "r") as f:
    css = f.read()

experience_styles = """
/* --- EXPERIENCE SECTION --- */
.experience-section {
    padding-top: 60px;
    margin-bottom: 80px;
}

.see-experience-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    color: #a1a1a1;
    font-size: 14px;
    margin-bottom: 40px;
    text-decoration: none;
}

.experience-title {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 24px;
    margin-bottom: 48px;
    color: #fff;
}

.timeline {
    display: flex;
    flex-direction: column;
    gap: 40px;
}

.timeline-item {
    display: flex;
    gap: 48px;
}

.timeline-date {
    min-width: 140px;
    color: #444;
    font-size: 14px;
    padding-top: 4px;
}

.timeline-content {
    position: relative;
    padding-left: 0;
}

.timeline-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
}

.status-dot {
    width: 10px;
    height: 10px;
    background: #22c55e;
    border-radius: 50%;
    box-shadow: 0 0 10px #22c55e;
}

.timeline-company {
    font-size: 20px;
    font-weight: 600;
    color: #fff;
}

.company-logo {
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.company-logo img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

.timeline-role {
    color: #a1a1a1;
    font-size: 16px;
    margin-bottom: 12px;
}

.timeline-desc {
    color: #444;
    font-size: 14px;
    line-height: 1.6;
    max-width: 600px;
}

/* Mobile Experience */
@media (max-width: 768px) {
    .timeline-item {
        flex-direction: column;
        gap: 12px;
    }
    .timeline-date {
        min-width: auto;
    }
    .timeline-item {
        position: relative;
        padding-left: 40px;
    }
    .timeline-content::before {
        content: "";
        position: absolute;
        left: -26px;
        top: 30px;
        bottom: -50px;
        width: 1px;
        background: #222;
    }
    .timeline-item:last-child .timeline-content::before {
        display: none;
    }
    .timeline-header {
        position: relative;
    }
    /* Logo circle on mobile */
    .mobile-logo-wrapper {
        position: absolute;
        left: -54px;
        top: 0;
        width: 44px;
        height: 44px;
        background: #111;
        border: 1px solid #333;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 2;
    }
}

/* Hide desktop logo on mobile if needed or adapt */
@media (min-width: 769px) {
    .mobile-logo-wrapper { display: none; }
}
"""

if "EXPERIENCE SECTION" not in css:
    with open("portfolio/styles.css", "a") as f:
        f.write(experience_styles)

with open("portfolio/index.html", "r") as f:
    html = f.read()

experience_html = """<section id="experience" class="experience-section">
          <a href="#" class="see-experience-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            See Experience
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </a>

          <h2 class="experience-title">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            Experience
          </h2>

          <div class="timeline">
            <!-- Experience 1: Indie Hacker -->
            <div class="timeline-item">
              <div class="timeline-date">Mar 2024 - Present</div>
              <div class="timeline-content">
                <div class="mobile-logo-wrapper">
                    <img src="./favicon.svg" width="24" height="24" alt="Logo">
                </div>
                <div class="timeline-header">
                  <div class="status-dot"></div>
                  <span class="timeline-company">Indie Hacker</span>
                  <div class="company-logo">
                    <img src="./favicon.svg" alt="Indie Hacker">
                  </div>
                  <span class="timeline-role">Founder</span>
                </div>
                <p class="timeline-desc">I'm a cracked indie-hacker, iOS and Web App founder. I'm currently working on my own products and sharing my journey on social media.</p>
              </div>
            </div>

            <!-- Experience 2: University Federico II -->
            <div class="timeline-item">
              <div class="timeline-date">Sep 2023 - Present</div>
              <div class="timeline-content">
                <div class="mobile-logo-wrapper">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                </div>
                <div class="timeline-header">
                  <div class="status-dot"></div>
                  <span class="timeline-company">University Federico II</span>
                  <div class="company-logo" style="background: #003087;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg>
                  </div>
                  <span class="timeline-role">Student</span>
                </div>
                <p class="timeline-desc">I'm a student of Computer Science at the University Federico II in Naples, Italy.</p>
              </div>
            </div>

            <!-- Experience 3: GCerti -->
            <div class="timeline-item">
              <div class="timeline-date">Jul 2025 - Nov 2025</div>
              <div class="timeline-content">
                <div class="mobile-logo-wrapper">
                    <div style="width:12px; height:12px; background:#22c55e; border-radius:3px;"></div>
                </div>
                <div class="timeline-header">
                  <span class="timeline-company">GCerti</span>
                  <div class="company-logo" style="background:#22c55e;"></div>
                  <span class="timeline-role">Frontend Developer | Internship</span>
                </div>
                <p class="timeline-desc">I was a frontend developer at GCerti, a company that provides certification services.</p>
              </div>
            </div>

            <!-- Experience 4: Apple Developer Academy -->
            <div class="timeline-item">
              <div class="timeline-date">Oct 2023 - Jun 2024</div>
              <div class="timeline-content">
                <div class="mobile-logo-wrapper">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>
                </div>
                <div class="timeline-header">
                  <span class="timeline-company">Apple Developer Academy</span>
                  <div class="company-logo" style="background:#000;">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>
                  </div>
                  <span class="timeline-role">Student | App Founder</span>
                </div>
                <p class="timeline-desc">I was a student at the Apple Developer Academy in Naples, Italy. I was able to learn about the Apple ecosystem and develop my own apps.</p>
              </div>
            </div>

            <!-- More experiences can be added here following the same pattern -->
          </div>
        </section>"""

# Insert before the apps/projects section or after hero
if '<section id="projects"' in html:
    html = html.replace('<section id="projects"', experience_html + '\n        <section id="projects"')
else:
    html = re.sub(r'</section>\s*<section id="contact"', r'</section>\n' + experience_html + r'\n<section id="contact"', html, flags=re.DOTALL)

with open("portfolio/index.html", "w") as f:
    f.write(html)
