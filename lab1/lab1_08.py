# Задача 8. Три точки A, B, C на оси, C между A и B.
# Найти произведение длин отрезков AC и BC.

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

AC = abs(C - A)        # длина AC
BC = abs(C - B)        # длина BC

print("|AC| * |BC| =", AC * BC)