"""

2 Sets:
1. Reach Pacific:
    - Up, Left
2. Reach Atlantic:
    - Down, Right

Intersection is the answer

Multi Point BFS
the borders are our starting points

1. Choices
    - up down left right
    curr < next since we are starting with border

2. State
    - 2 sets, pacific, atlantic
    - queue will help us perform the BFS


return [list(cell) for cell in pacific.intersection(atlantic)]

Time Complexity: O(RC)
Initialize Pacific and Atlantic Sets: O(R + C)
Pacific BFS O(RC)
Atlantic BFS O(RC)
Set Intersection O(RC)
Convert Intersection to Output O(RC)

Space Complexity: O(RC)
Pacific Set O(RC)
Atlantic Set O(RC)
Pacific BFS queue O(RC)
Atlantic BFS queue O(RC)

Pattern: Multi Source BFS with reverse traversal

Insight: instead of starting from every cell and checking whether water can reach the oceans,
start from the oceans and identify which cells can reach them

Invariant: every cell in an ocean's visited set has a valid descending path to that ocean

Condition:

heights[nr][nc] >= heights[row][col]

Python Concepts:
    - deque(pacific) initializes a queue using the elements of a set
    - set.intersection() finds elements common to both sets
    - Mark cells when enqueing, not when dequeing
"""
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        for row in range(ROWS):
            pacific.add((row, 0))
            atlantic.add((row, COLS - 1))

        for col in range(COLS):
            pacific.add((0, col))
            atlantic.add((ROWS - 1, col))

        def bfs(queue, visited):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    # Explore neighbors
                    nr = row + dr
                    nc = col + dc

                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue

                    if heights[nr][nc] < heights[row][col]:
                        continue

                    if (nr, nc) in visited:
                        continue

                    # Mark while enqueing
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        bfs(deque(pacific), pacific)

        bfs(deque(atlantic), atlantic)

        return [list(cell) for cell in pacific.intersection(atlantic)]



if __name__ == "__main__":
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = sol.pacificAtlantic(heights)
    print(result)
