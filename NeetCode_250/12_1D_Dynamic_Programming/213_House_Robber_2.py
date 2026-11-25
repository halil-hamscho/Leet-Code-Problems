"""

Problem Reduction of endpoints leads to 2 Ranges 
- exclude last house: 0 to n - 1
- exclude first house: 1 to n

2 House Robber Iterations

Time: O(n)
Space: O(1)
"""


class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)

        def rob_linear(start, stop):

            prev1 = 0
            prev2 = 0
            result = 0
            for i in range(start, stop):
                result = max(prev1, prev2 + nums[i])

                prev2, prev1 = prev1, result

            return result

        r1 = rob_linear(0, n - 1)
        r2 = rob_linear(1, n)
        return max(r1, r2)




if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    result = sol.rob(nums)