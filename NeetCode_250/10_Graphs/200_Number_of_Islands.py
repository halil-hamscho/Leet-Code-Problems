from typing import List

"""
1. Choices:
    - up, down, left right

2. State:
    - grid
        - replace the in memory grid or extra 2D or hashset coordinates

3. Base Cases:
    - out of bounds
    - not land (0)
    - already visited

Output: Int Sum

Pattern: Grid DFS, connected components

Time: O(R x C)
since node is processed once so traversal takes O(V + E)
it is not 3^n since we are not backtracking

Space: O(R x C)
since the recursion stack can be the entire grid

Recognition: Counting disconnected regions suggests counting connected components

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        output = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col, grid):
            # Check Node
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return

            if grid[row][col] == "0":
                return
            
            if grid[row][col] == "#":
                return

            # Mark
            grid[row][col] = "#"

            # Explore
            # Up
            dfs(row - 1, col, grid)
            # Down
            dfs(row + 1, col, grid)
            # Left
            dfs(row, col - 1, grid)
            # Right
            dfs(row, col + 1, grid)

            return

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col, grid)
                    output += 1

        return output

if __name__ == "__main__":
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    sol = Solution()
    result = sol.numIslands(grid)