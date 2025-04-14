class Stack:
    def __init__(self):
        self.__data = []

    def push(self, val):
        self.__data.insert(0, val)

    def top(self):
        if len(self.__data) == 0:
            raise RuntimeError("Cannot Top empty Stack")
        return self.__data[0]

    def pop(self):
        if len(self.__data) == 0:
            raise RuntimeError("Cannot Pop empty Stack")
        item = self.__data.pop(0)
        return item

    def is_empty(self):
        return len(self.__data) == 0

    def __str__(self) -> str:
        res = ""
        if len(self.__data) == 0:
            return res
        for item in self.__data:
            res += str(item) + "\n"
        return res


def task1(s: str):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in opening_brackets:
            stack.push(ch)
        elif ch in closing_brackets:
            if stack.is_empty() or stack.top() != matching_brackets[ch]:
                return "Brackets do not match!"
            else:
                stack.pop()
    return "String is good!"


def task2(eq: str):
    st = Stack()
    eq = eq.split()
    for ch in eq:
        if ch.isnumeric():
            st.push(int(ch))
        elif ch == '+':
            num1 = st.pop()
            num2 = st.pop()
            st.push(num2 + num1)
        elif ch == '*':
            num1 = st.pop()
            num2 = st.pop()
            st.push(num2 * num1)
        elif ch == '-':
            num1 = st.pop()
            num2 = st.pop()
            st.push(num2 - num1)
        elif ch == '/':
            num1 = st.pop()
            num2 = st.pop()
            st.push(num2 / num1)
    return st.top()


stack = Stack()
print("1 - Вставка в стек",
      "2 - Просмотр верхушки",
      "3 - Удаление верхушки",
      "4 - Проверка на пустоту",
      "5 - Задание 1",
      "6 - Задание 2",
      "0 - Вывод стека",
      sep="\n"
      )
while True:
    command = int(input("Введите команду: "))
    while True:
        command = int(input("Введите команду: "))
        if command == 1:
            val = input("Введите значение: ")
            stack.push(val)
        elif command == 2:
            print(stack.top())
        elif command == 3:
            stack.pop()
        elif command == 4:
            if stack.is_empty():
                print("Empty Stack")
            else:
                print(f"Stack is not empty:\n{stack}")
        elif command == 5:
            string = input("Введите строчку: ")
            task1(string)
            print("String is good")
        elif command == 6:
            eq = input("Введите выражение: ")
            print(task2(eq))
        elif command == 0:
            print(stack)
        else:
            print("Несуществующая команда!")