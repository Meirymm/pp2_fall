import re

def tab_case(a: str):
    words = re.findall("[A-Z][^A-Z]*", a)
    return ' '.join(words)

a = input()     #SalemAlemMenMeyrim
print(tab_case(a))