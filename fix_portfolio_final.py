import re

# Final touch script to fix Navbar Desktop, Hero Avatars, and Bio info
with open("portfolio/styles.css", "r") as f:
    css = f.read()

new_css = """
/* Desktop Pill Navbar */
.navbar {
    position: sticky;
    top: 24px;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(18, 18, 18, 0.8);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 100px;
    padding: 12px 24px;
    margin: 24px auto 60px auto;
    width: 100%;
    max-width: 1200px;
}

.logo svg {
    color: #fff;
}

.nav-links {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 32px;
}

.nav-utils {
    display: flex;
    gap: 20px;
    align-items: center;
}

/* Hero Avatars Correction */
.avatars-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 180px;
    margin-bottom: 40px;
    position: relative;
    width: fit-content;
}

.avatar-left {
    width: 110px;
    height: 110px;
    border-radius: 24px;
    object-fit: cover;
    transform: rotate(-6deg) translateX(20px);
    border: 2px solid #1a1a1a;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    z-index: 1;
    filter: brightness(0.7);
}

.avatar-right {
    width: 120px;
    height: 120px;
    border-radius: 24px;
    object-fit: cover;
    transform: rotate(4deg) translateX(-20px);
    border: 2px solid #1a1a1a;
    box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    z-index: 2;
}

/* Bio highlights */
.highlight-stone { color: #00d382; font-weight: 600; } /* Stone Green */
.highlight-flutter { color: #02569B; font-weight: 600; }
.highlight-react { color: #61DAFB; font-weight: 600; }
.highlight-supabase { color: #3ECF8E; font-weight: 600; }

.tech-stack {
    display: flex;
    gap: 12px;
    margin-top: 20px;
    font-size: 14px;
    color: #888;
}
"""

with open("portfolio/styles.css", "a") as f:
    f.write(new_css)

with open("portfolio/index.html", "r") as f:
    html = f.read()

# Update Navbar with X icon as per screenshot
new_nav = r"""<header class="navbar">
        <div class="logo">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        </div>
        <nav class="nav-links">
          <a href="#projects" aria-label="Projects"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></a>
          <a href="#experience" aria-label="Experience"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></a>
          <a href="#terminal" aria-label="Terminal"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg></a>
          <a href="#blog" aria-label="Blog"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></a>
        </nav>
        <div class="nav-utils">
          <a href="#" aria-label="Language">
            <svg width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path d="M2.5 4v16h19V4H2.5zm1.5 1.5h16v13H4v-13zm2 2v2h2v-2H6zm3 0v2h2v-2H9zm3 0v2h2v-2h-2zm3 0v2h2v-2h-2zm-9 3v2h2v-2H6zm3 0v2h2v-2H9zm3 0v2h2v-2h-2zm3 0v2h2v-2h-2zm-9 3v2h2v-2H6zm3 0v2h2v-2H9zm3 0v2h2v-2h-2zm3 0v2h2v-2h-2z" fill="currentColor"/></svg>
          </a>
          <a href="#" aria-label="Theme"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg></a>
          <a href="https://x.com" target="_blank" aria-label="X (Twitter)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
          </a>
        </div>
      </header>"""

html = re.sub(r'<header class="navbar">.*?</header>', new_nav, html, flags=re.DOTALL)

# Update Bio and Avatars content
new_hero = r"""<section class="hero-section">
          <div class="avatars-container">
            <img src="./dGNkMoUq_400x400.jpg" alt="Profile Left" class="avatar-left" />
            <img src="./dGNkMoUq_400x400.jpg" alt="Profile Right" class="avatar-right" />
          </div>
          
          <div class="title-row">
            <h1 class="hero-title">
              <span class="greeting">Sup!</span> I'm Paulo Henrique 
              <svg class="verified-icon" width="18" height="18" viewBox="0 0 24 24" fill="#3B82F6"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>
            </h1>
          </div>

          <div class="tags">
            <span class="tag">🇧🇷 Brazilian</span>
            <span class="tag">Indie Hacker</span>
            <span class="tag">Gym</span>
            <span class="tag">Coding</span>
          </div>

          <p class="bio">
            <span class="text-mute">Senior Mobile Developer at</span> <span class="highlight-stone">Stone Payments</span>. 
            <br><br>
            <span class="text-mute">I'm a passionate</span> <span class="text-white">Indie Hacker</span> <span class="text-mute">from Brazil, crafting high-quality</span> 
            <span class="text-white">iOS & Android</span> <span class="text-mute">apps.</span>
            <br><br>
            <span class="text-mute">Expertise in</span> <span class="highlight-flutter">Flutter</span>, <span class="highlight-react">React</span> <span class="text-mute">and</span> <span class="highlight-supabase">Supabase</span>. 
            <span class="text-mute">Developing seamless experiences for</span> <span class="text-white">Mobile & Web</span>.
          </p>
        </section>"""

html = re.sub(r'<section class="hero-section">.*?</section>', new_hero, html, flags=re.DOTALL)

with open("portfolio/index.html", "w") as f:
    f.write(html)
