import re

#with open("row.txt", 'r' ) as f:
 #   data = f.read()
data="salem_alem,men_sabaktamyn_uide_emes"
matches = re.findall(r"[a-z]+_[a-z]+", data)
print(matches)