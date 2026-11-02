"""
1. Choices:
    Which unused number goes next?

2. State:
    - current path and used numbers

3. Base Case:
    - All numbers have been selected

4. Restoration:
    - remove the last number from path and used


Main Pattern: Backtracking (Permutations)
Unlike subsets and combinations, permutations care about the order of elements

Combinations restrict which indices can be visited next

permitations allow every index to be considered, but restruct which elements can be reused

Time: O(n x n!)

n! permutations, each copying is O(n)

Space: O(n x n!)

Auxiliary: recursion stack, path, and used each is O(n)

if input contained duplicate values such as [1,1,2] the value based used set would not work
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []
        path = []
        used = set()
        def dfs():
            # Base Case
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                path.append(num)
                used.add(num)
                dfs()

                path.pop()
                used.remove(num)

            return

        dfs()
        return
    



if __name__ == "__main__":
    sol = Solution()
    result = sol.permute(nums = [1,2,3])