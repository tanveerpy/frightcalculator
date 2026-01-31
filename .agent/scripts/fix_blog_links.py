import re

file_path = r'd:/Fright/blog/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: find the img, then find the link in the h2, and wrap the img.
# Since regex across multiple lines is tricky, let's iterate through article blocks if possible.
# But regex with dotall is easier for this specific structure.

# Structure:
# <article class="blog-card">
#     <img src="..." ...>
#     <div class="blog-content">
#         ...
#         <h2 class="blog-title"><a href="TARGET_URL">...</a></h2>

def replacement(match):
    full_block = match.group(0)
    img_tag = match.group(1)
    target_url = match.group(2)
    
    # Check if already wrapped
    if '<a href="' in full_block and full_block.find('<a href="') < full_block.find('<img'):
        return full_block

    new_img_block = f'<a href="{target_url}" class="blog-img-link">{img_tag}</a>'
    return full_block.replace(img_tag, new_img_block)

# Regex to match the article block up to the H2 link
# We capture the img tag (group 1) and the href (group 2)
pattern = re.compile(r'(<img src="[^"]+" alt="[^"]+" class="blog-img">)\s*<div class="blog-content">.*?<h2 class="blog-title"><a href="([^"]+)">', re.DOTALL)

# This regex is a bit dangerous if it over-matches. 
# Let's try a safer approach: Parse the text line by line or split by <article>

parts = content.split('<article class="blog-card">')
new_content = parts[0]

for part in parts[1:]:
    # Each part starts with the inside of the article
    # Find the img tag
    img_match = re.search(r'<img src="[^"]+" alt="[^"]+" class="blog-img">', part)
    # Find the href
    link_match = re.search(r'<h2 class="blog-title"><a href="([^"]+)">', part)
    
    if img_match and link_match:
        img_tag = img_match.group(0)
        url = link_match.group(1)
        
        # reconstruct the part with wrapped img
        new_part = part.replace(img_tag, f'<a href="{url}" class="blog-img-link" title="Read Article">{img_tag}</a>')
        new_content += '<article class="blog-card">' + new_part
    else:
        new_content += '<article class="blog-card">' + part

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated blog images to be clickable.")
