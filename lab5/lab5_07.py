# Задача 7. Проверить, образуют ли элементы арифметическую прогрессию.
# Вывести разность, если да; иначе 0.

N = int(input("N = "))
a = list(map(int, input(f"Введите {N} элементов: ").split()))

diff = a[1] - a[0]           # предполагаемая разность
is_ap = True
for i in range(2, N):
    if a[i] - a[i - 1] != diff:
        is_ap = False
        break

print(diff if is_ap else 0)