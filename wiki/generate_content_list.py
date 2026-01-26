import os
import re
from pathlib import Path

docs_dir = Path(r"e:\Dev\Personal\Wiki\maulanaaghnii.github.io\docs")
md_files = sorted(list(docs_dir.glob("*.md")))

def get_title(file_path):
    try:
        content = file_path.read_text(encoding="utf-8")
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except:
        pass
    # Fallback to title case of filename
    return file_path.stem.replace("-", " ").title()

categories = {
    "General": ["index.md", "homepage.md", "content-list.md", "cheat-sheets.md", "tips-and-tricks.md", "underrated-tools.md", "when-you-bored.md"],
    "C# Programming": [],
    ".NET": [],
    "Docker": [],
    "Ubuntu": [],
    "Infrastructure & Tools": ["wsl.md", "chocolatey.md", "github.md", "consul.md", "consule-docker.md"],
    "Miscellaneous": ["dicoding-machine-learning.md", "material-mkdocs-yml.md"]
}

for f in md_files:
    name = f.name
    if name in [item for sublist in categories.values() for item in sublist]:
        continue
    
    if name.startswith("csharp"):
        categories["C# Programming"].append(name)
    elif name.startswith("dotnet") or name.startswith("aspnet") or name == "entity-framework-core.md":
        categories[".NET"].append(name)
    elif name.startswith("docker"):
        categories["Docker"].append(name)
    elif name.startswith("ubuntu"):
        categories["Ubuntu"].append(name)
    elif name.startswith("kubernetes"):
        if "Infrastructure & Tools" not in categories: categories["Infrastructure & Tools"] = []
        categories["Infrastructure & Tools"].append(name)
    elif name in ["mysql.md", "postgresql.md"]:
        if "Databases" not in categories: categories["Databases"] = []
        categories["Databases"].append(name)
    else:
        categories["Miscellaneous"].append(name)

with open(docs_dir / "content-list.md", "w", encoding="utf-8") as f:
    f.write("# Content List\n\n")
    for cat, files in categories.items():
        if not files: continue
        f.write(f"## {cat}\n")
        for file_name in sorted(files):
            title = get_title(docs_dir / file_name)
            f.write(f"- [{title}]({file_name})\n")
        f.write("\n")

print("Content list updated.")
