import os
import glob
import re

# Correct Header Templates
ROOT_HEADER = """    <header class="main-header">
        <div class="container header-content">
            <a href="index.html" class="logo">
                <span class="logo-icon">📦</span>
                <span class="logo-text">Freight<span class="highlight">Class</span>Calc</span>
            </a>
            <nav class="main-nav">
                <ul>
                    <li><a href="index.html">Calculator</a></li>
                    <li><a href="blog/index.html">Blog</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>"""

BLOG_HEADER = """    <header class="main-header">
        <div class="container header-content">
            <a href="../index.html" class="logo">
                <span class="logo-icon">📦</span>
                <span class="logo-text">Freight<span class="highlight">Class</span>Calc</span>
            </a>
            <nav class="main-nav">
                <ul>
                    <li><a href="../index.html">Calculator</a></li>
                    <li><a href="../blog/index.html">Blog</a></li>
                    <li><a href="../contact.html">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>"""

def replace_header(file_path, new_header):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to capture the header block
    # It usually starts with <header class="main-header"> and ends with </header>
    # We used default indentation in the template, so strictly replacing might work if indentation matches.
    # But regex is safer for varying indentation.
    
    pattern = re.compile(r'<header class="main-header">.*?</header>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_header, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")
    else:
        print(f"Header not found in: {file_path}")

# 1. Update Root Files
root_files = ['d:/Fright/index.html', 'd:/Fright/contact.html', 'd:/Fright/privacy.html', 'd:/Fright/terms.html']
for file_path in root_files:
    if os.path.exists(file_path):
        replace_header(file_path, ROOT_HEADER)

# 2. Update Blog Files
blog_files = glob.glob('d:/Fright/blog/*.html')
for file_path in blog_files:
    replace_header(file_path, BLOG_HEADER)

print("Header update complete.")
