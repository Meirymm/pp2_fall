import re

#with open("row.txt", 'r', encoding="utf-8") as f:
    #data = f.read()
data="ab,abbb,abbbbb,acfgffgb,abb"
matches = re.findall(r"ab{2,3}", data)
print(matches)



