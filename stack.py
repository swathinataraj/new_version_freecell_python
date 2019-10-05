class Stack:
    # creates a new stack
    def __init__(self):
        self.list_stack = []  # represent the stack as a list
        self.size_stack = 0  # indicate the current size of the stack
        self.top_stack = -1  # indicate the top position of the stack

    # returns the number of items in the stack
    def __len__(self):
        return self.size_stack

    # returns True if the stack is empty or False otherwise
    def is_empty(self):
        return len(self) == 0

    # pushes an item onto the top of the stack
    def push(self, item):
        self.list_stack.append(item)
        self.top_stack += 1
        self.size_stack += 1

    # removes and returns the top item on the stack
    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        item = self.list_stack[self.top_stack]
        self.top_stack -= 1
        self.size_stack -= 1
        del self.list_stack[len(self)]
        return item

    # returns the item on the stack without removing it
    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        item = self.list_stack[self.top_stack]
        return item
