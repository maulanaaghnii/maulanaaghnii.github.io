import os
import re
from pathlib import Path

docs_dir = Path(r"e:\Dev\Personal\Wiki\maulanaaghnii.github.io\docs")
md_files = list(docs_dir.glob("*.md"))

all_links = set()
for md_file in md_files:
    try:
        content = md_file.read_text(encoding="utf-8")
        links = re.findall(r"\[.+?\]\(([a-zA-Z0-9_-]+\.md)\)", content)
        for link in links:
            all_links.add(link)
    except Exception:
        pass

existing_files = {f.name for f in md_files}
missing_links = sorted([link for link in all_links if link not in existing_files])

with open("missing_final.txt", "w", encoding="utf-8") as f:
    f.write("Missing files:\n")
    for missing in missing_links:
        f.write(missing + "\n")
