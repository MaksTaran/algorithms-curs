# Задача 1. Рекурсивный факториал: n! = n * (n-1)!

def factorial(n):
    if n == 0 or n == 1:     # базовый случай: 0! = 1! = 1
        return 1
    return n * factorial(n - 1)   # рекурсивный случай

n = int(input("n = "))
print(f"{n}! =", factorial(n))