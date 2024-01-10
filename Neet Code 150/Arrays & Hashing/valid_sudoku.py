'''
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according
to the following rules

1. Each Row must contain the digist 1 - 9 without
repetition
2. each column must contain the digist 1-9 without 
repetition
3. Each of the nine 9x9 sub boxes of the grid
must containthe digit 1- 9 without repetition


ONLY THE FILLED CELLS
NEED TO BE VALIDATED


# ideas:
utilize a set
- check the row
- check the column
how to split it into the 3 x 3?
utilize numpy?

board in IT's CURRENT STATE
'''
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board) -> bool:
        # default dict to have a key:set()
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r/3, c/3)

        # for every row 
        for r in range(9):
            # for every column
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                # if the current number is in the hashset of the row or column
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True

'''
Code Explanation
- skip the current value if it is a period(.)
- utilize a hash set for each row, each column, and each square
- for the row, the hash set key is the index: (set of number in row)
Example
rows = 0: 5,3,7
- for the column, we use a hash set where the key is the index and the value is a set of numbers for each column

now for the squares
the way you do it is that the key is a tuple that has a respective index 
since we have 9 3x3 cells, we can break up the sudoku board into 9 differnt cells
we do this by having a tuple key
Example:
row = 0
column = 0
squares = (0,0): 5,3,6,9,8

'''

def main():
    print()
    test_one = Solution()
    board = (
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    )
    result_one = test_one.isValidSudoku(board)
    print(result_one)

if __name__ == '__main__':
    main()


        # # row check
        # column_set = set()
        # for index,row in enumerate(board):
        #     row_set = set()
        #     for item in row:
        #         if item == '.': # only care about numbers
        #             continue
        #         if item in row_set: # duplicate violates the #1 rule
        #             return False
        #         row_set.add(item)
        # return True
        # check the columns

