"""

Surround all 'O' regions by replacing with X's

1. Choices
    - up down left right
    
2. State:
    - grid

Pattern: Multisource BFS or DFS, grid traversal, boundary connectivity

Key Insight: Instead of finding surrounded regions, identify regions connected to the border that cannot be captured

Intuition: Start BFS from all border "O", mark every reachable "O" as safe, any remaining turn to "X"

Invariant: Every cell that is marked as "#" is connected to the border and must remain "O"

Time Complexity: O(R x C)
- since every cell is visited at most once during BFS, plus the board traversals

Space Complexity: O(R x C)
- for the BFS queue in the worst case

Heuristics:
- grid regions involving boundaries -> Consider starting from the borders
- need to identify enclosed regions -> consider finding the regions that are not enclosed
- need connectivity or reachability -> BFS or DFS

- Start from Cells whose status is already known, then use traversal to classify the remaining cells

"""
from collections import deque

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])

        queue = deque()

        # Upper Border
        for col in range(COLS):
            if board[0][col] == "O":
                queue.append((0, col))
                board[0][col] = "#"

        # Bottom Border
        for col in range(COLS):
            if board[ROWS - 1][col] == "O":
                queue.append((ROWS - 1, col))
                board[ROWS - 1][col] = "#"

        # Left Border
        for row in range(ROWS):
            if board[row][0] == "O":
                queue.append((row, 0))
                board[row][0] = "#"

        # Right Border
        for row in range(ROWS):
            if board[row][COLS - 1] == "O":
                queue.append((row, COLS - 1))
                board[row][COLS - 1] = "#"

        def bfs(queue, board):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                row, col = queue.popleft()

                # Explore Neighbors
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue

                    if board[nr][nc] != "O":
                        continue

                    # Mark
                    board[nr][nc] = "#"
                    queue.append((nr, nc))

        bfs(queue, board)
        # Make all surrounded O's be X's
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

                elif board[row][col] == "#":
                    board[row][col] = "O"

    
if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol = Solution()
    result = sol.solve(board)