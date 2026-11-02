"""


We need to sort 
Mental Heuritic:
    1. Sorting prevents different orderings of the same subset
    2. Local used set prevents duplicate branches of the same depth

Time: O(n * 2^n)
- sorting O(n log n)
- backtracking O(2^n)
- copying O(n)

Space: O(n * 2^n)
- stack O(n)
- output: O(2^n)
- sets: O(n^2)

We use a local seen set to prevent duplicate choices
at the same recursive depth

1. Same depth: skip duplicate values because they would generate identical brancehs
2. Deeper recursion: Allow duplicate values that may form valid subsets such as [2,2]

Pattern: Backtracking with duplicate elimination
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        nums.sorted()

        def dfs(index):
            result.append(path.copy())

            used = set()
            for i in range(index, len(nums)):
                if nums[i] in used:
                    continue
                
                path.append(nums[i])
                used.add(nums[i])
                dfs(i + 1)
                path.pop()

            return

        dfs(0)
        return result
            


if __name__ == "__main__":
    sol = Solution()
    result = sol.subsetsWithDup(nums = [1,2,2])