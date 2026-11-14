# Задача 4. Рекурсивно проверить, является ли строка палиндромом.

def is_palindrome(s):
    # нормализация: без пробелов и в нижнем регистре
    s = s.lower().replace(" ", "")
    if len(s) <= 1:          # базовый случай: 0 или 1 символ
        return True
    if s[0] != s[-1]:        # крайние символы разные — не палиндром
        return False
    return is_palindrome(s[1:-1])   # проверяем «внутренность»

text = input("Строка: ")
print("Палиндром" if is_palindrome(text) else "Не палиндром")