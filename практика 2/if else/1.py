#1
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#2 elif- это способ выражения Python "если предыдущие условия не были выполнены, попробуйте выполнить это условие".
a=33
b=33
if (a>b) :
    print("a is greater than b")
elif (a==b):
    print("a and b are equal")

#3 else улавливает все, что не улавливается предыдущими условиями.
a=200
b=33
if b>a:
    print("b is greater than a")
elif b==a:
    print("b and a are equal")
else:
    print("a is greater than b")
    
#4 if we have only one operator we can write in ine line
a=200
b=45
if a>b:print("a is greater than b")

#5
a=2
b=330
print("A") if a>b else print("B")

#6
a = 200
b = 33
c = 500
if a > b and c < a:
  print("Both conditions are True")
  
#7
a = 200
b = 33
c = 500
if a > b or c < a:
  print("Both conditions are True")

#8
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#9
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
#10 pass for escape error if we have empty if
a = 33
b = 200

if b > a:
  pass