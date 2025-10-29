class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            val = min(self.min[-1], val)
            self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        # min = math.inf
        # for n in self.stack:
        #     if n < min:
        #         min = n
        # return min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()