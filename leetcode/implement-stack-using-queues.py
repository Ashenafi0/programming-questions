class MyStack:

    def __init__(self):
        self.que=deque()

        

    def push(self, x: int) -> None:
        self.que.append(x)
        

    def pop(self) -> int:
        if self.que:
            for i in range(len(self.que)-1):
                self.que.append(self.que.pop())
            return self.que.pop()

        else:
            return 
        

    def top(self) -> int:
        if self.que:
            top=0
            for i in range(len(self.que)):
                top=self.pop()
                self.que.append(top)
            return top

        else:
            return
        

    def empty(self) -> bool:
        return len(self.que)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()