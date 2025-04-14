class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            popped_data = self.head.data
            self.head = None
            self.size -= 1
            return popped_data
        else:
            popped_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped_data

    def pop_back(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            popped_data = self.head.data
            self.head = None
            self.size -= 1
            return popped_data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            popped_data = current.next.data
            current.next = None
            self.size -= 1
            return popped_data

    def at(self, index):
        if self.size == 0:
            return None
        else:
            if index < 0:
                index += self.size
            if index < 0 or index >= self.size:
                raise IndexError("Incorrect index")
            current = self.head
            for i in range(index):
                current = current.next
            return current.data

    def push(self, data, index):
        if index == 0:
            self.push_front(data)
        elif index == self.size:
            self.push_back(data)
        else:
            new_node = Node(data)
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def pop(self, index):
        if self.size == 0:
            return None
        else:
            if index == -1:
                return self.pop_front()
            elif index == self.size:
                return self.pop_back()
            else:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                to_remove = current.next
                current.next = to_remove.next
                popped_data = to_remove.data
                del to_remove
                self.size -= 1
                return popped_data

    def print_list(self):
        if self.size == 0:
            print('\n')
            print("List is empty")
            print('\n')
        else:
            current = self.head
            print("\n")
            while current.next is not None:
                print(str(current.data) + " -> ", end='')
                current = current.next
            print(str(current.data))
            print("\n")

    def clear(self):
        while self.head is not None:
            to_remove = self.head
            self.head = self.head.next
            del to_remove
        self.size = 0

    def has_elements_exceeding_sum(self):
        if self.head is None:
            return False

        total_sum = 0
        current = self.head
        while current:
            total_sum += current.data
            current = current.next

        current = self.head
        while current:
            if current.data > total_sum:
                return True
            current = current.next

        return False

    def separate_positive_negative(self):
        if self.head is None:
            return None, None

        positive_list = LinkedList()
        negative_list = LinkedList()

        current = self.head
        while current:
            if current.data > 0:
                positive_list.push_back(current.data)
            elif current.data < 0:
                negative_list.push_back(current.data)
            current = current.next

        return positive_list, negative_list


def menu():
    print("1.     Push Front")
    print("2.     Push Back")
    print("3.     Push at Index")
    print("4.     Pop Front")
    print("5.     Pop Back")
    print("6.     Pop at Index")
    print("7.     Print List")
    print("8.     List Length")
    print("9.     Clear List")
    print("10.    Check for Elements Exceeding Sum")
    print("11.    Separate Positive and Negative Elements")
    print("0.     Exit")


linked_list = LinkedList()

while True:
    menu()
    task = input("Enter your wish (0-11): ")

    if task == "0":
        print("\n")
        print("Exiting the program.")
        break
    elif task == "1":
        data = input("Enter data to push front: ")
        linked_list.push_front(data)
    elif task == "2":
        data = input("Enter data to push back: ")
        linked_list.push_back(data)
    elif task == "3":
        data = input("Enter data to push: ")
        index = int(input("Enter index to push at: "))
        linked_list.push(data, index)
    elif task == "4":
        popped_data = linked_list.pop_front()
        print("\n")
        print(f"Popped front: {popped_data}")
        print("\n")
    elif task == "5":
        popped_data = linked_list.pop_back()
        print("\n")
        print(f"Popped back: {popped_data}")
        print("\n")
    elif task == "6":
        index = int(input("Enter index to pop at: "))
        popped_data = linked_list.pop(index)
        print("\n")
        print(f"Popped at index {index}: {popped_data}")
        print("\n")
    elif task == "7":
        linked_list.print_list()
    elif task == "8":
        print("\n")
        print(f"Length of the list: {linked_list.size}")
        print("\n")
    elif task == "9":
        linked_list.clear()
        print("\n")
        print("List is empty.")
        print("\n")
    elif task == "10":
        if linked_list.has_elements_exceeding_sum():
            print("\n")
            print("There are elements exceeding the sum.")
            print("\n")
        else:
            print("\n")
            print("No elements exceeding the sum.")
            print("\n")
    elif task == "11":
        positive_elements, negative_elements = linked_list.separate_positive_negative()

        print("Positive Elements:")
        positive_elements.print_list()

        print("Negative Elements:")
        negative_elements.print_list()
    else:
        print("\n")
        print("Invalid choice. Please enter a number between 0 and 11.")
        print("\n")
