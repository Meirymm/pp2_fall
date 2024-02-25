import re
data=input()              #"hfhdfab,ahjfvfhjhb,akdkb"
matches = re.findall(r"a.*b$", data)
print(matches)