# Задача 10. Сумма элементов каждой диагонали, параллельной главной.
# Диагональ задаётся разностью i - j = offset.
# offset меняется от -(M-1) до (M-1): -(M-1) — правый верхний угол (1 элемент),
# M-1 — левый нижний угол (1 элемент). Начинаем с одноэлементной.

M = int(input("M = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

for offset in range(-(M - 1), M):
    total = 0
    count = 0
    for i in range(M):
        j = i - offset          # из условия i - j = offset
        if 0 <= j < M:          # элемент в пределах матрицы
            total += a[i][j]
            count += 1
    # подпись: выше/главная/ниже главной
    if offset < 0:
        name = f"выше главной, сдвиг {abs(offset)}"
    elif offset == 0:
        name = "главная диагональ"
    else:
        name = f"ниже главной, сдвиг {offset}"
    print(f"{name} (элементов={count}): сумма = {total}")