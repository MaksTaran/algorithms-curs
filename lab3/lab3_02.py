# Задача 2. N > 0. Найти 1.1 · 1.2 · 1.3 · ... (N сомножителей).

N = int(input("N = "))

product = 1.0
for i in range(N):
    factor = 1.1 + i * 0.1    # 1.1, 1.2, 1.3, ...
    product *= factor

print("Произведение =", product)