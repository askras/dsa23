class Node:
    def __init__(self, data):
        self.data = data
        self.last = None    
class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        if self.top is None:
            return True
        return False
    
    def push(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.last = self.top
            self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise RuntimeError("Cannot Pop empty Stack")
        res = self.top.data
        self.top = self.top.last
        return res
            
    def top(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def printl(self):
        top = self.top
        while not top.last.is_empty():
            print(top.data)
            top = top.last
    
    def clear(self):
            while not self.top.last.is_empty():
                self.top = self.top.last   
                
def task1(string):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    stack = Stack()
    res = 'Wrong string!'
    if len(string)%2 != 0:
        return res
    for i in string:
        if i in left:
            stack.push(i)
        elif right.index(i) == left.index(stack.data):
            stack.pop()
        else:
            return res
    return 'Good string!'

def task2(string):
    num = list('123456789')
    operation = list('+-*/')
    stack = Stack()
    for i in string:
        if i in num:
            stack.push(i)
        if i == operation[0]:
            a = stack.pop()
            b = stack.pop()
            stack.push(str(int(a)+int(b)))
        elif i == operation[1]:
            a = stack.pop()
            b = stack.pop()
            stack.push(str(int(a)-int(b)))
        elif i == operation[2]:
            a = stack.pop()
            b = stack.pop()
            stack.push(str(int(a)*int(b)))
        elif i == operation[3]:
            a = stack.pop()
            b = stack.pop()
            stack.push(str(int(a)//int(b)))
    return stack.pop()