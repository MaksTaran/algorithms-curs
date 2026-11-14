# Задача 4. В каждом столбце — сколько элементов больше среднего по столбцу.

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

for j in range(N):
    col = [a[i][j] for i in range(M)]   # «вытаскиваем» столбец в отдельный список
    avg = sum(col) / M
    count = 0
    for x in col:
        if x > avg:
            count += 1
    print(f"Столбец {j+1}: среднее = {avg:.2f}, больше среднего: {count}")