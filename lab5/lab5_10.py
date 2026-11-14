# Задача 10. Массив содержит ровно два одинаковых элемента.
# Найти их номера и вывести в порядке возрастания.

N = int(input("N = "))
a = list(map(int, input(f"Введите {N} элементов: ").split()))

# Для каждого i ищем j > i, где a[j] == a[i].
# Как только нашли — это и есть пара.
pair = None
for i in range(N):
    for j in range(i + 1, N):
        if a[i] == a[j]:
            pair = (i, j)
            break
    if pair:
        break

if pair:
    print("Номера одинаковых элементов:", pair[0] + 1, "и", pair[1] + 1)  # +1 → 1-based
else:
    print("Одинаковых элементов нет")