from time import sleep


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.val)

class LinkedList:
    def __init__(self, node=Node):
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        cur = self.head
        len = 0
        while cur:
            len += 1
            cur = cur.next
        return len

    def __reversed__(self):
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def __getitem__(self, index: int):
        if index < 0:
            index += len(self)
        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")

        if len(self) // 2 < index:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr.val
        else:
            curr = self.tail
            for _ in range(len(self) - index - 1):
                curr = curr.prev
            return curr.val

    def __setitem__(self, index, val):
        if index < 0:
            index += len(self)
        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")

        if len(self) // 2 <= index:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.val = val
        else:
            curr = self.tail
            for _ in range(len(self) - index):
                curr = curr.prev
            curr.val = val

    def __delitem__(self, index):
        if index < 0:
            index += len(self)

        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")

        if index == 0:
            self.pop_front()

        if index == len(self) - 1:
            self.pop_back()

        if len(self) // 2 >= index:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.next.prev = curr
        else:
            curr = self.tail
            for _ in range(len(self) - index - 1):
                curr = curr.prev
            curr.prev = curr.prev.prev
            curr.prev.prev.next = curr

    def __str__(self) -> str:
        res = ""
        if self.head is None:
            return ("Empty LinkedList")

        cur = self.head
        while cur.next:
            res += str(cur.val) + " ⇄ "
            cur = cur.next
        res += str(cur.val)
        return res

    def push_back(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        if len(self) == 1:
            self.tail = new_node
            self.tail.prev = self.head
            self.head.next = self.tail
            return

        cur = self.tail
        cur.next = new_node
        new_node.prev = cur
        self.tail = new_node

    def push_front(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        if len(self) == 1:
            tmp = self.head
            new_node.next = tmp
            tmp.prev = new_node
            self.head = new_node
            self.tail = tmp
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert(self, val, index):
        if index < 0:
            index += len(self)

        if len(self) < index or index < 0:
            raise IndexError(f"Invalid index {index}")

        if index == 0:
            self.push_front(val)
            return

        if index == len(self) - 1:
            self.push_back(val)
            return

        new_node = Node(val)

        if len(self) // 2 >= index:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            new_node.prev = curr
            curr.next = new_node
            new_node.next.prev = new_node
        else:
            curr = self.tail
            for _ in range(len(self) - index - 1):
                curr = curr.prev
            new_node.next = curr.next
            new_node.prev = curr
            curr.next = new_node
            new_node.next.prev = new_node

    def pop_back(self):
        if self.head is None:
            raise IndexError("Cannot pop_back empty list!")

        prev = self.tail.prev
        prev.next = None
        self.tail.prev = None
        self.tail = prev

    def pop_front(self):
        if self.head is None:
            raise IndexError("Cannot pop_front empty list!")
        next = self.head.next
        next.prev = None
        self.head.next = None
        self.head = next

    def clear(self):
        self.head = None
        self.tail = None

    def index(self, val) -> int:
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise RuntimeError(f"Cannot find {val} in list!")


def task1(linked_list: LinkedList):
    if linked_list is None:
        return

    val = {}

    for i in range(len(linked_list)):
        if linked_list[i] in val.keys():
            val[linked_list[i]] += 1
        else:
            val[linked_list[i]] = 1

    current = linked_list.head
    while current:
        if val[current.val] == 1:
            if current.prev:
                current.prev.next = current.next
            else:
                linked_list.head = current.next

            if current.next:
                current.next.prev = current.prev
            else:
                linked_list.tail = current.prev

        current = current.next


def task2(linked_list1: LinkedList, linked_list2: LinkedList) -> LinkedList:
    res = LinkedList()
    for i in range(len(linked_list1) if len(linked_list1) <= len(linked_list2) else len(linked_list2)):
        res.push_back(linked_list1[i] * linked_list2[i])
    return res


lst = LinkedList()
print("1 - Вставка в начало",
      "2 - Вставка в конец",
      "3 - Вставка по индексу",
      "4 - Удаление по индексу",
      "5 - Удаление певрого элемета",
      "6 - Удаление последнего элемента",
      "7 - Реверс списка",
      "8 - Взятие по индексу",
      "9 - Удаление всех элементов, которые встречаются ровно 1 раз",
      "10 - Попарное произведение L1 и L2",
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
            print(f"Список, до удаления всех элементов, встречающихся 1 раз {lst}")
            task1(lst)
            print(f"Список, после удаления всех элементов, встречающихся 1 раз {lst}")
            sleep(2)
        case 10:
            size = int(input("Введите длину 2-ого списка"))
            lst2 = LinkedList()
            for i in range(size):
                val = int(input(f"Введите значение для {i}-ого элемента"))
                lst2.push_back(val)
            print(task2(lst2, lst))
        case 11:
            print(lst)
            sleep(2)
        case 12:
            lst.clear()
        case _:
            print("Несуществующая команда!")