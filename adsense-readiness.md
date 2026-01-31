# AdSense Readiness Plan

## 📋 Overview
The goal is to prepare the "Freight Class Density Calculator" website for Google AdSense approval. This requires adding mandatory legal pages, ensuring content quality, optimizing for user experience, and technical compliance.

## 🎯 Success Criteria
- [ ] Privacy Policy page exists and is linked.
- [ ] Terms of Service page exists and is linked.
- [ ] Contact Us page exists with functional contact info/form.
- [ ] About Us section/page clarifies the site's purpose.
- [ ] Cookie Consent banner is implemented (GDPR/CCPA compliance).
- [ ] `ads.txt` file exists (placeholder).
- [ ] Navigation is clear and accessible.
- [ ] Site passes Google's Core Web Vitals (Speed/UX).
- [ ] No "Thin Content" penalties (sufficient text on main page).

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla).
- **Hosting**: GitHub Pages (implied).

## 📂 File Structure Updates
```
/
├── privacy.html       [NEW]
├── terms.html         [NEW]
├── contact.html       [NEW]
├── ads.txt            [NEW]
├── index.html         [MODIFY - Add links/Cookie Banner]
└── style.css          [MODIFY - Styles for new pages/banner]
```

## 📝 Task Breakdown

### Phase 1: Mandatory Legal Pages (Frontend Specialist)
- [ ] **Create Privacy Policy**: Standard AdSense-compliant privacy policy logic.
  - *Input*: Template with cookies/data collection info.
  - *Output*: `privacy.html`
  - *Verify*: File exists and contains "Google AdSense" mentions.
- [ ] **Create Terms of Service**: Standard disclaimer for calculator accuracy.
  - *Input*: Liability disclaimer (not professional advice).
  - *Output*: `terms.html`
  - *Verify*: File exists and contains "Limitation of Liability".
- [ ] **Create Contact Page**: Simple contact info or form.
  - *Input*: Email address protection check.
  - *Output*: `contact.html`
  - *Verify*: File exists and is accessible.

### Phase 2: UX & Navigation (Frontend Specialist)
- [ ] **Footer Navigation**: Add links to Privacy, Terms, and Contact in `index.html`.
  - *Input*: `index.html` footer section.
  - *Output*: Updated footer.
  - *Verify*: Links are clickable and lead to correct pages.
- [ ] **Cookie Consent Banner**: Add a simple banner for cookie acceptance.
  - *Input*: JS logic for localStorage.
  - *Output*: HTML/CSS/JS in main files.
  - *Verify*: Banner appears on first visit, disappears on accept.
- [ ] **Navigation Menu Update**: Ensure "Resources" or "About" is visible.

### Phase 3: Technical & Content (SEO/Backend Specialist)
- [ ] **Create ads.txt**: Add a placeholder `ads.txt` file.
  - *Input*: Standard format `google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0`.
  - *Output*: `ads.txt`.
  - *Verify*: File accessible at root.
- [ ] **Content Enrichment**: Review `index.html` for "Thin Content".
  - *Input*: Current text vs. Competitors (Freightos/FedEx).
  - *Output*: Add more "How to use" or "Why is this accurate" text if needed.
  - *Verify*: SEO Check passes.

## ✅ Phase X: Verification
- [ ] **Security Scan**: `python .agent/scripts/checklist.py` (includes security)
- [ ] **UX Audit**: `python .agent/skills/frontend-design/scripts/ux_audit.py .`
- [ ] **SEO Check**: `python .agent/skills/seo-fundamentals/scripts/seo_checker.py .`
- [ ] **Manual Check**: Verify all links in footer work.
- [ ] **Manual Check**: Verify Cookie Banner behavior.
