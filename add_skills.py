import re

# Update Styles for Skills Grid
with open("portfolio/styles.css", "r") as f:
    css = f.read()

skills_styles = """
/* --- SKILLS SECTION --- */
.skills-section {
    padding-top: 60px;
    margin-bottom: 80px;
}

.skills-title {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 24px;
    margin-bottom: 40px;
    color: #fff;
}

.skill-category {
    margin-bottom: 40px;
}

.category-title {
    font-size: 18px;
    font-weight: 500;
    margin-bottom: 20px;
    color: #fff;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 12px;
}

.skill-card {
    background: #0d0d0d;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.skill-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.skill-icon {
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.skill-years {
    font-size: 12px;
    color: #444;
}

.skill-name {
    font-size: 15px;
    color: #fff;
    font-weight: 500;
}

/* Mobile Skills */
@media (max-width: 480px) {
    .skills-grid {
        grid-template-columns: 1fr;
    }
}
"""

if "SKILLS SECTION" not in css:
    with open("portfolio/styles.css", "a") as f:
        f.write(skills_styles)

with open("portfolio/index.html", "r") as f:
    html = f.read()

skills_html = """
        <section id="skills" class="skills-section">
          <h2 class="skills-title">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            Skills
          </h2>

          <!-- iOS Development -->
          <div class="skill-category">
            <h3 class="category-title">iOS Development</h3>
            <div class="skills-grid">
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#F05138"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">Swift/SwiftUI</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">1-2 years</span>
                </div>
                <span class="skill-name">SwiftData</span>
              </div>
            </div>
          </div>

          <!-- Web Development -->
          <div class="skill-category">
            <h3 class="category-title">Web Development</h3>
            <div class="skills-grid">
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2h10v10H12z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">NextJS</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#61DAFB"><circle cx="12" cy="12" r="2"/><path d="M12 7c2.76 0 5 2.24 5 5s-2.24 5-5 5-5-2.24-5-5 2.24-5 5-5zm0-2c-3.87 0-7 3.13-7 7s3.13 7 7 7 7-3.13 7-7-3.13-7-7-7z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">React</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#F7DF1E"><path d="M3 3h18v18H3z"/></svg></div>
                  <span class="skill-years">3-4 years</span>
                </div>
                <span class="skill-name">Javascript</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#3178C6"><path d="M3 3h18v18H3z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">Typescript</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#38B2AC"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">Tailwind</span>
              </div>
            </div>
          </div>

          <!-- General -->
          <div class="skill-category">
            <h3 class="category-title">General</h3>
            <div class="skills-grid">
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#00599C"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">0-1 years</span>
                </div>
                <span class="skill-name">C</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#3776AB"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">1-2 years</span>
                </div>
                <span class="skill-name">Python</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#FFCA28"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">Firebase</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2h4v10h-4zM8 8h4v10H8z"/></svg></div>
                  <span class="skill-years">3-4 years</span>
                </div>
                <span class="skill-name">RestAPI</span>
              </div>
            </div>
          </div>

          <!-- Tools & Software -->
          <div class="skill-category">
            <h3 class="category-title">Tools & Software</h3>
            <div class="skills-grid">
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#F24E1E"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">3-4 years</span>
                </div>
                <span class="skill-name">Figma</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#1572B6"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">2-3 years</span>
                </div>
                <span class="skill-name">XCode</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#007ACC"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">3-4 years</span>
                </div>
                <span class="skill-name">VSCode</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#0070C9"><path d="M12 2L2 7l10 5 10-5-10-5z"/></svg></div>
                  <span class="skill-years">1-2 years</span>
                </div>
                <span class="skill-name">App Store Connect</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2h4v10h-4z"/></svg></div>
                  <span class="skill-years">3-4 years</span>
                </div>
                <span class="skill-name">GitHub</span>
              </div>
              <div class="skill-card">
                <div class="skill-header">
                  <div class="skill-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="#635BFF"><path d="M12 2h4v10h-4z"/></svg></div>
                  <span class="skill-years">1-2 years</span>
                </div>
                <span class="skill-name">Stripe</span>
              </div>
            </div>
          </div>
        </section>
"""

# Insert after experience section
if '</section>\n        <section id="projects"' in html:
    html = html.replace('</section>\n        <section id="projects"', '</section>\n' + skills_html + '\n        <section id="projects"')
else:
    # Fallback to insert before projects
    html = html.replace('<section id="projects"', skills_html + '\n        <section id="projects"')

with open("portfolio/index.html", "w") as f:
    f.write(html)
