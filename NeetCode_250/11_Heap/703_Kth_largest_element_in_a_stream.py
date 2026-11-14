"""
Instead of maintaing a max heap containing every element
we maintain a min heap containing only the k largest elements

Distinction
1. Max Heap: the root is the largest element, but the remaining elements are not sorted
2. Min heap of size k: the root is the smallest of k largest elements, which makes it the kth largest overall

Pattern: Top K elements using a bounded min heap

We use a min heap bounded by size k

"""
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]

        if self.heap[0] < val:
            # or heapq.heapreplace(self.heap, val)
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
    
if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    kthLargest.add(3)
    kthLargest.add(5)
    kthLargest.add(10)
    kthLargest.add(9)
    kthLargest.add(5)




