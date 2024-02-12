#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def is_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = is_prime(numbers)
print("Prime numbers:")
print(prime_numbers)


