# Лабораторная 9. Сортировка выбором
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):                  # i — граница отсортированной части
        min_idx = i                         # предполагаем, что a[i] — минимум
        for j in range(i + 1, n):           # ищем минимум в a[i+1..n-1]
            if a[j] < a[min_idx]:
                min_idx = j                 # нашли меньше — запомнили индекс
        # меняем местами, только если минимум не на своём месте
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]

        # печать после прохода: слева — отсортированная часть, справа — оставшаяся
        sorted_part = a[:i + 1]
        rest_part   = a[i + 1:]
        print(f"Проход {i + 1}: min={a[i]:>3} (индекс {min_idx})  →  {sorted_part} | {rest_part}")

    return a


# === Запуск ===
n = int(input("Размер массива: "))
a = list(map(int, input(f"Введите {n} элементов через пробел: ").split()))

print("Исходный массив:", a)
selection_sort(a)
print("Отсортированный массив:", a)