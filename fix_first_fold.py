import re

# Comprehensive fix for Hero Section to match the mobile/desktop screenshots exactly
with open("portfolio/styles.css", "r") as f:
    css = f.read()

hero_visual_styles = """
/* --- EXACT HERO VISUALS --- */
.hero-section {
    padding-top: 100px;
    padding-bottom: 40px;
}

.avatars-container {
    display: flex;
    position: relative;
    height: 180px;
    margin-bottom: 48px;
    width: 100%;
}

.avatar-left {
    width: 160px;
    height: 170px;
    object-fit: cover;
    border-radius: 24px;
    transform: rotate(-6deg);
    border: 2px solid #1a1a1a;
    position: absolute;
    left: 0;
    z-index: 1;
    filter: brightness(0.8);
}

.avatar-right {
    width: 170px;
    height: 185px;
    object-fit: cover;
    border-radius: 24px;
    transform: rotate(3deg);
    border: 2px solid #1a1a1a;
    position: absolute;
    left: 110px;
    z-index: 2;
    box-shadow: -15px 0 35px rgba(0,0,0,0.7);
}

.title-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 16px;
}

.hero-title {
    font-size: 24px;
    font-weight: 500;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 6px;
}

.greeting {
    color: #444; /* Darker "Sup!" */
}

.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 32px;
}

.tag {
    background: #121212;
    padding: 6px 16px;
    border-radius: 12px;
    font-size: 14px;
    color: #a1a1a1;
    border: 1px solid rgba(255,255,255,0.05);
}

.bio {
    font-size: 22px;
    line-height: 1.4;
    color: #444; /* Muted color for "I'm an", "and", etc. */
}

.bio .text-white {
    color: #fff;
    font-weight: 500;
}

.blog-preview {
    margin: 40px 0;
}

.blog-label {
    font-size: 14px;
    color: #444;
    margin-bottom: 12px;
}

.blog-link {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    color: #fff;
    font-size: 18px;
    border-bottom: 1px solid #fff;
    padding-bottom: 4px;
    width: fit-content;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 40px;
}

.stat-card {
    background: #0d0d0d;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 24px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 140px;
}

.stat-card .label-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #444;
    font-size: 14px;
}

.stat-card .value {
    font-size: 36px;
    font-weight: 400;
    color: #fff;
}

/* Mobile adjustments */
@media (max-width: 600px) {
    .avatars-container { height: 160px; }
    .avatar-left { width: 140px; height: 150px; }
    .avatar-right { width: 150px; height: 165px; left: 90px; }
    .bio { font-size: 18px; }
}
"""

with open("portfolio/styles.css", "a") as f:
    f.write(hero_visual_styles)

with open("portfolio/index.html", "r") as f:
    html = f.read()

# Update Content to match the very first fold exactly
hero_html = r"""<section class="hero-section">
                <div class="avatars-container">
                    <img src="./dGNkMoUq_400x400.jpg" alt="Elmineiro" class="avatar-left">
                    <img src="./dGNkMoUq_400x400.jpg" alt="Elmineiro" class="avatar-right">
                </div>
                
                <div class="title-row">
                    <h1 class="hero-title">
                        <span class="greeting">Sup!</span> I'm Elmineiro
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="#3B82F6"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg>
                    </h1>
                </div>

                <div class="tags">
                    <span class="tag">Gym</span>
                    <span class="tag">F1</span>
                    <span class="tag">Coding</span>
                    <span class="tag">Traveling</span>
                    <span class="tag">Physics</span>
                </div>

                <p class="bio">
                    I'm an <span class="text-white">indie hacker</span> and <span class="text-white">founder</span>, building <span class="text-white">iOS</span> and <span class="text-white">web apps.</span>
                    <br>
                    I <span class="text-white">ship my own products</span> and <span class="text-white">share the journey</span> on <span class="text-white">social media.</span>
                </p>

                <div class="blog-preview">
                    <div class="blog-label">Read the latest blog</div>
                    <a href="#" class="blog-link">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                        I Stopped Listening to Music for a Week. H...
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left:auto;"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                </div>

                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="label-row">
                            <span>iOS Apps</span>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        </div>
                        <div class="value">9</div>
                    </div>
                    <div class="stat-card">
                        <div class="label-row">
                            <span>Web Apps</span>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                        </div>
                        <div class="value">6</div>
                    </div>
                    <div class="stat-card">
                        <div class="label-row">
                            <span>Followers</span>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg>
                        </div>
                        <div class="value">6.468</div>
                    </div>
                    <div class="stat-card">
                        <div class="label-row">
                            <span>Experience</span>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        </div>
                        <div class="value">2</div>
                    </div>
                </div>
            </section>"""

html = re.sub(r'<section class="hero-section">.*?</section>', hero_html, html, flags=re.DOTALL)

with open("portfolio/index.html", "w") as f:
    f.write(html)
