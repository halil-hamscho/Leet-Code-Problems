"""


So once we reach x amount of capital, we can invest in capital[i] that will give us profit[i]

the once we reach x, invest in the largest profit project

- I need the min capital, max profit?


initial capacity of 0
iterate through, by the max profit of curr_capacity
once we cross a capacity, we add the possible ones to the max_heap


curr cap
    - pick most profitable project
    - add to capacity
    - add values that are eligible to the max_heap

we are bounded by our project profitability and incremental eligibility

Pattern: Greedy Pattern

This problem is similar to 1834 Single Threaded CPU

both problems

    1. a sorted collection that determines when items become available
    2. a pointer that progressively adds eligible items
    3. a heap that selects the highest priority available item

eligibility and priority

Time: O(n log n)
Space: O(n)

"""
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:

        sorted_array = sorted(zip(capital, profits))

        curr_capacity = w
        max_heap = []
        i = 0
        for _ in range(k):

            # Add newly eligible projects
            while i < len(sorted_array) and curr_capacity >= sorted_array[i][0]:
                    heapq.heappush(max_heap, -sorted_array[i][1])
                    i += 1
           
            if not max_heap:
                break

            # Select the most profitable and increase current capital
            curr_capacity += -heapq.heappop(max_heap)

        return curr_capacity

if __name__ == "__main__":
    w = 0
    k = 3
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    sol = Solution()
    result = sol.findMaximizedCapital(k, w, profits, capital)