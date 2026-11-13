# Задача 2. Даны три числа. Найти сумму двух наибольших.
# Идея: сумма всех минус наименьшее = сумма двух наибольших.

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

total = a + b + c
smallest = min(a, b, c)
print("Сумма двух наибольших =", total - smallest)