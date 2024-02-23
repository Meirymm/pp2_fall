import re

with open("row.txt", 'r', encoding="utf-8") as f:
    data = f.read()
print(data)
matches = re.findall(r"аб*", data)
print(matches)

