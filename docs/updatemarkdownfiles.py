import os
import re
from pathlib import Path 

glob_path = Path(r"D:\Dev\000wiki\docs")

file_list = [pp.name for pp in glob_path.glob("**/*.md")]
file_dict = {pp.name:pp.name.replace(".md", "").replace("-", " ").title() for pp in glob_path.glob("**/*.md")}
#print(file_dict)
def multiple_replace(text, replacements):
    pattern = re.compile("|".join(map(re.escape, replacements.keys())))
    return pattern.sub(lambda match: replacements[match.group(0)], text)

def content_list_string():
    replacements = {
        "Csharp": "C#",
        "Dotnet": ".NET"
    }
    mdStr = "# Content List\n\n"
    for md_file in file_dict:
        md_title = md_title = multiple_replace(file_dict[md_file], replacements).title()
        mdStr = mdStr + f"- [{md_title}]({md_file})\n"

    return mdStr


os.remove(r"D:\Dev\000wiki\docs\content-list.md")
f = open(r"D:\Dev\000wiki\docs\content-list.md", "a")
f.write(content_list_string())
f.close()

