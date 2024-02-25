import re
data=input()                              #"dddddSalemHHHHHello"
matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)