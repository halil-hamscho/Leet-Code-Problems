Heap

- Only gurantees that every parent is smaller than or equal to its children

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

Heapify

2 Ways to Construct a heap

    1. Repeated Insertion (n elements)
        1. Start with empty heap
        2. Insert each element
        3. Percolate up after each insertion

    Time: O(n log n)

    2. Bottom Up Heapify
        1. Find the last node that has children
        2. Starting from that node, move backwards toward the root
        3. For each node, percolate it down until the heap property is satisfied

        - start at last parent, modify existing array

    Time: O(n)

    Why?
        - nodes near the bottom require very little movement
        - nodes near the root can move farther, but there are very few of them
        - leaf nodes require no movement at all

    def heapify(nums):
        n = len(nums)

        def sift_down(i): # Similar to pop() operation
            while 2 * i + 1 < n:
                left = 2 * i + 1
                right = 2 * i + 2

                smallest = left

                if right < n and nums[right] < nums[left]:
                    smallest = right

                if nums[i] <= nums[smallest]:
                    break

                nums[i], nums[smallest] = nums[smallest], nums[i]
                i = smallest

        for i in range(n // 2 - 1, -1, -1):
            sift_down(i)

        return nums

Python already has heapify

import heapq

nums = [5, 3, 8, 1, 2]

heapq.heapify(nums)
O(n) time

Invariant:
    - ater processing a node, the entire subtree rooted at that node is a valid heap

Why is building a heap using repeated heappush() operations O(n log n) while bottom up heapify() is O(n)

Heap with 1,000,000 elements

Notes
500,000 leaf nodes -> 0 Levels
250,000 nodes -> 1 level
125,000 nodes -> 2 levels
62,500 nodes -> 3 levels
1 root node -> approximately 19 levels

As the potential percolation distance increases, the number of node that require that muchwork decreases

Interviews


In order to implement a Max Heap
we can negate the numbers before inserting them

import heapq
nums = [3, 7, 2, 9, 5]

max_heap = [-num for num in nums]

heapq.heapify(max_heap)
print(-max_heap[0])