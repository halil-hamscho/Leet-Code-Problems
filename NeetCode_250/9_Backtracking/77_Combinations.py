"""

1. Choices:
- What can I decide at each step
- Eitehr include or exclude

2. State:
index, but there is a condition here len() <= k

Pattern: Backtracking with a For Loop
Intuition: we are constructing one element at a time by choosing from the remaining available candidates

Number of Valid Combinations:
( n / k ) = n! / (k! * (n - k)!)
Time: O(k * (n/k))
Space: O(k * (n/k))

We can prune by comparing
remaining numbers vs. needed numbers
if needed > remaining:
    break
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        def dfs(index):
            # Limit the depth of backtracking
            if len(path) == k:
                result.append(path.copy())
                return

            for i in range(index, n + 1):
                remaining = n - i + 1
                needed = k - len(path)

                if remaining < needed:
                    break

                path.append(i)
                dfs(i + 1)

                path.pop()
                
            return
        
        dfs(1)
        return result

if __name__ == "__main__":
    result = Solution().combine(n = 4, k = 2)