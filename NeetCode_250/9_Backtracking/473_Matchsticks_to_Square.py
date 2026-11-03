"""

Pattern: Backtracking with assignment to groups

Hint 1: Can we treat the matchsticks array into 4 parts and try all of them

1. Choice: assign matchstick to one of 4 sides

2. State: current matchstick index, four side lengths

3. Base Case: every matchstick assigned

4. Restoration: subtract the matchstick after an unsuccessful branch

Pruning:
- Skip assignments that exceed the target

Optimization:
- Sort decending to process restrictive choices first
- Use seen to avoid equivalent side lengths

Time: O(4^n)
- 4 choices, n numbers
- at every recursive loop we do constant work (no copy)
- sorting O(n log n), exponential dominates

Space: O(n)
Recursive Stack: O(n)
Set at most 4 elements so O(1)

The loop iterates through available destinations, while the recursive index tracks the elements being assigned

Recognition Heuristic: when a problem asks you to partition elements into a fixed number of groups subject to constraints, 
consider assigning elements to groups through backtracking

Time:
4 choices, 
"""

class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4
        if max(matchsticks) > target:
            return False

        matchsticks.sort(reverse=True)

        sides = [0] * 4
        def dfs(index, sides):
            if index == len(matchsticks):
                return True

            seen = set()
            for i in range(4):

                if sides[i] + matchsticks[index] > target:
                    continue

                if seen[i] in seen:
                    continue

                seen.add(seen[i])

                # Choose
                sides[i] += matchsticks[index]

                # Explore
                if dfs(index + 1, sides):
                    return True

                # Restore
                sides[i] -= matchsticks[index]

            return False

        return dfs(0, sides)


if __name__ == "__main__":
    sol = Solution()
    result = sol.makesquare(matchsticks=[1,1,2,2,2])
        