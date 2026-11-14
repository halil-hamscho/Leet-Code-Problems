import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x != y:
                y = y - x
                heapq.heappush(max_heap, -y)

        return -max_heap[0] if max_heap[0] else 0
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.lastStoneWeight([2,7,4,1,8,1])