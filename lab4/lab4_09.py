# Задача 9. Рекурсивное решение «Ханойской башни».

def hanoi(n, source, target, spare, moves):
    # n       — сколько дисков осталось перенести
    # source  — откуда
    # target  — куда
    # spare   — вспомогательный стержень
    # moves   — список для накопления шагов
    if n == 0:               # базовый случай: переносить нечего
        return
    hanoi(n - 1, source, spare, target, moves)   # 1) n-1 диск → spare
    moves.append((n, source, target))            # 2) нижний диск → target
    hanoi(n - 1, spare, target, source, moves)   # 3) n-1 диск → target

n = int(input("Сколько дисков? "))
moves = []
hanoi(n, "A", "C", "B", moves)

print(f"Минимум ходов: {len(moves)}  (2^{n} - 1 = {2**n - 1})")
for i, (disk, src, dst) in enumerate(moves, 1):
    print(f"{i:2d}. диск {disk}: {src} → {dst}")