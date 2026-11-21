
"""


Data Structures

- Max Heap to keep track of priority
- Set to keep track of letters

Pattern: Greedy with Max Heap

Greedy Principle remains the same: select the most frequent eligible character

next available index = i + K + 1
similar to using a cooldown queue

Underlying Intution:
Greedily select the most frequent available element, then temporarily prevent it from being selected again

If the heap is empty but characters remain in the cooldown queue, no valid arrangement is possible

"""
import heapq

from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = []
        
        for char, count in counts.items():
            max_heap.append((-count, char))

        heapq.heapify(max_heap)

        output = []
        prev = None

        while max_heap:

            count, char = heapq.heappop(max_heap)

            output.append(char)

            if prev:
                heapq.heappush(max_heap, (prev[0], prev[1]))

            if count + 1 < 0:
                prev = (count + 1, char)
            else:
                prev = None

        joined_s = "".join(output)
        return joined_s if len(joined_s) == len(s) else ""

if __name__ == "__main__":
    s = "aba"
    sol = Solution()
    result = sol.reorganizeString(s)