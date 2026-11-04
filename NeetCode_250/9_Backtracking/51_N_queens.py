"""



Pattern: Backtracking with contraints

Recognition:

Find all valid arrangements -> Backtracking

Decisions affect future choices -> Maintain State

Each positionmust satisfy restrictions -> constraint checking

Choices can be undone -> Choose, explore, restore

Some constraints can be guranteed structurally -> Reduce the search space


Time Complexity: O(n^2 * n!)

every column the the search decreases
n(n - 1)(n - 2)... 1 = n!
O(n!) factorial

result.append(["".join(row) for row in board])
this is O(n^2) since n x n matrix

Space: O(S * n^2 + n^2)

board O(n^2)

three sets
at most n queens are placed so
O(n) for all three

stack: O(n)

For S solutions
result will have O(S * n^2)
"""
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        board = [["."] * n for _ in range(n)]

        result = []

        cols = set()
        diag1 = set() # row - col
        diag2 = set() # row + col

        def dfs(row, board):
            if row == n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):

                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Choose
                board[row][col] = "Q"

                # Explore
                dfs(row + 1, board)

                # Return
                board[row][col] = "."

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return

        dfs(0, board)
        return result



if __name__ == "__main__":
    sol = Solution()
    result = sol.solveNQueens(n =  4)