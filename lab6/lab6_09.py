# Задача 9. Упорядочить строки так, чтобы их первые элементы возрастали.

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)

# сортировка пузырьком по первому элементу строки
for i in range(M - 1):
    for j in range(M - 1 - i):
        if a[j][0] > a[j + 1][0]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Результат:")
for row in a:
    print(*row)