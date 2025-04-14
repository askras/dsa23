import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def symmetrical_traversal(self, node, result):
        if node:
            self.symmetrical_traversal(node.left, result)
            result.append(node.key)
            self.symmetrical_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.key)
                stack.append(node.right)
                stack.append(node.left)

        return result

    def postorder_traversal(self):
        result = []
        stack = [(self.root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.key)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return result

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._get_min_value(root.right)
            root.right = self._delete_recursive(root.right, root.key)

        return root

    def _get_min_value(self, node):
        while node.left:
            node = node.left
        return node.key

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def print_tree(self):
        result = []
        self.symmetrical_traversal(self.root, result)
        print("Симметричный обход (symmetrical):", result)

    def print_preorder(self):
        result = self.preorder_traversal()
        print("Прямой обход (preorder):", result)

    def print_postorder(self):
        result = self.postorder_traversal()
        print("Обратный обход (postorder):", result)

    def is_empty(self):
        return self.root is None

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

    def print_pretty_tree(self):
        print("Красивый вывод дерева:")
        self._print_pretty_tree_recursive(self.root, 0)
        print()

    def _print_pretty_tree_recursive(self, node, level):
        if node is not None:
            self._print_pretty_tree_recursive(node.right, level + 1)
            print("  " * level + str(node.key))
            self._print_pretty_tree_recursive(node.left, level + 1)

    def _insert_recursive_unordered(self, current, nodes):
        if not nodes:
            return

        random_side = random.choice(["left", "right"])  # Случайно выбираем сторону
        current.key = nodes.pop(0)  # Вместо случайного индекса, выбираем первый элемент

        if nodes and random_side == "left":
            current.left = Node(None)
            self._insert_recursive_unordered(current.left, nodes)

        if nodes and random_side == "right":
            current.right = Node(None)
            self._insert_recursive_unordered(current.right, nodes)

    def insert_unordered(self, nodes):
        if not nodes:
            return

        if self.root is None:
            self.root = Node(None)

        self._insert_recursive_unordered(self.root, nodes)

    def find_vertices_with_unequal_children(self):
        result = []
        self._find_vertices_with_unequal_children_recursive(self.root, result)
        return result

    def _find_vertices_with_unequal_children_recursive(self, node, result):
        if node:
            left_child_count = self._count_children(node.left)
            right_child_count = self._count_children(node.right)

            if left_child_count != right_child_count:
                result.append(node.key)

            self._find_vertices_with_unequal_children_recursive(node.left, result)
            self._find_vertices_with_unequal_children_recursive(node.right, result)

    def _count_children(self, node):
        if node is None:
            return 0
        return 1 + self._count_children(node.left) + self._count_children(node.right)


bst_search = BinarySearchTree()

# Вставляем элементы в дерево по порядку
elements_to_insert = [10, 5, 15, 3, 7, 12, 17]
for element in elements_to_insert:
    bst_search.insert(element)

bst_search.print_pretty_tree()
# Печатаем симметричный обход (должен быть отсортированным, так как это дерево поиска)
bst_search.print_tree()

print("Вершины с неравным количеством потомков в поддеревьях:", bst_search.find_vertices_with_unequal_children())

bst_unordered = BinarySearchTree()

# Вставляем элементы в дерево в произвольном порядке
elements_unordered = [10, 5, 15, 3, 7]
bst_unordered.insert_unordered(elements_unordered)

# Печатаем симметричный обход
bst_unordered.print_pretty_tree()

def main():
    bst = BinarySearchTree()

    while True:
        print("\nВыберите действие:")
        print("1. Вставить элемент")
        print("2. Удалить элемент")
        print("3. Поиск элемента")
        print("4. Проверить на пустоту")
        print("5. Вывести высоту дерева")
        print("6. Вывести дерево")
        print("7. Прямой обход")
        print("8. Обратный обход")
        print("9. Симметричный обход")
        print("10. Найти вершины с неравным количеством потомков")
        print("0. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == '1':
            key = int(input("Введите ключ для вставки: "))
            bst.insert(key)
        elif choice == '2':
            key = int(input("Введите ключ для удаления: "))
            bst.delete(key)
        elif choice == '3':
            key = int(input("Введите ключ для поиска: "))
            if bst.search(key):
                print("Элемент найден.")
            else:
                print("Элемент не найден.")
        elif choice == '4':
            if bst.is_empty():
                print("Дерево пусто.")
            else:
                print("Дерево не пусто.")
        elif choice == '5':
            print("Высота дерева:", bst.height())
        elif choice == '6':
            bst.print_pretty_tree()
        elif choice == '7':
            print("Прямой обход:")
            bst.print_preorder()
        elif choice == '8':
            print("Обратный обход:")
            bst.print_postorder()
        elif choice == '9':
            print("Симметричный обход:")
            bst.print_tree()
        elif choice == '10':
            vertices = bst.find_vertices_with_unequal_children()
            print("Вершины с неравным количеством потомков в поддеревьях:", vertices)
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
