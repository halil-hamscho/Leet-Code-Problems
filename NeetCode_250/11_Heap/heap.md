Heap

Specialized Tree-Based Structure
    - Implements the abstract data type of "Priority Queue"

    2 Types

    1. Min Heap -> smallest value at the root node
    2. Max Heap -> largest value at the root node

Dynamic Array (1 based indexing)
    - left child (2 x i)
    - right child (2 x i + 1)
    - parent i / 2

Push

O(log n)

- As long as child is < parent, continue switching

def push(self, val):
    self.heap.append(val)
    i = len(self.heap) - 1

    # Percolate Up (valid index and i is less than parent)
    while i > 1 and self.heap[i] < self.heap[i // 2]:
        temp = self.heap[i]
        self.heap[i] = self.heap[i // 2]
        self.heap[i // 2] = temp
        i = i // 2

Pop

O (log n)
    - pop from the heap the value with the highest priority

1. Read the root element
2. Take the rightmost node fo the last level and swap it
3. Maintain structure property, but order property is violated
4. Find the nodes right place
5. Swap the node with min(left_child, right_child)

def pop(self):
    if len(self.heap) == 1:
        return None
 
    if len(self.heap) == 2:
        return self.heap.pop()

    result = self.heap[1]

    self.heap[1] = self.heap.pop()

    i = 1

    while 2 x i < len(self.heap): # as long as there is a left child
        left = 2 x i
        right = 2 x i + 1

        smallest = left

        # If right child exists and it is smaller than left
        if right < len(self.heap) and self.heap[right] < self.heap[left]:
            smallest = right

        # if the parent is smaller or equal to the child, then no swap
        if self.heap[i] <= self.heap[smallest]:
            break

        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]

        i = smallest

    return result

