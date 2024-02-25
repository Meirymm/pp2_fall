import re

def upper_case(a: str):
    return re.findall("[A-Z][^A-Z]*", a)

a= input()   #menKbtudaokumynZhanePythonuirenudemin
print(upper_case(a))
