import re

#with open("row.txt", 'r' ) as f:
 #   data = f.read()
data="dddddSalemHHHHHello"
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)