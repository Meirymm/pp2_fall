#1 внутри функции работает
def myfunc(n):
    return lambda a:a*n
x=myfunc(2)
print(x(11))
#2 внутри функции выполняем 2 условии
def myfunc(n):
    return lambda a:a*n
x=myfunc(2)
y=myfunc(4)
print(x(11))
print(y(13))