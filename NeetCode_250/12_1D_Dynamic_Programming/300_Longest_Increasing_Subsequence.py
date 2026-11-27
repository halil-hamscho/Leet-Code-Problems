"""
Decisions:
    - extend if increasing (i > i - 1)
    - start new

Base Case:
    - every element forms a subsequence of len 1

State:
    - dp[i] = longest increasing sequence ending at nums[i]

Recurrence:

    - dp[i] = max(eligible items)

Here:

    n states
        at every i state, we have to search through the eligible states and find the max

        O(n^2) inherently

Pattern: DP with variable predecessor dependencies

Takeaway: Since we need to check all previous states, DP will not be O(n)
"""
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * (n)

        for index in range(n):

            # Check Eligible Items
            curr_max = 0
            for i in range(index):
                if nums[index] > nums[i]:
                    curr_max = max(curr_max, dp[i])

            dp[index] += curr_max

        return dp[n]

    def other(self, nums):

        n = len(nums)
        dp = [1] * (n)

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def binarySearchLIS(self, nums):

        """
        Rather than asking
        DP -> what is the longest subsequence ending at each element?
        Optimized -> what is the smallest ending value we can achieve for each subsequence length

        index 
        subsequence length
        smallest possible value

        State: smallest ending value for each subsequence length
        Decisions:
            - append to increase subsequence
            - replace the smallest value for an existing subsequence length

        Time: O(n log n)
        Space: O(n)

        Intuition:
            For 2 increasing subsequences of the same length, the one with the smaller
            ending value provides more opportunities for future growth

        Since the DP states become expensive, ask yourself whether you can retain only the most useful information 
        from those states

        - We eliminated the n search of candidates by maintaining the smallest ending value for each length

        Redefine the state rather than optimizing the recurrence
        """

        tails = [] # the smallest ending value
        for num in nums:
            index = bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num

        return len(tails)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    sol = Solution()
    result = sol.binarySearchLIS(nums)