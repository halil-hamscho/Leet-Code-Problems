from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            for col in range(COLS):

                val = board[row][col]
                
                if val == ".":
                    continue
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if val in boxes[(row // 3, col // 3)]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[(row // 3, col // 3)].add(val)

        return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    result = Solution().isValidSudoku(board)
    if result != True:
        print(f"bad")