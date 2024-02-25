import re
#with open("row.txt", 'r' ) as f:
 #  data = f.read()
data="hfhdfab,ahjfvfhjhb,akdkb"
matches = re.findall(r"a.*b$", data)
print(matches)