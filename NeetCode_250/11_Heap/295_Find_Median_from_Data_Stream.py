"""

2 Ways to go about this
Median: middle value in an ORDERED LIST

addNum
    -> find insertion point
    -> add, then shift everything else to the right from i + 1


- Binary Search Way

    - addNum: Use Binary Search (log n) to find insertion point, then insert, shift all numbers to the right. 
        Time Complexity: O(log n + n)
    - findMedian: O(1)

- 2 Heaps
the expensive operation is keeping the list sorted

however, we don't need everything to be sorted, we just need access the middle number

    Invariants:
        - ordering: every element in the max heap is less than or equal to every element in the min heap
        - size: the max heap has one more element than the min heap


Pattern: 2 Heaps

Generalization:
- lets say we want 25th percentile
we want to maintain a boundary, but if the boundary is different

we adjust the len of the max_heap to contain the distribution that we want


1. Ordering:
    - max heap numbers <= min heap numbers

2. Size: max heap contains the same # of elemeents or exactly one more

^ the size invariant is what we change
"""
import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
            
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            # max heap greater
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -num)
            
        elif len(self.min_heap) > len(self.max_heap):
            # min heap greater
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        return -self.max_heap[0]
        
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


    def findMedian(self) -> float:

        if self.lenmax == self.lenmin:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# 
# obj.addNum(num)
# param_2 = obj.findMedian()
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    result1 = obj.findMedian()
    obj.addNum(3)
    result2 = obj.findMedian()



