# Задача 7. Поменять местами столбцы, содержащие min и max матрицы.

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

# ищем min, max и запоминаем их столбцы
min_val = a[0][0]
max_val = a[0][0]
min_col = 0
max_col = 0
for i in range(M):
    for j in range(N):
        if a[i][j] < min_val:
            min_val = a[i][j]
            min_col = j
        if a[i][j] > max_val:
            max_val = a[i][j]
            max_col = j

if min_col != max_col:              # если это разные столбцы
    for i in range(M):
        a[i][min_col], a[i][max_col] = a[i][max_col], a[i][min_col]

print("Результат:")
for row in a:
    print(*row)