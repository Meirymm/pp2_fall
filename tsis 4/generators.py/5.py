def Mygenerator(n):
    while n >= 0:
        yield n
        n =n- 1

n = int(input())

for number in Mygenerator(n):
    print(number)