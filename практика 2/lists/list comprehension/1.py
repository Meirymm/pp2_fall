#1
"""fruits=["apple","banana","cherry","kiwi","mango"]
new_list=[]
for x in fruits:
    if "a" in x:
        new_list.append(x)
print(new_list)"""
#2
"""fruits=["apple","banana","cherry","kiwi","mango"]
new_list=[x for x in fruits if "a" in x]
print(new_list)"""
#3
fruits=["apple","banana","cherry","kiwi","mango"]
new_list=[x for x in fruits if x!="apple"]
print(new_list)