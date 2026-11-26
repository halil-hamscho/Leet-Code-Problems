"""

Contigous Subarray

Decisions:
    - start a new subarray
    - continue

2 extremes
    - curr_min
    - curr_max

curr_max = maximum product ending at the current index
curr_min = minimum product ending at the current index
result = maximum product seen so far

condensing information into two extremes

Pattern: Kadene's algorithm variation with two DP states

Key Insight: Negative multiplication reverses ordering

General Takeaway: Preserve the information that future decisions can turn into an optimal result

new_max = max(curr_max * num, curr_min * num, num)
new_min = min(curr_max * num, curr_min * num, num)

Since multiplying by a negative number reverses the ordering of previous products. We need to preserve both extremes

Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max = curr_min = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            curr_max, curr_min = (
                max(num, curr_max * num, curr_min * num), 
                min(num, curr_max * num, curr_min * num)
            )

            result = max(result, curr_max)

        return result

if __name__ == "__main__":
    nums = [2, 3, 0, -2, 4]
    sol = Solution()
    result = sol.maxProduct(nums)

        