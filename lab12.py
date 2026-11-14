# Лабораторная 12. Работа с очередью.
from collections import deque
import queue


# Часть 1. Очередь через collections.deque (основной способ)
print("Часть 1. collections.deque")

q = deque()                                  # создание пустой очереди

# добавление в конец
q.append("A")
q.append("B")
q.append("C")
print(f"После добавления A, B, C:  q = {list(q)}")

# просмотр начала БЕЗ удаления
print(f"Первый в очереди (без удаления): {q[0]}")

# извлечение из начала (с удалением)
item = q.popleft()
print(f"Извлечено из начала: {item}    q = {list(q)}")

# проверка пустоты
print(f"Очередь пуста? {len(q) == 0}")

# размер
print(f"Размер очереди: {len(q)}")

# перебор элементов
print("Перебор элементов:")
for x in q:
    print(f"  → {x}")

# очистка
q.clear()
print(f"После очистки: q = {list(q)}, пусто? {len(q) == 0}")


# Часть 2. Очередь через queue.Queue (потокобезопасная)
print("Часть 2. queue.Queue")

qq = queue.Queue()                           # создание пустой очереди

# добавление через put()
qq.put("X")
qq.put("Y")
qq.put("Z")
print(f"После put X, Y, Z:   q = {list(qq.queue)}")

# просмотр начала без удаления (обращение к внутреннему списку)
print(f"Первый в очереди: {qq.queue[0]}")

# извлечение через get() — блокирующий, но т.к. очередь не пуста — вернёт сразу
item = qq.get()
print(f"Извлечено через get(): {item}    q = {list(qq.queue)}")

# проверка пустоты
print(f"Очередь пуста? {qq.empty()}")

# размер
print(f"Размер очереди: {qq.qsize()}")

# перебор элементов
print("Перебор элементов:")
for x in qq.queue:
    print(f"  → {x}")

# очистка
qq.queue.clear()
print(f"После очистки: q = {list(qq.queue)}, пусто? {qq.empty()}")


# Часть 3. Практический пример: очередь покупателей
print("Часть 3. Симуляция очереди покупателей")


customers = deque(["Анна", "Борис", "Вера", "Глеб"])

print(f"Исходная очередь: {list(customers)}")

# пока очередь не пуста — обслуживаем покупателя
step = 0
while customers:
    step += 1
    served = customers.popleft()
    print(f"Шаг {step}: обслужили '{served}', в очереди осталось: {len(customers)}")
    if customers:
        print(f"         следующий: {customers[0]}")

print("Очередь пуста — все обслужены.")


# Часть 4. Практический пример: BFS на графе
print("Часть 4. Обход графа в ширину (BFS) через очередь")


# граф — словарь смежности
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs(start):
    visited = set()                          # уже посещённые узлы
    q = deque([start])                       # очередь — старт с начального узла
    order = []                               # порядок обхода

    while q:
        node = q.popleft()                   # берём первый из очереди
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)           # добавляем соседей в конец

    return order

print(f"Граф: {graph}")
print(f"BFS из 'A': {bfs('A')}")