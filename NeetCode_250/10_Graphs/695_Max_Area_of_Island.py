"""

Pattern: Graph DFS
- Invariant: Found 1, explore DFS, if cumulative sum > running sum, replace

1. Choices:
- up, down, left right

2. State:
- grid, already visited
    - hashset, a 2d boolean or inplace change

3. Base Cases:
- out of bounds
- already visited
- not land, 0

# Check, Mark, Explore

Pattern: Grid DFS with recursive aggregation

- in this case, the Mark is simply area = 1 since each recursive
call constributes the area discovered in that direction
returing area propogrates the accumulated count back to the caller

Python Concept: return recursive values instead of nonlocal

"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        max_area = 0
        def dfs(row, col, grid):
            # Check
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return 0

            if grid[row][col] == 0:
                return 0

            if grid[row][col] not in [0, 1]:
                return 0

            # Mark
            grid[row][col] = "#"
            area = 1

            # Explore
            area += dfs(row - 1, col, grid)
            area += dfs(row + 1, col, grid)
            area += dfs(row, col - 1, grid)
            area += dfs(row, col + 1, grid)

            return area
            

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col, grid))

        return max_area

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    result = sol.maxAreaOfIsland(grid)
