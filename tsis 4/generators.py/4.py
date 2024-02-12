def squares(a, b):
    for i in range(a, b+1):
        yield i**2
for number in squares(2, 10):
    print(number)