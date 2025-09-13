class MinStack:

    def __init__(self):
        self.data = []
        self.sorted = SortedList()
        

    def push(self, val: int) -> None:
        print(val)
        self.data.append(val)
        if len(self.data) == 1:
            self.sorted.add(val)
        else:
            if val <= self.sorted[-1]:
                self.sorted.add(val)
            else:
                self.sorted.add(val)


    def pop(self) -> None:
        if self.data:
            val = self.data[-1]     
            self.sorted.remove(val) 
            self.data = self.data[:-1]

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.sorted[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
