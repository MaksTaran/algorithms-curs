# Задача 6. Рекурсивно поменять порядок слов в строке на обратный.

def reverse_words(s):
    words = s.split()        # нормализуем: убираем лишние пробелы
    if len(words) <= 1:      # базовый случай: одно слово (или пусто)
        return " ".join(words)
    # первое слово уходит в конец, остальные переворачиваем рекурсивно
    return reverse_words(" ".join(words[1:])) + " " + words[0]

text = input("Строка: ")
print(reverse_words(text))