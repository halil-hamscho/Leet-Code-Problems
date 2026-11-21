"""

This question is very similar to reorganize a string

- greedy approach where we take the most occurances of a letter

- need a conditional to make sure it is not 3 iterations

in reverse string there is 

when there is nothing in the heap then that means cut the string

greedily select the character with the highest remaining frequency, but that doesn't necessarily mean
we should append it twice

Example:
a = 0
b = 2
c = 5

c
"""
import heapq
from collections import deque

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap = []

        for count, letter in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count > 0:
                max_heap.append((count, letter))

        heapq.heapify(max_heap)
        result = []

        while max_heap:

            count, char = heapq.heappop(max_heap)

            if len(result) >= 2 and result[-1] == result[-2] == char:

                if not max_heap:
                    break

                next_count, next_char = heapq.heappop(max_heap)

                heapq.heappush(max_heap, (count, char))

                count, char = next_count, next_char

            result.append(char)
            count += 1

            if count < 0:
                heapq.heappush(max_heap, (count, char))

        return "".join(result)

if __name__ == "__main__":
    sol = Solution()
    result = sol.longestDiverseString(a = 0, b = 8, c = 11)