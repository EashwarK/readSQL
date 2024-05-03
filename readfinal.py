import os

table_names = []
sqlcmnd = []
with open("sql_file.sql", "r") as file:
    content = file.read().strip() 
    sqllines = content.splitlines()
    for x in sqllines:
        sqlcmnd.append(x)

words = content.split()  
for i, word in enumerate(words):
    if word.upper() == "INTO":
        table_names.append(words[i + 1])
print(table_names)
for i in range(len(table_names)): 
    filename = table_names[i]+".sql"
    if os.path.exists(filename): 
        with open(filename, "r+") as f:
            content = f.read()
            if sqlcmnd[i] not in content:
                f.write(sqlcmnd[i]+'\n')
    else:
        with open(filename, "w") as f:
            f.write(sqlcmnd[i]+'\n')
