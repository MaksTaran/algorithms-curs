# Задача 8. M, N чётные. Поменять местами левую верхнюю и правую нижнюю четверти.

M = int(input("M (чётное) = "))
N = int(input("N (чётное) = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

h = M // 2                 # половина по строкам
w = N // 2                 # половина по столбцам

# Обходим левую верхнюю четверть и меняем её с соответствующей клеткой правой нижней
for i in range(h):
    for j in range(w):
        a[i][j], a[i + h][j + w] = a[i + h][j + w], a[i][j]

print("Результат:")
for row in a:
    print(*row)