# Задача 4. Вывести: A1, AN, A2, AN-1, A3, AN-2, ...
# (чередование: первый, последний, второй, предпоследний, ...)

N = int(input("N = "))
a = list(map(int, input(f"Введите {N} элементов через пробел: ").split()))

# Два указателя: left идёт с начала, right — с конца.
left = 0
right = N - 1
result = []
while left <= right:
    result.append(a[left])
    if left != right:        # чтобы не задвоить средний элемент
        result.append(a[right])
    left += 1
    right -= 1

print(result)