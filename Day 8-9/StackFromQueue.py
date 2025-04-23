class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
        return None

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    solution = MyStack()

    print("Is empty?", solution.empty())
    solution.push(5)
    solution.push(10)
    print("Top element:", solution.top())
    print("Popped element:", solution.pop())
    print("Top element after pop:", solution.top())
    print("Is empty now?", solution.empty())
    print("Popped element:", solution.pop())
    print("Is empty now?", solution.empty())
