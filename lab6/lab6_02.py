# Задача 2. Сумма и произведение элементов K-й строки (1 ≤ K ≤ M).

M = int(input("M = "))
N = int(input("N = "))
a = []
for i in range(M):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    a.append(row)
K = int(input("K (1..M) = "))

row_k = a[K - 1]           # строка с номером K → индекс K-1

s = sum(row_k)             # сумма — встроенная функция
p = 1                      # нейтральный элемент для произведения
for x in row_k:
    p *= x

print("Сумма:", s)
print("Произведение:", p)