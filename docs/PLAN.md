# 🎯 Pre-Live Audit & Optimization Plan

This plan outlines the final verification and hardening phase for the **FreightClassCalc** blog before going live. We will use a multi-agent approach to ensure the site is secure, performant, and visible.

## 🤖 Squad Assembly

| Agent | Focus Area | Responsibility |
|-------|------------|----------------|
| `project-planner` | Orchestration | Task management, synchronization |
| `seo-specialist` | Visibility | Meta audits, Schema.org, GEO optimization |
| `security-auditor` | Hardening | Vulnerability scans, header security, XSS/CSRF checks |
| `performance-optimizer` | Speed | Lighthouse audits, image optimization, Core Web Vitals |
| `test-engineer` | Verification | Link integrity, responsive design, functional testing |

---

## 📋 Audit Surface

### 1. SEO & Discoverability (`seo-specialist`)
- [ ] **Meta Tag Audit**: Verify all 30 articles have unique titles, descriptions, and OpenGraph tags.
- [ ] **Semantic Structure**: Validate H1-H6 hierarchy for engine indexing.
- [ ] **Image Alt-Text**: Ensure all "Nano Banana" illustrations have descriptive alt tags for accessibility and image search.
- [ ] **Sitemap/Robots**: Verify indexing configuration.

### 2. Security & Compliance (`security-auditor`)
- [ ] **Head Hardening**: Check for missing security headers (CSP, HSTS, X-Frame-Options).
- [ ] **Contact Form Audit**: Test the `contact.html` for basic injection vulnerabilities.
- [ ] **Code Privacy Check**: Ensure no API keys or local file paths are exposed in the HTML.

### 3. Performance & UX (`performance-optimizer`)
- [ ] **Lighthouse Audit**: Benchmark the Home page and representative blog posts.
- [ ] **Image Optimization**: Audit the 30 PNG assets for size (aiming for <500KB where possible).
- [ ] **Render Blocking**: Identify and defer non-critical JS/CSS.

### 4. Functional Integrity (`test-engineer`)
- [ ] **Link Audit**: Run a crawler to find any 404s or circular redirects.
- [ ] **Responsive Check**: Ensure the new blog grid behaves on mobile devices.
- [ ] **Header/Footer Sync**: Verify common components are consistent across all subpages.

---

## 🛠️ Execution Roadmap

1. **Step 1: Automated Scans**
   - Run `seo_checker.py`, `security_scan.py`, and `lighthouse_audit.py` in parallel.
2. **Step 2: Analysis & Fixes**
   - Review audit reports and apply fixes (e.g., compressing images, fixing broken meta tags).
3. **Step 3: Manual Verification**
   - Final walkthrough of the responsive UI.
4. **Step 4: Final Sign-off**
   - Comprehensive Orchestration Report.

---

## 🚦 Verification Criteria
- [ ] zero 404 links.
- [ ] SEO score > 90.
- [ ] Security scan results: Clean.
- [ ] Lighthouse Performance > 85.
