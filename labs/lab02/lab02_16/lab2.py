from time import sleep


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


class SimpleLinkedList():
    def __init__(self, node=Node):
        self.head = None

    def __len__(self) -> int:
        cur = self.head
        len = 0
        while cur:
            len += 1
            cur = cur.next
        return len

    def __reversed__(self):
        curr = self.head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def __getitem__(self, index: int):
        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def __setitem__(self, index, val):
        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.val = val

    def __delitem__(self, index):
        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")
        if index == 0:
            self.pop_front()
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next

    def __str__(self) -> str:
        res = ""
        cur = self.head
        while cur.next:
            res += str(cur.val) + " -> "
            cur = cur.next
        res += str(cur.val)
        return res

    def push_back(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        curr_node: Node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def push_front(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert(self, val, index):
        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")
        if index == 0:
            self.push_back(val)
            return
        curr = self.head
        new_node = Node(val)
        for _ in range(index - 1):
            curr = curr.next
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node

    def pop_back(self):
        if self.head is None:
            raise IndexError("Cannot pop_back empty list!")
        del self[len(lst) - 1]

    def pop_front(self):
        if self.head is None:
            raise IndexError("Cannot pop_front empty list!")
        self.head = self.head.next

    def clear(self):
        self.head.next = None

    def task1(self):
        res = SimpleLinkedList()
        vals = []
        for i in range(len(self)):
            vals.append(self[i])
        vals.sort()
        for val in vals:
            res.push_back(val)
        return res

    def task2(self):
        min = self.head.val
        max = self.head.val
        min_inx = 0
        max_inx = 0
        for i in range(len(self)):
            if min > self[i]:
                min = self[i]
                min_inx = i
            if max < self[i]:
                max = self[i]
                max_inx = i
        self[max_inx], self[min_inx] = min, max


lst = SimpleLinkedList()
print("1 - Вставка в начало",
      "2 - Вставка в конец",
      "3 - Вставка по индексу",
      "4 - Удаление по индексу",
      "5 - Удаление певрого элемета",
      "6 - удаление последнего элемента",
      "7 - Реверс списка",
      "8 - Взятие по индексу",
      "9 - Сортировка списка",
      "10 - Обмен максимального и минимального значения в списке",
      "11 - Вывод списка в поток",
      "12 - Очистка списка",
      sep='\n')
while True:
    command = int(input("Введите команду: "))
    match command:
        case 1:
            val = int(input("Введите значение: "))
            lst.push_front(val)
        case 2:
            val = int(input("Введите значение: "))
            lst.push_back(val)
        case 3:
            inx = int(input("Введите индекс: "))
            val = int(input("Введите значение: "))
            lst.insert(val, inx)
        case 4:
            inx = int(input("Введите индекс: "))
            del lst[inx]
        case 5:
            lst.pop_front()
        case 6:
            lst.pop_back()
        case 7:
            reversed(lst)
        case 8:
            inx = int(input("Введите индекс: "))
            item = lst[inx]
            print(f'Элемемет под номером {inx} = {item}')
        case 9:
            task1 = lst.task1()
            print(f"Отсортированный список {task1}")
        case 10:
            lst.task2()
        case 11:
            print(lst)
            sleep(2)
        case 12:
            lst.clear()
        case _:
            print("Несуществующая команда!")