"""
Time: O(n * n!)

Space: O(n * n!)
it is O(n^2) auxiiary space comes from creating a separate seen set
at each recursive depth

- Recursion Stack: O(n), max depth n
- Path: O(n) curr permutation
- Used Array: O(n)
- Local seen set: O(n^2)

Since each active recursive call has its own seen set
n + (n - 1) + (n - 2) + ... + 1 = (n (n + 1)) / 2


Pattern: Backtracking with duplicate elimination

Takeways:

1. No DFS state arguments: path and used array maintain the state, depth is len(path)

2. Used boolean arary to track indices, that way we avoid using the same element in our current permutation

3. local seen set. We avid choosing the same value multiple times in the same recursive depth

4. backtracking: after exploring a choice, we need to path.pop() and used[i] = False

5. No sorting required
"""


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:

        result = []
        path = []
        used = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            seen = set()
            for i, num in enumerate(nums):
                if used[i]:
                    continue

                if num in seen:
                    continue

                used[i] = True
                seen.add(num)
                path.append(num)
                
                dfs()

                used[i] = False
                path.pop()

            return

        dfs()
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    result = sol.permuteUnique(nums)


                


        