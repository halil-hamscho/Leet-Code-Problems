

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(row, col):

            # Check (Base Cases)
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return 1

            if grid[row][col] == 0:
                return 1

            if (row, col) in visited:
                return 0

            # Mark
            visited.add((row, col))

            # Explore
            result = 0
            result += dfs(row - 1, col) # Up
            result += dfs(row + 1, col) # Down
            result += dfs(row, col - 1) # Left
            result += dfs(row, col + 1) # Right

            return result

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return dfs(row, col)


if __name__ == "__main__":
    grid = [[1,1],[1,1]]
    sol = Solution()
    result = sol.islandPerimeter(grid)    