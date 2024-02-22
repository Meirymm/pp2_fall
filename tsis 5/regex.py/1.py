'''import re
txt=str(input())
x=re.findall(r"ab*",txt)

print(x)'''
import re

def match_string(string):
    pattern = r'ab*'
    if re.match(pattern, string):
        return True
    else:
        return False
match_string(str(input()))

# Test the function
