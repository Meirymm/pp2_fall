import re
#encoding="utf-8" for read russian text
with open("row.txt") as file:
    data = file.read()

matches = re.findall(r"аb*", data)
print(matches)

