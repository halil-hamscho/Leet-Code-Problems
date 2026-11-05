"""

Pattern: Graph DFS

1. Choices:
    - up, down, left right

2. State:
    - row, col tells recursion where we are
    - board/hashset of what we have visited

3. Base Case:
    - out of bounds, or visited already
    - either 1 or 0

4. Restoration:
    - remove from hashset/undo the board


Search Space, we are trying to find the land
    

1. Modify Grid
2. 2D Array of True and False
3. Hashset of coordinates

Time: O(RC)
    Algorithm:
        1. Graph Traversal DFS: at most land cells, visited only once
        2. Grid Traversal: at most RxC cells

Space: O(RC)
    - Recursion stack: DFS can be vast and visit every land cell before returning
    - no other additional data structure

Pattern: Graph DFS with Check Mark Explore
"""

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col, grid):

            # Check (Base Cases)
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return 1

            if grid[row][col] == 0:
                return 1

            if grid[row][col] not in [0, 1]:
                return 0

            # Mark
            grid[row][col] = "#"

            # Explore
            result = 0
            result += dfs(row - 1, col, grid) # Up
            result += dfs(row + 1, col, grid) # Down
            result += dfs(row, col - 1, grid) # Left
            result += dfs(row, col + 1, grid) # Right

            return result

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return dfs(row, col, grid)


if __name__ == "__main__":
    grid = [[1,1],[1,1]]
    sol = Solution()
    result = sol.islandPerimeter(grid)    