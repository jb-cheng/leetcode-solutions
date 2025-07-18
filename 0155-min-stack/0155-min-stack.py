class MinStack:

    def __init__(self):
        self.minimum = [float('inf')]
        self.stack = list()

    def push(self, val: int) -> None:
        self.minimum.append(min(self.minimum[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.minimum.pop()
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()