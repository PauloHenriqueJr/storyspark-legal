import re

# Comprehensive update for the "iOS Apps" grid and "Contact Me" section
with open("portfolio/styles.css", "r") as f:
    css = f.read()

apps_css = """
/* --- iOS APPS GRID --- */
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
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 80px;
}

.app-card {
    background: #0d0d0d;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.app-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 255, 255, 0.1);
}

.app-icon-wrapper {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    overflow: hidden;
    background: #1a1a1a;
}

.app-icon-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.app-info h3 {
    font-size: 18px;
    color: #fff;
    margin-bottom: 8px;
}

.app-info p {
    font-size: 13px;
    color: #808080;
    line-height: 1.5;
}

/* --- CONTACT ME --- */
.contact-section {
    background: #0d0d0d;
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 24px;
    padding: 40px;
    margin-bottom: 60px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.contact-left h2 {
    font-size: 32px;
    margin-bottom: 24px;
}

.contact-details {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.contact-item { text-decoration: none; color: inherit; }
.email-text { font-size: 18px; color: #808080; }
.other-contacts { color: #505050; font-size: 14px; margin-top: 8px; }
.site-link { font-size: 18px; color: #fff; margin-top: 4px; display: block; }
.copyright { color: #505050; font-size: 14px; margin-top: 32px; }

.contact-right {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.social-btn {
    width: 44px;
    height: 44px;
    background: #1a1a1a;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    transition: background 0.2s;
}

.social-btn:hover { background: #252525; }

/* Responsive */
@media (max-width: 768px) {
    .apps-grid { grid-template-columns: 1fr; }
    .contact-section { flex-direction: column; align-items: flex-start; gap: 40px; }
}
"""

with open("portfolio/styles.css", "a") as f:
    f.write(apps_css)

with open("portfolio/index.html", "r") as f:
    html = f.read()

# Replace projects section with the new App Grid and Contact Me
new_content = r"""<section id="projects" class="projects-section">
          <div class="section-header">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="4"></circle><line x1="12" y1="17" x2="12" y2="19"></line><line x1="12" y1="5" x2="12" y2="7"></line><line x1="17" y1="12" x2="19" y2="12"></line><line x1="5" y1="12" x2="7" y2="12"></line></svg>
            <h2>iOS Apps</h2>
          </div>

          <div class="apps-grid">
            <!-- App 1: TidyFlow -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#22C55E; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>TidyFlow</h3>
                <p>Revolutionize the way of remembering tasks. Urgent notifications, Routine tasks, Voice memos to capture your thoughts and much more.</p>
              </div>
            </div>

            <!-- App 2: TidySpace -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#000; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                   <svg width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm0 18c-3.31 0-6-2.69-6-6s2.69-6 6-6 6 2.69 6 6-2.69 6-6 6z"/><path d="M12 8c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4z"/></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>TidySpace</h3>
                <p>Store from A to Z. Links, Photos, Docs and Notes, all in one place. Easy to recover, easy to send.</p>
              </div>
            </div>

            <!-- App 3: MagicDec -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#111; width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:24px;">01</div>
              </div>
              <div class="app-info">
                <h3>MagicDec</h3>
                <p>The funniest way to learn and do conversion with binary digits. Transform numbers to colors, convert ascii, decimals, binary and hex.</p>
              </div>
            </div>

            <!-- App 4: BMI -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#fff; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="black"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 12h10"/></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>BMI</h3>
                <p>Simple, but efficient way to keep track of your BMI. Log your weight, and let the math do its work. Get healthy, stay healthy.</p>
              </div>
            </div>

            <!-- App 5: GoodBites -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#FBBF24; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                   <svg width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M11 9H9V2H7v7H5V2H3v7c0 2.12 1.66 3.84 3.75 3.97V22h2.5v-9.03C11.34 12.84 13 11.12 13 9V2h-2v7zm5-3v8h2.5v8H21V2c-2.76 0-5 2.24-5 4z"/></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>GoodBites</h3>
                <p>Your personal cookbook. Send recipes from the internet to the app. Add your meals, cook them, and enjoy them.</p>
              </div>
            </div>

            <!-- App 6: PDF Mastery -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#DC2626; width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:14px; flex-direction:column;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                  PDF
                </div>
              </div>
              <div class="app-info">
                <h3>PDF Mastery</h3>
                <p>PDF and Image tools. From compression to conversion, everything at hand. Merge, Split, Convert, Compress and Share.</p>
              </div>
            </div>
            
            <!-- App 7: Khrona -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#fff; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><path d="M2.5 2v6h6M21.5 22v-6h-6"/><path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.3"/></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>Khrona</h3>
                <p>Keep track of your life. Understand how your days are going. Spot patterns in your days, mood and journal. Get better.</p>
              </div>
            </div>

            <!-- App 8: SoloType -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#fff; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>SoloType</h3>
                <p>A fun way to interact with yourself and your other personality. Reply to yourself, create chats, and store messages and thoughts.</p>
              </div>
            </div>

            <!-- App 9: Lystra -->
            <div class="app-card">
              <div class="app-icon-wrapper">
                <div style="background:#fff; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                   <svg width="32" height="32" viewBox="0 0 24 24" fill="black"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                </div>
              </div>
              <div class="app-info">
                <h3>Lystra</h3>
                <p>A minimal app to add things on the fly. Thoughts and Todos with recordings speech to text.</p>
              </div>
            </div>
          </div>
        </section>

        <section id="contact" class="contact-section">
          <div class="contact-left">
            <h2>Contact Me</h2>
            <div class="contact-details">
              <a href="mailto:emandipietro@gmail.com" class="contact-item email-text">emandipietro@gmail.com</a>
              <div>
                <span class="other-contacts">Other Contacts</span>
                <a href="https://emanueledp.site" class="contact-item site-link">emanueledp.site</a>
              </div>
              <p class="copyright">© 2026 Emanuele Di Pietro</p>
            </div>
          </div>
          <div class="contact-right">
            <a href="#" class="social-btn"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></svg></a>
            <a href="#" class="social-btn"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a>
            <a href="#" class="social-btn"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
            <a href="#" class="social-btn"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.377.505 9.377.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
          </div>
        </section>"""

html = re.sub(r'<section id="projects".*?</section>', new_content, html, flags=re.DOTALL)

with open("portfolio/index.html", "w") as f:
    f.write(html)
