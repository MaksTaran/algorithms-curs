# Задача 1. Квадратная матрица M×M (M нечётное).
# Обход по спирали ПРОТИВ часовой стрелки, начиная с a[0][0]:
# первый столбец ↓, последняя строка →, последний столбец ↑,
# первая строка ←, затем внутреннее кольцо. Центр — последним.

M = int(input("M (нечётное) = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

# Границы текущего «кольца»
top, bottom, left, right = 0, M - 1, 0, M - 1
result = []

while top <= bottom and left <= right:
    # 1) левый столбец сверху вниз
    for i in range(top, bottom + 1):
        result.append(a[i][left])
    left += 1
    if left > right: break

    # 2) нижняя строка слева направо (начиная с left, чтобы не задвоить угол)
    for j in range(left, right + 1):
        result.append(a[bottom][j])
    bottom -= 1
    if top > bottom: break

    # 3) правый столбец снизу вверх
    for i in range(bottom, top - 1, -1):
        result.append(a[i][right])
    right -= 1
    if left > right: break

    # 4) верхняя строка справа налево
    for j in range(right, left - 1, -1):
        result.append(a[top][j])
    top += 1

print(*result)