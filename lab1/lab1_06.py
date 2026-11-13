# Задача 6. Найти расстояние между точками (x1, y1) и (x2, y2).
# Формула: sqrt((x2-x1)^2 + (y2-y1)^2).

import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Расстояние =", d)