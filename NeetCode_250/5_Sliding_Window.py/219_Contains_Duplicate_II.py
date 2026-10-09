"""
Hint here is that we want a window of |i - j| <= k

This automatically should tell us to use a sliding window approach,
in this case the hashmap stores the most recent index
value -> most recent index
and then we ask whether that index is still within distance k

"""
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        seen = {} # value: index

        for index, num in enumerate(nums):
            if num in seen and index - seen[num]  <= k:
                return True
            seen[num] = index

        return False


if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    result = Solution().containsNearbyDuplicate(nums, k)