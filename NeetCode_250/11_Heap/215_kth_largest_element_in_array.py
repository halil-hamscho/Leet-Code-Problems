"""

Pattern: Min Heap Size K

Intuition:
- Kth Largest -> Min_Heap Bounded by k, num > min_heap[0] replace

Intuition:

1. Populate the min heap with K elements
2. The root represents the smallest among out K largest candidates
3. If a new number is greater than the root, replace it
4. Otherwise, ignore it
5. After processing everything, the root is the Kth largest element

Time Complexity:
O (n log k)
- performing log k operations

Space:
O(k) since the heap can only have k nodes

the heap root always represents the weakest candidate among the k elements we want to retain
"""
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)

            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]
        