def square_generator(N):
    for i in range(N+1):
        yield i ** 2
for number in square_generator(10):
    print(number)

