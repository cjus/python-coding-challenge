"""Basic implementation of a Stack"""


class Stack_Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Stack_Node(None)
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        node = Stack_Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
