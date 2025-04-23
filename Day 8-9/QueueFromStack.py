class MyQueue:

    def __init__(self):
        self.stack1_in = []
        self.stack2_out = []

    def push(self, x: int) -> None:
        self.stack1_in.append(x)

    def pop(self) -> int:
        self._shift_stacks()
        return self.stack2_out.pop()

    def peek(self) -> int:
        self._shift_stacks()
        return self.stack2_out[-1]

    def empty(self) -> bool:
        return not self.stack1_in and not self.stack2_out

    def _shift_stacks(self):
        if not self.stack2_out:
            while self.stack1_in:
                self.stack2_out.append(self.stack1_in.pop())

if __name__ == "__main__":
    solution = MyQueue()

    print("is empty? :", solution.empty())
    solution.push(3)
    solution.push(4)
    print("peek:", solution.peek())
    print("pop:", solution.pop())
    print("peek after pop:", solution.peek())
