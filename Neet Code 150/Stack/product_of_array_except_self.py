class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # does not count as extra memory
        # prefixes
        # one pass to calculate the prefix
        prefix = 1
        for index, value in enumerate(nums):
            res[index] = prefix
            prefix *= nums[i] # prefix * current number
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = postfix * res[i] # multiplying prefix and postfix
            postfix *= nums[i]
        return res