class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        print(f"Rows {ROWS}")
        print(f"Columns {COLS}")
        path = set() # unique path, cannot go back
        def dfs(r, c, i):
            # base cases
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or
                (r,c) in path):
                return False
            path.add((r,c)) # add word since it is valid
            # check all 4 positions
            res = (dfs(r + 1, c , i + 1) or
                   dfs(r - 1, c , i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)) # return true if any of these are true
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        # if we go through
        return False

def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "ABCCED"
    res = Solution().exist(board,word)
    print(res)

if __name__ == "__main__":
    main()