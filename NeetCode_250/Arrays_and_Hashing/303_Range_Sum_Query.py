from typing import List

"""
Range_Sum_Query is essentially prefix sum, where we need to have an array that keeps tally of the additions

the edge case here is when we want left to be from the start
in this case, we don't have to subtract anything since the prefix takes care of the addition for us

        if left <= 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]

there is the edge case if we want everything from left being 0 to right, we just return right

however, we can remove this edge case by just adding a 0


"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:

        if left <= 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left - 1]

if __name__ == "__main__":
    result = NumArray([-2, 0, 3, -5, 2, -1])
    for left, right in [[0, 2], [2, 5], [0, 5]]:
        print(f"{result.sumRange(left, right)}")
