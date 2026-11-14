# Лабораторная 7. Сортировка пузырьком.
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):                 # номер прохода
        swapped = False                    # были ли обмены
        for j in range(n - 1 - i):         # последние i элементов уже на месте
            if a[j] > a[j + 1]:            # неправильный порядок
                a[j], a[j + 1] = a[j + 1], a[j]   # меняем местами
                swapped = True
        print(f"Проход {i + 1}: {a}")
        if not swapped:                    # обменов не было — уже отсортирован
            break
    return a

n = int(input("Размер массива: "))
a = list(map(int, input(f"Введите {n} элементов через пробел: ").split()))

print("Исходный массив:", a)
bubble_sort(a)
print("Отсортированный массив:", a)