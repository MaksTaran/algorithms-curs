# Лабораторная 11. Обход дерева.
from collections import deque


# Узел дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Вставка (BST)
# Если значение меньше корня — в левое поддерево, иначе — в правое.
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# Поиск
def search(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    return search(root.left, value)


# Прямой обход (preorder, NLR)
def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)        # корень
        preorder(root.left, result)      # левое
        preorder(root.right, result)     # правое
    return result


# Симметричный обход (inorder, LNR)
def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)       # левое
        result.append(root.value)        # корень
        inorder(root.right, result)      # правое
    return result


# Обратный обход (postorder, LRN)
def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)     # левое
        postorder(root.right, result)    # правое
        result.append(root.value)        # корень
    return result


# Обход в ширину (BFS, level-order)
# Очередь: берём узел, добавляем в очередь его детей.
def bfs(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# Визуализация дерева в консоли
def print_tree(root, level=0, prefix="Корень: "):
    if root is not None:
        print("    " * level + prefix + str(root.value))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")


# Запуск
tree = None
for v in [50, 30, 20, 40, 70, 60, 80]:
    tree = insert(tree, v)

print("Дерево:")
print_tree(tree)

print("\nПрямой обход (NLR):       ", preorder(tree))
print("Симметричный обход (LNR): ", inorder(tree))
print("Обратный обход (LRN):     ", postorder(tree))
print("В ширину (BFS):           ", bfs(tree))

# поиск элемента
target = int(input("\nКакой элемент искать? "))
if search(tree, target):
    print(f"Элемент {target} найден")
else:
    print(f"Элемент {target} НЕ найден")