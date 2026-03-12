import re

# Update Styles for Skills Mobile Grid
with open("portfolio/styles.css", "r") as f:
    css = f.read()

# Replace the existing mobile skills adjustment with the exact layout requested
mobile_fix = """
/* Mobile Skills exact layout match */
@media (max-width: 600px) {
    .skills-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 8px;
    }
    .skill-card {
        padding: 12px;
        border-radius: 12px;
        min-height: 80px;
    }
    .skill-years {
        font-size: 10px;
    }
    .skill-name {
        font-size: 13px;
        margin-top: 4px;
    }
    .skill-icon svg {
        width: 18px;
        height: 18px;
    }
}
"""

# Check if we already have a mobile skills rule to replace or just append
if ".skills-grid {" in css and "@media (max-width: 480px) {" in css:
    css = re.sub(r'@media \(max-width: 480px\) \{.*?\.skills-grid \{.*?\}', mobile_fix, css, flags=re.DOTALL)
else:
    css += mobile_fix

with open("portfolio/styles.css", "w") as f:
    f.write(css)
