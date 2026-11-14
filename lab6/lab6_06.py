# Задача 6. В каждой строке поменять местами min и max элементы.

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

for i in range(M):
    row = a[i]
    min_idx = row.index(min(row))  # индекс минимального
    max_idx = row.index(max(row))  # индекс максимального
    # кортежное присваивание меняет местами
    row[min_idx], row[max_idx] = row[max_idx], row[min_idx]

print("Результат:")
for row in a:
    print(*row)