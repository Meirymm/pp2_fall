import re
data=input()        #"ab,abbb,abbbbb,acfgffgb,abb"
matches = re.findall(r"ab{2,3}", data)
print(matches)



