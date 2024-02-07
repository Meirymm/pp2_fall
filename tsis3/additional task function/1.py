def calculate_factorial(num):
    if num == 1:
        return num
    else:
        return num * calculate_factorial(num - 1)
num2 = int(input())
print(calculate_factorial(num2))