# Задача 3. Даны три точки A, B, C на плоскости.
# Определить, какая из точек B или C ближе к A, и вывести её и расстояние.

import math

ax = float(input("Ax = "))
ay = float(input("Ay = "))
bx = float(input("Bx = "))
by = float(input("By = "))
cx = float(input("Cx = "))
cy = float(input("Cy = "))

# расстояние от A до B и от A до C (формула из lab1_06)
dAB = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
dAC = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)

if dAB < dAC:
    print("Точка B ближе, расстояние =", dAB)
elif dAC < dAB:
    print("Точка C ближе, расстояние =", dAC)
else:
    print("B и C на одинаковом расстоянии:", dAB)