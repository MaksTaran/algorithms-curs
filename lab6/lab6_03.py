# Задача 3. Номер столбца с наименьшим произведением элементов
# и само наименьшее произведение.

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

best_product = None
best_col = -1
for j in range(N):
    p = 1
    for i in range(M):
        p *= a[i][j]
    if best_product is None or p < best_product:
        best_product = p
        best_col = j

print("Номер столбца (1-based):", best_col + 1)
print("Наименьшее произведение:", best_product)