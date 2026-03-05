import os,re

for root,dirs,files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path=os.path.join(root,file)

            with open(path,"r",encoding="utf-8") as f:
                code=f.read()

            # fix db = get_db()
    return db["collection"]
            code=re.sub(
                r'return\s+db\["([^"]+)"\]',
                r'db = get_db()\n    db = get_db()
    return db["\1"]',
                code
            )

            with open(path,"w",encoding="utf-8") as f:
                f.write(code)

print("ALL DB ERRORS FIXED")
