#1:arithmetic operators
x=10
y=5
print(x+y)
print(x*y)
print(x-y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

#2:assignment operators(присваивания)
x=10
print(x)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x&=3
print(x)
x^=3
print(x)

#3: comparison operetors(сравнение)
x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#4 logical operators
x=7
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x>5 and x<10))

#5 identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

#6 membership operators
x=[5,4,6,8,7]
print(5 in x)

#7 bitwise operators
x=6
y=3
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<2)
print(x>>2)