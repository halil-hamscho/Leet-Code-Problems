"""
Pattern: Graph DFS on a 2D Grid
- Treat each pixel as a node and its four adjacent pixels as neighbors

- Check -> Mark -> Explore

Intuition:
Since we want to modify an entire connected region, not just individual pixels

1. Choices:
    - adjacent, up down left right

2. State:
    - the previous color at image[sr][sc]
    - image

3. Base Case:
    - found same color, unvisited
    - found diff color

Time: O(RC)
- DFS on the whole grid

Space: O(RC)
- recursion stack can expand the whole grid

"""

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        original_color = image[sr][sc]

        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(row, col, image):
            # Check is node valid

            if not (0 <= row < ROWS and 0 <= col < COLS):
                return
            
            if visited[row][col]:
                return
            
            if image[row][col] != original_color:
                return

            # Mark
            visited[row][col] = True
            image[row][col] = color

            # Explore
            dfs(row - 1, col, image) # Up
            dfs(row + 1, col, image) # Down
            dfs(row, col - 1, image) # Left
            dfs(row, col + 1, image) # Right

            return

        dfs(sr, sc, image)

        return image
            
if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1 
    sc = 1 
    color = 2
    sol = Solution()
    result = sol.floodFill(image, sr, sc, color)