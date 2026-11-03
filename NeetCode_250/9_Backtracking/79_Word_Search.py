"""

Recursive Function
1. is row, col inside board
2. does board[row][col] match word[index]
3. have we matched the entire word


# Up
up = dfs(row - 1, col, index + 1)

# Down
down = dfs(row + 1, col, index + 1)

# Left
left = dfs(row, col - 1, index + 1)
            
# Right
right = dfs(row, col + 1, index + 1)


Time: O(R x C x 3^L)
The reason it is 3^L and not 4^L is because the first cell has up to 4 directions, but every
subsequent cell has at most 3 valid directions because we cannot revisit the cell we just came from

Space: O(L)
the recursive stack at most is the length of the word

6 Most Important Lessons:

1. The board itself can track visited cells. You don't need a separate data structure

2. Restore state after recursion. 

3. Pass only the necessary state.(row, col, index) contains everything necessary to describe the current search position

4. Use short circuit evaluation
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        def dfs(row, col, index):
            # Base Case
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return False

            if board[row][col] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True
            
            temp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row - 1, col, index + 1)
                or dfs(row + 1, col, index + 1) 
                or dfs(row, col + 1, index + 1) 
                or dfs(row, col - 1, index + 1)
            )

            board[row][col] = temp
            
            return found

        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False
if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    sol = Solution()
    result = sol.exist(board, word)