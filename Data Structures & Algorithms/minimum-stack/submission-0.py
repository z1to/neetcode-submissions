class MinStack:

    def __init__(self):
        self.stk = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.mstk:
            self.mstk.append(val)
        else:
            current_min = min(val, self.mstk[-1])
            self.mstk.append(current_min)

    def pop(self) -> None:
        self.stk.pop()
        self.mstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.mstk[-1]
