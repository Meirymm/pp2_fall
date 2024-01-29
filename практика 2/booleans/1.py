#1
print(10>9)
print(10==9)
print(10<9)

#2
a=200
b=33
if b>a:
    print("b greater,than a")
else:
    print("b is not greater than a")
    
#3
x="Hello"
y=0
z=["apple","cherry","banana"]
print(bool(x))
print(bool(y))
print(bool(z))

#4 Значении которые равны на false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#5 function __len__ return false too
class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj))
        
#6 i can create function,which can return true
def myfunction():
    return True
print(myfunction())

#7
def myfunction():
    return True
if myfunction():
    print("Yes")
else:
    print("NO!")
    
#8 In Python we have more functions that return a boolean value
#Foer example:isinstance
x=200
print(isinstance(x,int))
