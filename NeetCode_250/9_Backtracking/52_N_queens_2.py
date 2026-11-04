"""
Pattern: Backtracking with Constraints

- N Queens 2 is different from N Queens 1 since we only count all valid arrangements

Both use exactly the same search tree, constraints and pruning

In N Queens 2, the three sets are sufficient to explore the search tree, we don't need an actual board



"""

class Solution:
    def totalNQueens(self, n: int) -> int:

        result = 0
        cols = set()
        diag1 = set() # row - col
        diag2 = set() # row + col

        def dfs(row, board):
            if row == n:
                nonlocal result
                result += 1
                return

            for col in range(n):

                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                # Choose
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Explore
                dfs(row + 1, board)

                # Return

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return

        dfs(0)
        return result

if __name__ == "__main__":
    sol = Solution()
    result = sol.totalNQueens(n=4)