class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
    
if __name__ == "__main__":
    q = MyCircularQueue(3)
    
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.enQueue(1))
    print(q.enQueue(4))
    print(q.Rear())      
    print(q.isFull())
    print(q.deQueue())
    print(q.enQueue(4))
    print(q.Rear())      
    print(q.Front())
