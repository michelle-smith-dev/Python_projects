class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.myQueue = []

    def push(self, x: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)
        print("Stack 1:", self.stack1)

    def pop(self) -> int:
        while len(self.stack1) != 0:
            i = self.stack1.pop()
            self.stack2.append(i)  # stack.append(primary.pop()), less code lines but not as readable
        print("Stack 2:", self.stack2)
        self.stack2.pop()
        print("Pop Stack 2:", self.stack2)
        # while len(self.stack2) != 0:
        #     self.peek()
        #     self.stack2.pop()
        # return self.empty()

    def peek(self) -> int:
        print("Peek:", self.stack2[-1])
        if self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[-1]

    def empty(self) -> bool:  # bool is the type hint, it is the return type
        if len(self.stack1) == 0:
            print("My Queue is empty:", self.stack2)
            return True
        else:
            return False


obj = MyQueue()
obj.push(3)
obj.push(31)
obj.push(23)
obj.pop()

