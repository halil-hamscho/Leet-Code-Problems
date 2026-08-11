class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def capture(r,c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != "O"):
                return
            # found a border O
            board[r][c] == "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Phase 1, change all the unsurrounded O's to T
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r,c)
        
        # Phase 2, change all the surrounded O's to X's and all the T's back to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"