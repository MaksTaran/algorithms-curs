# Задача 5. Номер ПЕРВОГО столбца, в котором все элементы — нечётные.
# Если такого нет — вывести 0.

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

found = 0
for j in range(N):
    all_odd = True
    for i in range(M):
        if a[i][j] % 2 == 0:       # нашли чётный — столбец не подходит
            all_odd = False
            break
    if all_odd:
        found = j + 1              # +1 → 1-based
        break                      # первый же найденный — ответ

print(found)