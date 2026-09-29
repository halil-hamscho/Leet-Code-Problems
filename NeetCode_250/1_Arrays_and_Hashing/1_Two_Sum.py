"""

From what I remmember about Two Sum is that 
- pointer problem for the O(n^2) solution since we have to go through the list twice
I know there is. afaster way, where we subtract the target by an index or something

nums[i] + nums[j] = target
rearrange
target - nums[i] = nums[j]

While Loop solution
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result
                j += 1
            i += 1
Brute Force Solution, nested iteration over every possible pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result

Okay so with the hashmap solution, we need to think about
# number I have seen, index where I last saw it

the key here is using the hashmap as a look up of previous numbers we have seen
"""


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # look up of Keys is O(1), key: number I saw, it's index
        hashMap = {}
        for i, num in enumerate(nums):
            num_j = target - num
            if num_j in hashMap:
                result = [hashMap.get(num_j), i]
                return result
            else:
                hashMap[num] = i

if __name__ == "__main__":
    nums = 3,2,4
    target = 6
    output = [1, 2]
    result = Solution().twoSum(nums, target)
    if result != output:
        print("You failed")
    else:
        print(f"Output: {output}, Result: {result}")