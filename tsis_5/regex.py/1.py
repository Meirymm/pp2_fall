import re
#encoding="utf-8" for read russian text
#with open("row.txt", "r",encoding="utf-8") as file:
 #   data = file.read()
data="a,abb,acc,abbbb"
matches = re.findall(r"ab*", data)
print(matches)

