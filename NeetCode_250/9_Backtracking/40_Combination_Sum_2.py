"""

Pattern: 
- Backtracking (Combinations) with Duplicate Pruning
2 decision loop or for loop

Intuitions:
Same depth: each iteration of the for loop explores an alternative choice
Diff depth: each recursive call explores how to extend the current combination

Invariant: at each recursion depth, explore each distinct candidate value only once

We need to sort here since it establishes a consisnet ordering for combinations

Example:
[1, 7, 2, 6, 1]

both [1, 7] and [7, 1] can be generated

after sorting:
[1, 1, 2, 6, 7]


Time:
- Sorting O(n log n)
- Backtracking O(2^n)
- Copying: O(n)

O(n log n + n * 2^n) -> O(n (log n + 2^n)) -> simplifies to O(n * 2^n)

Space:
- recursion stack O(n)
- output result has O(2^n) combinations

O(n * 2^n)

4 Things
1. Choices
- keep curr or skip

2. State
index, 
total recursive state total

3. Base Case
- if index == len(candidates)
    exhausted the numbers

if total > target:
    - to much, break

if total == target:
    we found a good one, save

4. Restoration
path.append()
dfs()
path.pop()

"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []
        path = []
        candidates.sort()

        def dfs(index, total):

            if total == target:
                # Save
                result.append(path.copy())
                return

            seen = set()

            for i in range(index, len(candidates)):

                if total + candidates[i] > target:
                    break

                if candidates[i] in seen:
                    continue

                seen.add(candidates[i])

                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                path.pop()

        dfs(0, 0)
        return result



if __name__ == "__main__":
    sol = Solution()

    candidates = [10,1,2,7,6,1,5]
    target = 8
    result = sol.combinationSum2(candidates, target)