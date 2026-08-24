class MyStack:

    def __init__(self):
        self.stack = []
        self.move_queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.move_queue.append(self.stack.pop(0))
        x = self.stack.pop(0)
        for i in range(len(self.move_queue)):
            self.stack.append(self.move_queue.pop(0))
        return x

    def top(self) -> int:
        for i in range(len(self.stack) - 1):
            self.move_queue.append(self.stack.pop(0))
        x = self.stack.pop(0)
        self.move_queue.append(x)
        for i in range(len(self.move_queue)):
            self.stack.append(self.move_queue.pop(0))
        return x



    def empty(self) -> bool:
        return self.stack == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()