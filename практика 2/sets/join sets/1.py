#1 union method
"""set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3=set1.union(set2)
print(set3)"""

#2 update method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set)

#3 intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#4 symmetric difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)