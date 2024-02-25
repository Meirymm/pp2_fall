import re
data=input()              #"This is,my home."
matches  = re.sub('[., ]',':', data)
print(matches)