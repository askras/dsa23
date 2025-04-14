from time import sleep

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


class CircularList():
    def __init__(self, node=Node):
        self.head = None

    def __len__(self) -> int:
        cur = self.head
        if self.head is None:
            return 0

        if self.head.next is None:
            return 1

        length = 1
        while cur.next != self.head:
            length += 1
            cur = cur.next
        return length

    def reverse(self):
        if self.head is None:
            raise RuntimeError()
        prev = None
        curr = self.head
        length = len(self)
        for _ in range(length):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head.next = prev
        self.head = prev

    def popValue(self, reach):
        curr = self.head
        index = 0
        while curr.next.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError(f"List does not have node with value {reach}")
        curr.next = curr.next.next

    def popAfterValue(self, reach):
        curr = self.head
        index = 0
        while curr.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError(f"List does not have node with value {reach}")
        curr.next = curr.next.next

    def popBeforeValue(self, reach):
        curr = self.head
        index = 0
        while curr.next.next.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError(f"List does not have node with value {reach}")
        curr.next = curr.next.next

    def __str__(self) -> str:
        res = "-> "
        if self.head is None:
            return "Empty list"

        cur = self.head
        for _ in range(len(self) - 1):
            res += str(cur.val) + " -> "
            cur = cur.next
        res += str(cur.val) + " ->"
        return res

    def push_back(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        if len(self) == 1:
            self.head.next = new_node
            new_node.next = self.head
            return

        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = self.head

    def push_front(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        if len(self) == 1:
            new_node.next = self.head
            self.head.next = new_node
            self.head = new_node

        curr_node = self.head
        for _ in range(len(self) - 1):
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insertBeforeValue(self, val, reach):
        new_node = Node(val)
        curr = self.head
        index = 0
        while curr.next.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError(f"List does not have node with value {reach}")
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node

    def insertAfterValue(self, val, reach):
        new_node = Node(val)
        curr = self.head
        index = 0
        while curr.val != reach:
            curr = curr.next
            index += 1
            if index > len(self):
                raise RuntimeError(f"List does not have node with value {reach}")
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node

    def pop_back(self):
        if self.head is None:
            raise IndexError("Cannot pop_back empty list!")
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        curr.next = curr.next.next

    def pop_front(self):
        if self.head is None:
            raise IndexError("Cannot pop_front empty list!")

        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        self.head = self.head.next
        curr.next = self.head

    def clear(self):
        self.head = None

    def index(self, val):
        curr = self.head
        for i in range(len(self)):
            if curr.val == val:
                return i
            curr = curr.next
        raise RuntimeError(f"{val} is not in List")

    def count_max_elements(self):
        if self.head is None:
            return 0

        max_value = float('-inf')
        count = 0

        curr = self.head
        for _ in range(len(self)):
            if curr.val > max_value:
                max_value = curr.val
                count = 1
            elif curr.val == max_value:
                count += 1
            curr = curr.next

        return count

    def remove_elements_more_than_two(self):
        if self.head is None:
            return

        elements_count = {}
        curr = self.head

        # Подсчитываем количество вхождений каждого элемента
        for _ in range(len(self)):
            if curr.val in elements_count:
                elements_count[curr.val] += 1
            else:
                elements_count[curr.val] = 1
            curr = curr.next

        # Удаляем элементы, встречающиеся более двух раз
        curr = self.head
        prev = None
        for _ in range(len(self)):
            if elements_count[curr.val] > 2:
                if prev is None:
                    self.pop_front()
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next


# Пример использования
lst = CircularList()

print("1 - Вставка в начало",
      "2 - Вставка в конец",
      "3 - Вставка до определённого значения",
      "4 - Вставка после определённого значения",
      "5 - Удаление по значению",
      "6 - Удаление до определённого значения",
      "7 - Удаление после определённого значения",
      "8 - Удаление первого элемента",
      "9 - Удаление последнего элемента",
      "10 - Реверс списка",
      "11 - Поиск индекса по значению",
      "13 - Задание 1",
      "14 - Задание 2",
      "12 - Очистка списка",

      "0 - Вывод списка в поток",
      sep='\n')

while True:
    command = int(input("Введите команду: "))
    if command == 1:
        val = int(input("Введите значение: "))
        lst.push_front(val)
    elif command == 2:
        val = int(input("Введите значение: "))
        lst.push_back(val)
    elif command == 3:
        reach = int(input("Введите значение, до которого нужно вставить элемент: "))
        val = int(input("Введите значение: "))
        lst.insertBeforeValue(val, reach)
    elif command == 4:
        reach = int(input("Введите значение, после которого которого нужно вставить элемент: "))
        val = int(input("Введите значение: "))
        lst.insertAfterValue(val, reach)
    elif command == 5:
        reach = int(input("Введите значение, которое нужно удалить из списка: "))
        lst.popValue(reach)
    elif command == 6:
        reach = int(input("Ввдите значение, до которого нужно удалить элменет"))
        lst.popBeforeValue(reach)
    elif command == 7:
        reach = int(input("Введите значение, после которого нужно удалить элемент"))
        lst.popAfterValue(reach)
    elif command == 8:
        lst.pop_front()
    elif command == 9:
        lst.pop_back()
    elif command == 10:
        lst.reverse()
    elif command == 11:
        val = int(input("Введите значение: "))
        print(lst.index(val))
    elif command == 12:
        lst.clear()
    elif command == 13:
        print(f"Количество максимальных элементов: {lst.count_max_elements()}")
    elif command == 14:
        lst.remove_elements_more_than_two()
        print("Элементы, входящие в список более двух раз, удалены.")
    elif command == 0:
        print(lst)
        sleep(2)
    else:
        print("Несуществующая команда!")
