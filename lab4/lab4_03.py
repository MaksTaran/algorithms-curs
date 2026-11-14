# Задача 3. Рекурсивно вычислить x^n.

def power(x, n):
    if n == 0:               # базовый случай: x^0 = 1
        return 1
    return x * power(x, n - 1)   # x^n = x * x^(n-1)

x = float(input("x = "))
n = int(input("n = "))
print(f"{x}^{n} =", power(x, n))