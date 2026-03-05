import os
import re

ROOT_DIR = "."

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # remove global # db removed
            content = re.sub(r"db\s*=\s*get_db\(\)", "# db removed", content)

            # remove global collections
            content = re.sub(r"\w+_collection\s*=\s*db\[[^\]]+\]", "# collection removed", content)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

print("✅ Database global usage cleaned")