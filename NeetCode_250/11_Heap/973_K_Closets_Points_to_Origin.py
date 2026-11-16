import math
import heapq

"""

1. Building the min heap
    - iterate throguh N points
    - each heappush() takes O(log N)
    - total: O(N log N)

2. Extracting the k closets points
    - perform k extractions
    - each heappop() takes O(log N)
    - total O(K log N)

Time: O(N log N + K log N) = O(N log N)
Space: O(N) since heap stores all N points


If we build usin gheapify instead of heappush()

O(N + K log N)
Space: O(N)

Pattern: heap, specifically a min heap
Recognition: Find the K smallest elements according to some metric

heapify: O(N)
heappop(): O(log N)
"""


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        """
        Min Heap Implementation
        """
        def e_distance(x2, y2):
            return math.sqrt( (0 - x2) ** 2 + (0 - y2) ** 2)

        min_heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = e_distance(x, y)
            heapq.heappush(min_heap, (distance, x, y))

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result

    def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Max Heap Approach
        - use a max heap because we want to keep the K smallest distances

        Once the heap reaches size k:
            1. Root is the largest distance among our current k Closets points
            2. If a new distance is smaller, replace
            3. if a new distance is greatear, ignore it
            4. this ensures the heap always contains the k closets points encountered so far
        """

        max_heap = []
        for x, y in points:
            distance = x*x + y*y

            if len(max_heap) < k:
                heapq.heappush((-distance, x, y))

            if distance < -max_heap[0][0]:
                heapq.heapreplace(max_heap, (-distance, x, y))

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(max_heap)
            result.append([x,y])

        return result

if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    sol = Solution()
    result = sol.kClosest(points, k)
    print(result)