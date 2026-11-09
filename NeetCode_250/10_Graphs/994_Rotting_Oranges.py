from collections import deque

"""
Pattern: Multi Source DFS


1. Choices:
    - 0 empty
    - 1 fresh
    - 2 rotten

2. State:
    - row, col
    , time, it can also be distance 

Time Complexity: O(RC)
    - Scan the entire grid: O(RC)
    - BFS Traversal, each node is added to the queue once O(RC), 4 directions is constant work

Space Complexity: O(RC)
- the queue can have all nodes if all 1   

Recognition:
we have multiple starting points spreading simultanously

Why BFS?
we need the minimum time for something to reach every reachable target

- Mark oranges when enqueing, not when dequeing

Similar to 286 Walls and Gates: record each cell's minimum distance. In Rotting Oranges
you care about the max time neede to reach all fresh oranges

Note: you can do grid[nr][nc] = 2 to change or signify rotten, rather than keeping a visited array
"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        fresh_count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_count += 1

                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        if fresh_count == 0: # no fresh oranges
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)

            # Explore Neighbors
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue

                if grid[nr][nc] != 1:
                    continue

                grid[nr][nc] = 2
                queue.append((nr, nc, time + 1))
                fresh_count -= 1

        return minutes if fresh_count == 0 else -1

if __name__ == "__main__":
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    sol = Solution()
    result = sol.orangesRotting(grid = [[0]])



