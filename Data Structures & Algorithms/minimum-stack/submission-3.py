class MinStack:

    def __init__(self):
        self.stack = []
        self.m = None
        self.current = 0
        

    def push(self, val: int) -> None:
        
        if self.m is None:
            self.m = val
            self.stack.append((val, val))
        else:
            if val <= self.m:
                self.stack.append((val, val))
                self.m = val
            else:
                self.stack.append((val, self.m))


            
    def pop(self) -> None:
        cur = self.stack.pop()
        if cur[0] == self.m:
            if self.stack:
                self.m = self.stack[-1][1]
            else:
                self.m = None

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.m

        
