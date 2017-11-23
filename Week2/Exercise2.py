class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        assert not self.is_empty()
        return self.stack.pop()

    def peek(self):
        assert not self.is_empty()
        return self.stack[-1]
        # return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return self.stack == []


if __name__ == "__main__":
    my_stack = MyStack()

    my_stack.push("Hello")
    my_stack.push(2)
    my_stack.push([])
    print(my_stack.pop())
    print(my_stack.peek())
    print(my_stack.is_empty())
    my_stack.pop()
    my_stack.pop()
    print(my_stack.is_empty())
