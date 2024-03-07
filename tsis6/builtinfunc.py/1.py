def multiplication(n):
    num = 1
    for i in n:
        num *= i
    return num
print(multiplication((1, 2, 3)))