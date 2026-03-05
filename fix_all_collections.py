import os
import re

ROOT = "."

pattern = r'(\w+)#collection_removed\s*=\s*db\["([^"]+)"\]'

for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            def replace(match):
                name = match.group(1)
                collection = match.group(2)

                return f'''
def get_{name}_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["{collection}"]
'''

            new_content = re.sub(pattern, replace, content)

            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

print("ALL COLLECTION ERRORS FIXED")
