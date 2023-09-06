import sqlparse

# with open("标品堡垒-DDL-2023714135601.sql", 'r', encoding="UTF-8") as f:
# with open("sqlserver.sql", 'r', encoding="UTF-8") as f:
with open("mongodb.sql", 'r', encoding="UTF-8") as f:
# with open("mysql.sql", 'r', encoding="UTF-8") as f:
    raw = f.read()
    statements = sqlparse.split(raw)
    for stat in statements:
        print(f'---------\n{stat}')
        parsed = sqlparse.parse(stat)
        print(parsed[0].tokens)