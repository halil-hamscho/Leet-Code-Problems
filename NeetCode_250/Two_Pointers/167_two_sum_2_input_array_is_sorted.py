"""
Going from O(n^2) time to O(n) was by exploiting the sorted nature of the array

so left is the smallest number
right is the largest number
 based on this, we remove an endpoint in order to get to the valid pair

"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        i = 0
        j = len(numbers) - 1
        while i < j:

            current = numbers[i] + numbers[j]

            if current == target:
                return [i + 1, j + 1]

            if current < target:
                i += 1
                continue

            if current > target:
                j -= 1
                continue
                
if __name__ == "__main__":
    numbers = [-10,-8,-2,1,2,5,6]
    target = 0
    result = Solution().twoSum(numbers, target)