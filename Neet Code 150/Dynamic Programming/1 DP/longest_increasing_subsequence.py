"""
Note:
We can utilize a greedy approach paired with binary search to 
obtain
Time: O(N * logN)
Space O(N)

"""

"""
Classic Dynamic Programming Solution
let dp[i] be the longest increase subsequence 
Time O(n^2)
Space O(n)
We solve it iteratively, where we use a dp array where dp[i] denotes the LIS ending at index i. 
We can always pick a single element and hence all dp[i] will be initialized at 0

For each element nums[i], if there is an smaller element nums[j] before it, the result
will be the maximum of current LIS length ending at i: dp[i] and LIS ending at that j + 1: dp[j] + 1. we say
+ 1 here because we are including the current element and extending teh LIS ending at j
"""
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    #  Ensure that the result d[i] is not influenced by the history of other non-optimal solutions
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

def main():
    nums = [10,9,2,5,3,7,101,18]
    result = Solution()
    print(result.lengthOfLIS(nums))

if __name__ == "__main__":
    main()