# Задача 5. 1 - A + A² - A³ + ... ± A^N. Без условного оператора!

A = float(input("A = "))
N = int(input("N = "))

total = 1.0
power = 1.0
sign = 1.0                 # множитель знака: 1 или -1
for i in range(1, N + 1):
    power *= A             # A^i
    sign = -sign           # переключаем знак: -1, +1, -1, ...
    total += sign * power

print("Сумма =", total)