# 🖼️ Image Optimization & Performance Plan

The current blog images are significantly oversized (~1MB each), which severely impacts Mobile Lighthouse scores and Core Web Vitals despite lazy-loading. This plan outlines the technical squad's approach to shrinking the 25MB+ image payload to under 3-5MB total.

## 🤖 Squad Assembly

| Agent | Focus Area | Responsibility |
|-------|------------|----------------|
| `project-planner` | Coordination | Strategy and verification tracking |
| `performance-optimizer` | Compression | Bulk conversion to WebP and high-compression PNG |
| `seo-specialist` | HTML Update | Modernizing `<picture>` tags or switching to `.webp` |
| `test-engineer` | Visual QA | Ensuring "Nano Banana" details are preserved after lossy compression |

---

## 📋 Optimization Strategy

### 1. Analysis & Benchmarking
- [ ] List all images in `blog/img/` and record their current sizes.
- [ ] Determine the optimal target size (aiming for <150KB per image).

### 2. Implementation: The Dual-Format Push (`performance-optimizer`)
> [!IMPORTANT]
> Since this is 2026, we will prioritize **WebP** as the primary format, which typically offers 3x reduction in size with better quality than JPEG.

- [ ] **Phase A**: Compress original PNGs using `Pillow` (Optimized PNG) for maximum compatibility.
- [ ] **Phase B**: Generate **WebP** versions of all 30 images.
- [ ] **Comparison**: Verify that the "Nano" technical details (text on screens, labels) remain legible.

### 3. Integration: Source Updates (`seo-specialist`)
- [ ] Update `blog/index.html` to point to `.webp` files.
- [ ] Update individual article files (Articles 1-30) meta tags and body images.
- [ ] (Optional) Implement `<picture>` tags with WebP/PNG alternatives if legacy support is a hard requirement.

### 4. Verification (`test-engineer`)
- [ ] Automated check for broken 404 image links.
- [ ] Final Lighthouse mobile benchmark on Article 28 (the heaviest page).

---

## 🛠️ Tools Used
- `python` with `PIL (Pillow)` for image processing.
- `seo_checker.py` to ensure meta tag integrity after changes.

## 🚦 Socratic Gate
1. **Format Choice**: Since WebP is natively supported by everything in 2026, do you want to switch **entirely** to WebP to save dev complexity, or keep PNG fallbacks?
2. **Lossy Tolerance**: May I apply "Adaptive Quality" (80%)? This usually reduces size by 70% without visible text blur.
