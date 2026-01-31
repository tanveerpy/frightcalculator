import os
import shutil
import re

# Configuration
BRAIN_DIR = r"C:/Users/Tanveer/.gemini/antigravity/brain/b2bf2b13-d655-4404-933f-06364518e6a9"
BLOG_DIR = r"d:/Fright/blog"
IMG_DIR = os.path.join(BLOG_DIR, "img")

# Mappings (Filename in Brain -> Targeted Article and Clean Name)
IMAGE_MAPPING = {
    "nano_banana_ltl_quotes_v2_png_1769779428845.png": "article-1-ltl-quotes.png",
    "nano_banana_nmfc_v_density_png_1769779632780.png": "article-2-nmfc-density.png",
    "nano_banana_avoid_fees_png_1769779661391.png": "article-3-avoid-fees.png",
    "nano_banana_dim_weight_v2_png_1769779450232.png": "article-6-dim-weight.png",
    "nano_banana_hazmat_v2_png_1769779473000.png": "article-7-hazmat.png"
}

HTML_MAPPING = {
    "article-1-ltl-quotes.png": "ltl-freight-quotes-guide.html",
    "article-2-nmfc-density.png": "nmfc-vs-density.html",
    "article-3-avoid-fees.png": "avoid-reclass-fees.html",
    "article-6-dim-weight.png": "dimensional-weight-guide.html",
    "article-7-hazmat.png": "hazmat-freight-guide.html"
}

def main():
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)

    # 1. Copy successful images
    for old_name, new_name in IMAGE_MAPPING.items():
        src = os.path.join(BRAIN_DIR, old_name)
        dst = os.path.join(IMG_DIR, new_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Deployed: {new_name}")

    # 2. Update Article Pages
    for img_name, html_file in HTML_MAPPING.items():
        file_path = os.path.join(BLOG_DIR, html_file)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Simple replacement for the img src in the hero section
            # Looking for any img src="img/..." or earlier placeholders
            content = re.sub(r'<img src="(?:img/|../)?[^"]+\.png"', f'<img src="img/{img_name}"', content, count=1)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated Article: {html_file}")

    # 3. Update Index
    index_path = os.path.join(BLOG_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_content = f.read()
        for img_name, html_file in HTML_MAPPING.items():
            pattern = rf'(href="{html_file}"[^>]*>.*?src=")([^"]+)(")'
            index_content = re.sub(pattern, rf'\1img/{img_name}\3', index_content, flags=re.DOTALL)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print("Updated Index Thumbnails.")

if __name__ == "__main__":
    main()
