from typing import List

"""
Pattern: Backtracking with Combinations

Establish 4 things before coding
1. Choices: What can I decide at each step?
- include the curr candidate
- skip the curr candidate

2. State: What information represents my current progress?
index: curr candidate
total: curr sum
path: curr nums so far

3. Base Case: When have I completed a valid possibility?
total == target: we found valid combination 
total > target: we exceeded the target
index == len(candidates): we exhausted our candidates

4. Restoration: What must I undo before exploring another choice?
pop from path


Time Complexity:
Recursion Tree at most O(2^d)
where
d = T / m + n

copying a path takes O(T/m) time in the worst case because that's the max number
of elements in a valid combination

Upper Bound
O(T/m * 2^(T/m + n)) exponential bound

We are exploring a recursion tree, not simply running two nested loops

Space:

1. Recursion Stack: At most O(T/m + n) calls
2. Current Path: at most O(T/m) elements

Excluding the output
O(T/m + n)

Lesson: Recursion complexity depends on how many calls are made and how deep those
calls can go, not simply the length of the input array

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        path = []
        def dfs(index, total):
            if total == target:
                result.append(path.copy())
                return

            if total > target:
                return

            if index == len(candidates):
                return

            # Add to Path
            path.append(candidates[index])
            dfs(index, total + candidates[index])

            # Skip Num
            path.pop()
            dfs(index + 1, total)

            return

        dfs(0, 0)
        return result

if __name__ == "__main__":        
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    result = sol.combinationSum(candidates, target)
    print(result)