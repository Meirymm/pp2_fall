def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)

"""
У нас есть список чисел, называемых числами.
Мы используем функцию фильтра вместе с лямбда-функцией для фильтрации простых чисел из списка.
Лямбда-функция берет каждое число из списка и передает его функции is_prime.
Если результат равен True, номер включается в отфильтрованный список."""