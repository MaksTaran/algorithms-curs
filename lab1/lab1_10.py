# Задача 10. Даны три вершины треугольника.
# Найти периметр и площадь (площадь — по формуле Герона).

import math

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

# длины сторон через расстояние между соответствующими вершинами
a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

p = a + b + c              # периметр
pp = p / 2                  # полупериметр для формулы Герона

S = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))   # площадь

print("Периметр P =", p)
print("Площадь S =", S)