from typing import List

"""
You are given a 
m × n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then 
the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

1. Choices:
- up down left right
- -1, 0, INF

2. State:
(row, col), grid

3. Base Cases:
- if -1: return
- if INF continue
- if 0: return

4. Restoration:
return since other places need 


2 Approaches to
- store the distance with each node
- process the BFS one level at a time

Time Complexity: O(m x n)
- each cell can be added to the queue once
- initial grid traversal O(m x n)
- BFS traversal O(m x n)

Space: O(m x n)
- at worst case the queue can contain all cells
BFS space depends on the maximum number of nodes waiting on the queue, not 
necessarily the total number of nodes visited

Pattern: Multisource BFS

Ivariant: when a cell is first discovered, its recorded distance is the
shortest possible distance to any treasure chest

- Find Shortest Path -> BFS
- Every movement has equal cost -> BFS can gurantee shortest distances
- Multiple starting locations -> Multisource BFS
- Find distance to the nearest source -> Consider reversing the search direction

"""

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Initialize
        queue = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        while queue:
            # Process
            row, col, distance = queue.popleft()

            # Explore
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                # Check boundries
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if grid[nr][nc] != 2147483647:
                    continue

                grid[nr][nc] = distance + 1
                queue.append((nr, nc, distance + 1))

        return grid


if __name__ == "__main__":
    grid = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
    
    ]
    sol = Solution()
    result = sol.islandsAndTreasure(grid)