# Лабораторная 10. Бинарный поиск в отсортированном массиве.
def binary_search(a, target):
    left = 0
    right = len(a) - 1
    step = 0

    while left <= right:                          # диапазон поиска не пуст
        step += 1
        mid = (left + right) // 2                 # середина диапазона
        current = a[mid]

        # печать текущего шага: диапазон, mid, значение
        print(f"Шаг {step}: диапазон [{left}..{right}], mid={mid}, a[{mid}]={current}", end="")

        if current == target:
            print("  → нашли!")
            return mid
        elif current > target:
            print(f"  → {current} > {target}, ищем в левой половине")
            right = mid - 1
        else:
            print(f"  → {current} < {target}, ищем в правой половине")
            left = mid + 1

    return -1                                     # не нашли



n = int(input("Размер массива: "))
a = list(map(int, input(f"Введите {n} элементов ЧЕРЕЗ ПРОБЕЛ (отсортированы по возрастанию): ").split()))

# если забыли отсортировать — сортируем
if a != sorted(a):
    print("Массив не отсортирован — сортируем:", sorted(a))
    a = sorted(a)

target = int(input("Искомый элемент: "))

print(f"\nМассив: {a}")
print(f"Ищем: {target}\n")

idx = binary_search(a, target)
if idx != -1:
    print(f"\nЭлемент найден по индексу {idx} (это {idx + 1}-й элемент, если считать с 1).")
else:
    print(f"\nЭлемент {target} не найден в массиве.")