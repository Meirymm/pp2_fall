import re
#with open("row.txt", 'r' ) as f:
 #data = f.read()
data="This is,my home."
matches  = re.sub('[., ]',':', data)
print(matches)