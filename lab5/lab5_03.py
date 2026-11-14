# Задача 3. N (>2), A, B. Массив: a[0]=A, a[1]=B,
# каждый следующий = сумма всех предыдущих.

N = int(input("N = "))
A = int(input("A = "))
B = int(input("B = "))

arr = [A, B]
total = A + B           # сумма всех уже добавленных
for i in range(2, N):
    arr.append(total)   # новый элемент = сумма предыдущих
    total += total      # сумма всех теперь удваивается (было total, стало total + total)

print(arr)