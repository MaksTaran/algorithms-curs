# Задача 2. N членов прогрессии: A, A·D, A·D², A·D³, ...

N = int(input("N = "))
A = float(input("A = "))
D = float(input("D = "))

arr = [A * D ** i for i in range(N)]   # i = 0..N-1

print(arr)