import os
import shutil
import re

# Configuration
BRAIN_DIR = r"C:/Users/Tanveer/.gemini/antigravity/brain/b2bf2b13-d655-4404-933f-06364518e6a9"
BLOG_DIR = r"d:/Fright/blog"
IMG_DIR = os.path.join(BLOG_DIR, "img")

# Mappings (Filename in Brain -> Targeted Article and Clean Name)
IMAGE_MAPPING = {
    "ltl_quotes_hero_png_1769776768470.png": "article-1-ltl-quotes.png",
    "nmfc_vs_density_comparison_png_1769776783727.png": "article-2-nmfc-density.png",
    "overweight_scale_alert_png_1769776806154.png": "article-3-avoid-fees.png",
    "logistics_software_hologram_png_1769777008788.png": "article-4-tms-software.png",
    "ltl_vs_ftl_aerial_png_1769777027584.png": "article-5-ltl-vs-ftl.png",
    "dim_weight_logic_png_1769777043154.png": "article-6-dim-weight.png",
    "hazmat_drum_labels_png_1769777060457.png": "article-7-hazmat.png",
    # Article 8 failed
    "pallet_do_vs_dont_png_1769776918777.png": "article-9-pallet-packing.png",
    "cargo_insurance_shield_png_1769776935669.png": "article-10-insurance.png"
}

HTML_MAPPING = {
    "article-1-ltl-quotes.png": "ltl-freight-quotes-guide.html",
    "article-2-nmfc-density.png": "nmfc-vs-density.html",
    "article-3-avoid-fees.png": "avoid-reclass-fees.html",
    "article-4-tms-software.png": "top-logistics-software.html",
    "article-5-ltl-vs-ftl.png": "ltl-vs-ftl.html",
    "article-6-dim-weight.png": "dimensional-weight-guide.html",
    "article-7-hazmat.png": "hazmat-freight-guide.html",
    "article-9-pallet-packing.png": "pallet-optimization.html",
    "article-10-insurance.png": "freight-insurance.html"
}

def main():
    # 1. Create img directory
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)
        print(f"Created directory: {IMG_DIR}")

    # 2. Copy and rename images
    for old_name, new_name in IMAGE_MAPPING.items():
        src = os.path.join(BRAIN_DIR, old_name)
        dst = os.path.join(IMG_DIR, new_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied: {old_name} -> {new_name}")
        else:
            print(f"Warning: {src} not found.")

    # 3. Update Individual Articles (Hero Images)
    for img_name, html_file in HTML_MAPPING.items():
        file_path = os.path.join(BLOG_DIR, html_file)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find any img tag with src starting with ../ (which I mistakenly added) or placeholders
            content = re.sub(r'<img src="\.\./[^"]+\.png"', f'<img src="img/{img_name}"', content)
            # Just in case some are still placeholders
            # (Note: This is a bit broad but safe for this batch)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated hero image in: {html_file}")

    # 4. Update Blog Index (Thumbnails)
    index_path = os.path.join(BLOG_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_content = f.read()
        
        for img_name, html_file in HTML_MAPPING.items():
            # Find the link to the article and the src in the next few lines
            # Pattern: look for href="html_file" and then the first src=
            pattern = rf'(href="{html_file}"[^>]*>.*?src=")([^"]+)(")'
            index_content = re.sub(pattern, rf'\1img/{img_name}\3', index_content, flags=re.DOTALL)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"Updated index thumbnails.")

if __name__ == "__main__":
    main()
