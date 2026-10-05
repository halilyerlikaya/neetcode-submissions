class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []       

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.min:
            if self.min[-1] > val:
                self.min.append(val)
            else:
                self.min += [self.min[-1]]
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.stk.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()