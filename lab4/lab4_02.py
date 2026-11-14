# Задача 2. Рекурсивное n-е число Фибоначчи: F(n) = F(n-1) + F(n-2).

def fib(n):
    if n <= 1:               # базовые случаи: F(0)=0, F(1)=1
        return n
    return fib(n - 1) + fib(n - 2)   # два рекурсивных вызова

n = int(input("n = "))
print(f"F({n}) =", fib(n))