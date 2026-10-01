"""
Pattern: Binary Search in Stages
- Find hte peak
- Binary Search the increasing side
- Binary Search the decreasing side

if array[m] < array[m + 1]: Ascending
else Descending

"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: list) -> int:

        array = mountainArr

        l = 0
        r = array.length() - 1

        while l <  r:

            m = (l + r) // 2

            if array.get(m) < array.get(m + 1):
                # ascending
                l = m + 1
            else:
                # descending
                r = m

        max_val_idx = l
        left_val = self.search(0, max_val_idx, target, mountainArr, True)
        right_val = self.search(max_val_idx + 1, array.length() - 1, target, mountainArr, False)

        if left_val == -1 and right_val == -1:
            return -1

        if left_val == -1 and right_val != -1:
            return right_val

        return left_val


    def search(self, left, right, target, mountainArr, ascending) -> int:

        l = left
        r = right

        while l <= r:

            m = (l + r) // 2

            if mountainArr.get(m) == target:
                return m

            elif mountainArr.get(m) < target:
                if not ascending:
                    r = m - 1
                    continue
                l = m + 1

            else:
                if not ascending:
                    l = m + 1
                    continue
                r = m - 1

        return -1

class MountainArray:
    def __init__(self, nums):
        self.nums = nums

    def get(self, index: int) -> int:
        return self.nums[index]

    def length(self) -> int:
        return len(self.nums)


if __name__ == "__main__":
    mountainArr = MountainArray([1, 2, 3, 4, 5, 3, 1])

    solution = Solution()

    result = solution.findInMountainArray(3, mountainArr)

    print(result)


if __name__ == "__main__":
    result = Solution.findInMountainArray(3, [1,2,3,4,5,3,1])
        