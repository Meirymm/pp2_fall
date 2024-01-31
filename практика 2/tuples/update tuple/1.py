#поменять
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)
#добавлять
x=("apple","banana","cherry")
y=list(x)
y.append("kiwi")
x=tuple(y)
print(x)


#удалить
#1
x=("apple","banana","cherry")
y=list(x)
y.remove("apple")
x=tuple(y)
print(x)
#2del
x=("apple","banana","cherry")
del("banana")
print(x)