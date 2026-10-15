"""
When implementing a circular queue
two approches
- Linked List
- Circular Array

For circular array
2 pointers
front
back
these tell us where the insertion and deletion points are

in this case formulas needed
# Move Forward
(index + 1) % k

# Move Backward
(index - 1) % k

Time:
Initialization O(k)

Space
O(k) for array

Note:
self.rear is the NEXT insertion point
so when enQueue, set the value first, then move forward

when getting isRear(), you need to move backwards first to get that previous value

"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.array = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        # Insert
        self.array[self.rear] = value

        # Update insertion point further and the size
        self.rear = (self.rear + 1) % self.k
        self.size += 1

        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False

        self.array[self.front] = None
        self.front = (self.front + 1) % self.k
        self.size -= 1

        return True

    def Front(self) -> int:

        return self.array[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:

        return self.array[(self.rear - 1) % self.k] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:

        return self.size == 0

    def isFull(self) -> bool:

        return self.size == self.k


if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    myCircularQueue.enQueue(1); 
    myCircularQueue.enQueue(2); 
    myCircularQueue.enQueue(3); 
    myCircularQueue.enQueue(4); 
    myCircularQueue.Rear();     
    myCircularQueue.isFull();   
    myCircularQueue.deQueue();  
    myCircularQueue.enQueue(4); 
    myCircularQueue.Rear();     