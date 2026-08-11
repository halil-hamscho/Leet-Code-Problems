class Solution:
    def solveNQueens(self, n: int):
        ans = []
        board = []
        for _ in range(n):
            row = "." * n # Ex. [., ., ., .] 4 
            board.append(row) # appending 4 rows of [., ., ., .]
        self.solve(0, board, ans, n)
        return ans
    
    def solve(self, col, board, ans, n):
        if col == n: # This calls after we finish adding to the last column
            ans.append(list(board))
            return
        
        for row in range(n): # For every row 
            if self.isSafe(row, col, board, n):
                # we are adding at that specific row, at that specific column
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(col+1, board, ans, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:] 
    
    def isSafe(self, row, col, board, n):
        # we are adding from left to right
        duprow = row
        dupcol = col

        # Upper Diagonal 
        # row and column both approach 0
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        col = dupcol
        row = duprow
        # Straight Left
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        
        # need to update these values every time
        col = dupcol
        row = duprow
        # Bottom Diagonal
        while row < n and col >= 0:
            if board[row][col]== "Q":
                return False
            row += 1
            col -= 1
        
        return True # checking all 3 directions


def main():
    result = Solution()
    num = 4
    print(result.solveNQueens(num))

if __name__ == "__main__":
    main()