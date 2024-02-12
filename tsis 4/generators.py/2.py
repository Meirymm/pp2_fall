def Mygenerator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield str(i)


number = Mygenerator(10)
print(",".join(number))