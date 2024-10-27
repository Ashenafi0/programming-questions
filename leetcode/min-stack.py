class MinStack:

    def __init__(self):
        self.stack=[]
        self.stack_min=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.stack_min.append(val)
        else:
            if self.stack_min[-1]>val:
                self.stack_min.append(val)
            else:
                self.stack_min.append(self.stack_min[-1])
            self.stack.append(val)

            
        

        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.stack_min.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
        

    def getMin(self) -> int:
        if self.stack_min:
            return self.stack_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()