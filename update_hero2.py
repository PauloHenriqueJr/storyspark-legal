import re

with open("portfolio/styles.css", "r") as f:
    css = f.read()

# Add styles for the exact hero implementation
if "avatars-container" not in css:
    hero_css = """
/* Top Navbar layout matching reference */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background-color: transparent;
  margin-bottom: 60px;
  max-width: 100%;
}

.logo svg {
  display: block;
}

.nav-links {
  display: flex;
  gap: 24px;
}

.nav-links a {
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s;
}

.nav-links a:hover {
  color: var(--text-primary);
}

.nav-utils {
  display: flex;
  gap: 24px;
  align-items: center;
  color: var(--text-secondary);
}

.nav-utils a {
  color: var(--text-secondary);
  transition: color 0.2s;
}

.nav-utils a:hover {
  color: var(--text-primary);
}

/* Avatar Group */
.avatars-container {
  display: flex;
  position: relative;
  height: 160px;
  margin-bottom: 32px;
}

.avatar-left {
  position: absolute;
  left: 0;
  top: 10px;
  width: 150px;
  height: 140px;
  object-fit: cover;
  border-radius: 20px;
  transform: rotate(-3deg);
  z-index: 1;
  border: 1px solid rgba(255,255,255,0.08);
  filter: brightness(0.6);
}

.avatar-right {
  position: absolute;
  left: 140px;
  top: 0;
  width: 160px;
  height: 150px;
  object-fit: cover;
  border-radius: 20px;
  transform: rotate(2deg);
  z-index: 2;
  box-shadow: -10px 0 25px rgba(0,0,0,0.8);
  border: 1px solid rgba(255,255,255,0.08);
}

/* Title Row */
.title-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.hero-title {
  font-size: 26px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 8px;
  color: #fff;
  font-family: inherit;
}

.greeting {
  color: #6b6b6b;
}

.grid-icon-wrapper {
  width: 36px;
  height: 36px;
  border-radius: 12px;
  background: transparent;
  border: 1px solid rgba(255,255,255,0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #8c8c8c;
  cursor: pointer;
  transition: all 0.2s;
}

.grid-icon-wrapper:hover {
  border-color: #fff;
  color: #fff;
}

/* Tags */
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}

.tag {
  padding: 6px 14px;
  background-color: #121212;
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 12px;
  font-size: 13px;
  color: #a3a3a3;
}

/* Bio Text */
.bio {
  font-size: 18px;
  line-height: 1.6;
  margin-top: 32px;
}

.text-white {
  color: #fff;
  font-weight: 500;
}

.text-mute {
  color: #6b6b6b;
  font-weight: 400;
}

/* Latest Blog */
.latest-blog {
  margin-top: 40px;
  margin-bottom: 40px;
}

.blog-label {
  font-size: 12px;
  color: #6b6b6b;
  font-family: 'Space Mono', monospace;
  margin-bottom: 12px;
}

.blog-link-content {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding-bottom: 2px;
  border-bottom: 1px solid #fff;
  color: #fff;
  transition: opacity 0.2s;
}

.blog-link-content:hover {
  opacity: 0.8;
}

.blog-link-content .blog-title {
  font-family: 'Space Mono', monospace;
  font-size: 14px;
}

/* Stat Grid Updates */
.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 16px;
}

.stat-card {
  background-color: #121212;
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.stat-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  color: #a3a3a3;
  font-size: 14px;
}

.stat-value {
  font-size: 32px;
  font-weight: 400;
  color: #fff;
}
"""
    with open("portfolio/styles.css", "a") as f:
        f.write("\n" + hero_css)

with open("portfolio/index.html", "r") as f:
    html = f.read()

# REPLACE THE ENTIRE HERO AND NAVBAR
html_new = re.sub(
    r'<header class="navbar">.*?</header>',
    r"""<header class="navbar">
        <div class="logo">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <nav class="nav-links">
          <a href="#projects" aria-label="Projects"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></a>
          <a href="#experience" aria-label="Experience"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></a>
          <a href="#terminal" aria-label="Terminal"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg></a>
          <a href="#blog" aria-label="Blog"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></a>
        </nav>
        <div class="nav-utils">
          <a href="#" aria-label="Language"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg></a>
          <a href="#" aria-label="Theme"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg></a>
        </div>
      </header>""",
    html,
    flags=re.DOTALL
)

html_new = re.sub(
    r'<section class="hero-section">.*?</section>\s*<section id="projects"',
    r"""<section class="hero-section">
          <div class="avatars-container">
            <img src="./dGNkMoUq_400x400.jpg" alt="Profile" class="avatar-left" />
            <img src="./dGNkMoUq_400x400.jpg" alt="Profile 2" class="avatar-right" />
          </div>
          
          <div class="title-row">
            <h1 class="hero-title">
              <span class="greeting">Sup!</span> I'm Elmineiro 
              <svg class="verified-icon" width="18" height="18" viewBox="0 0 24 24" fill="#3B82F6"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>
            </h1>
            <div class="grid-icon-wrapper">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="3" width="7" height="7" rx="1"></rect><rect x="14" y="14" width="7" height="7" rx="1"></rect><rect x="3" y="14" width="7" height="7" rx="1"></rect></svg>
            </div>
          </div>

          <div class="tags">
            <span class="tag">Gym</span>
            <span class="tag">F1</span>
            <span class="tag">Coding</span>
            <span class="tag">Traveling</span>
            <span class="tag">Physics</span>
          </div>

          <p class="bio">
            <span class="text-mute">I'm an</span> <span class="text-white">indie hacker</span> <span class="text-mute">and</span> <span class="text-white">founder</span>, <span class="text-mute">building</span> <span class="text-white">iOS</span> <span class="text-mute">and</span> <span class="text-white">web apps.</span>
            <br><br>
            <span class="text-white">I ship my own products</span> <span class="text-mute">and</span> <span class="text-white">share the journey</span> <span class="text-mute">on</span> <span class="text-white">social media.</span>
          </p>

          <div class="latest-blog">
            <div class="blog-label">Read the latest blog</div>
            <a href="https://storyspark.com.br" target="_blank" class="blog-link-content">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
              <span class="blog-title">Building StorySpark Infrastructure...</span>
              <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>

          <div class="stats-grid">
            <div class="stat-card">
              <div class="stat-header">
                <span class="stat-label">iOS Apps</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
              </div>
              <div class="stat-value">3</div>
            </div>
            <div class="stat-card">
              <div class="stat-header">
                <span class="stat-label">Web Apps</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
              </div>
              <div class="stat-value">4</div>
            </div>
            <div class="stat-card">
              <div class="stat-header">
                <span class="stat-label">Followers</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l11.733 16h4.267l-11.733 -16z"></path><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772"></path></svg>
              </div>
              <div class="stat-value">6.4k</div>
            </div>
            <div class="stat-card">
              <div class="stat-header">
                <span class="stat-label">Experience</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              </div>
              <div class="stat-value">2</div>
            </div>
          </div>
        </section>
        <section id="projects" """,
    html_new,
    flags=re.DOTALL
)

with open("portfolio/index.html", "w") as f:
    f.write(html_new)
