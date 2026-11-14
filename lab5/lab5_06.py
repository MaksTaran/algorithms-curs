# Задача 6. Среднее арифметическое элементов с номерами K..L (1-based).

N = int(input("N = "))
K = int(input("K = "))
L = int(input("L = "))
a = list(map(int, input(f"Введите {N} элементов: ").split()))

# K..L в номерах 1-based = индексы K-1 .. L-1
piece = a[K - 1:L]           # срез Python: правая граница НЕ включается
avg = sum(piece) / len(piece)
print("Среднее =", avg)