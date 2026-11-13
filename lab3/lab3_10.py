# Задача 10. A, B — целые положительные. НОД через алгоритм Евклида.

A = int(input("A = "))
B = int(input("B = "))

a = A
b = B
while b != 0:
    a, b = b, a % b        # b → a, остаток a % b → b

print("НОД =", a)