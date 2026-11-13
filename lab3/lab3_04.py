# Задача 4. A (вещ.), N > 0. Найти 1 + A + A² + A³ + ... + A^N.

A = float(input("A = "))
N = int(input("N = "))

total = 1.0            # первое слагаемое A^0 = 1
power = 1.0            # текущая степень A
for i in range(1, N + 1):
    power *= A         # A^i = A^(i-1) * A — не считаем A**i заново
    total += power

print("Сумма =", total)