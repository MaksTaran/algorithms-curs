# Задача 7. Рекурсивно разложить число на сумму простых чисел.
# Разложение не единственное; здесь ищем любое.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def decompose(n, min_p=2):
    # базовый случай: осталось 0 — разложение собрано
    if n == 0:
        return []
    # пробуем простые в порядке убывания — так разложение получается короче
    for p in range(n, min_p - 1, -1):
        if is_prime(p):
            rest = decompose(n - p, p)   # p как новая нижняя граница — чтобы не повторяться
            if rest is not None:
                return [p] + rest
    return None      # разложить не удалось (для n >= 2 не бывает)

n = int(input("n = "))
parts = decompose(n)
print(f"{n} = " + " + ".join(map(str, parts)))