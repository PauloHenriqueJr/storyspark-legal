import re

# Comprehensive fix for Styles and Layout based on the visual references
with open("portfolio/styles.css", "r") as f:
    css = f.read()

# Define a clean start for the styles to avoid conflicts
base_styles = """
:root {
  --bg-dark: #000000;
  --card-bg: #111111;
  --nav-bg: rgba(15, 15, 15, 0.7);
  --text-primary: #ffffff;
  --text-secondary: #a1a1a1;
  --accent-blue: #3b82f6;
  --border-color: rgba(255, 255, 255, 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: var(--bg-dark);
  color: var(--text-primary);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  line-height: 1.5;
  overflow-x: hidden;
}

.site-wrapper {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}

/* --- NAVBAR PILL --- */
.navbar {
  position: fixed;
  top: 24px;
  left: 50%;
  transform: translateX(-50%);
  width: calc(100% - 40px);
  max-width: 800px;
  height: 54px;
  background: var(--nav-bg);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-color);
  border-radius: 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
  z-index: 1000;
}

.nav-left, .nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nav-center {
  display: flex;
  gap: 24px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.nav-item {
  color: var(--text-secondary);
  text-decoration: none;
  display: flex;
  align-items: center;
  transition: color 0.2s;
}

.nav-item:hover {
  color: var(--text-primary);
}

.nav-item svg {
  width: 20px;
  height: 20px;
}

/* --- HERO SECTION --- */
.hero-section {
  padding-top: 140px;
  padding-bottom: 60px;
}

.avatars-container {
  display: flex;
  position: relative;
  height: 140px;
  margin-bottom: 40px;
}

.avatar-left {
  width: 120px;
  height: 120px;
  object-fit: cover;
  border-radius: 20px;
  transform: rotate(-4deg);
  border: 1px solid var(--border-color);
  position: absolute;
}

.avatar-right {
  width: 130px;
  height: 130px;
  object-fit: cover;
  border-radius: 20px;
  transform: rotate(2deg);
  border: 1px solid var(--border-color);
  position: absolute;
  left: 100px;
  box-shadow: -10px 0 30px rgba(0,0,0,0.5);
}

.hero-title {
  font-size: 28px;
  font-weight: 500;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.greeting { color: var(--text-secondary); }

.tags {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
}

.tag {
  background: #1a1a1a;
  padding: 6px 14px;
  border-radius: 10px;
  font-size: 13px;
  color: var(--text-secondary);
  border: 1px solid var(--border-color);
}

.bio {
  font-size: 18px;
  color: var(--text-secondary);
  max-width: 600px;
  margin-bottom: 40px;
}

.text-white { color: #fff; font-weight: 500; }
.highlight-stone { color: #00d382; font-weight: 600; }

/* --- PROJECTS --- */
.projects-section h2 {
  font-size: 20px;
  margin-bottom: 24px;
}

.projects-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.project-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  background: #0a0a0a;
  border: 1px solid var(--border-color);
  border-radius: 16px;
  text-decoration: none;
}

.project-icon {
  width: 54px;
  height: 54px;
  border-radius: 12px;
  object-fit: cover;
}

.project-info h3 {
  font-size: 16px;
  color: #fff;
  margin-bottom: 2px;
}

.project-info p {
  font-size: 14px;
  color: var(--text-secondary);
}

.nav-item-x {
  color: #fff;
}
"""

with open("portfolio/styles.css", "w") as f:
    f.write(base_styles)

# Update the HTML to much cleaner structure
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paulo Henrique | Developer</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="site-wrapper">
        <header class="navbar">
            <div class="nav-left">
                <a href="#" class="nav-item">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
                </a>
            </div>
            
            <nav class="nav-center">
                <a href="#projects" class="nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                </a>
                <a href="#experience" class="nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                </a>
                <a href="#terminal" class="nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                </a>
                <a href="#blog" class="nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                </a>
            </nav>

            <div class="nav-right">
                <a href="#" class="nav-item">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z"/></svg>
                </a>
                <a href="#" class="nav-item">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
                </a>
                <a href="https://x.com/PHenriqueJr_" target="_blank" class="nav-item nav-item-x">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                </a>
            </div>
        </header>

        <main>
            <section class="hero-section">
                <div class="avatars-container">
                    <img src="./dGNkMoUq_400x400.jpg" alt="Profile" class="avatar-left">
                    <img src="./dGNkMoUq_400x400.jpg" alt="Profile" class="avatar-right">
                </div>
                
                <h1 class="hero-title">
                    <span class="greeting">Sup!</span> I'm Paulo Henrique
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="#3B82F6"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>
                </h1>

                <div class="tags">
                    <span class="tag">🇧🇷 Brazilian</span>
                    <span class="tag">Indie Hacker</span>
                    <span class="tag">Coding</span>
                </div>

                <p class="bio">
                    <span class="text-white">Senior Mobile Developer</span> at <span class="highlight-stone">Stone Payments</span>. 
                    I'm an indie hacker from Brazil building iOS, Android and Web apps with <span class="text-white">Flutter, React and Supabase.</span>
                </p>
            </section>

            <section id="projects" class="projects-section">
                <h2>Projects</h2>
                <div class="projects-grid">
                    <a href="https://fresta.com.br" class="project-card" target="_blank">
                        <img src="./fresta.webp" alt="Fresta" class="project-icon">
                        <div class="project-info">
                            <h3>Fresta</h3>
                            <p>Modern logistics and delivery tracking solution.</p>
                        </div>
                    </a>
                    <a href="https://senda.com.br" class="project-card" target="_blank">
                        <img src="./senda.webp" alt="Senda" class="project-icon">
                        <div class="project-info">
                            <h3>Senda</h3>
                            <p>Streamlining communication and connectivity.</p>
                        </div>
                    </a>
                    <a href="https://omniwell.com.br" class="project-card" target="_blank">
                        <img src="./omniwell.webp" alt="OmniWell" class="project-icon">
                        <div class="project-info">
                            <h3>OmniWell</h3>
                            <p>Health and wellness management at your fingertips.</p>
                        </div>
                    </a>
                </div>
            </section>
        </main>
    </div>
</body>
</html>
"""

with open("portfolio/index.html", "w") as f:
    f.write(html_content)
