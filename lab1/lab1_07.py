# Задача 7. Три точки A, B, C на числовой оси.
# Найти длины отрезков AC и BC и их сумму.
# Длина отрезка на оси = модуль разности координат.

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

AC = abs(C - A)        # длина AC
BC = abs(C - B)        # длина BC

print("|AC| =", AC)
print("|BC| =", BC)
print("|AC| + |BC| =", AC + BC)