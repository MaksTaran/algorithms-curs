# Задача 5. Рекурсивный бинарный поиск в отсортированном массиве.

def binary_search(arr, target, lo, hi):
    if lo > hi:              # базовый случай: не нашли
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid           # нашли — возвращаем индекс
    if arr[mid] < target:    # ищем в правой половине
        return binary_search(arr, target, mid + 1, hi)
    return binary_search(arr, target, lo, mid - 1)   # в левой

# пример
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Искомое: "))
idx = binary_search(arr, target, 0, len(arr) - 1)
print("Индекс:", idx if idx != -1 else "не найден")