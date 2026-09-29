"""
2 ways to solve this

1. Use 2 Binary Searches
- since every first index is sorted, we can binary search to find the row
- once we have the row, we can binary search again through the columns

2. Use 1 binary seach
- flatten the array
- rows = mid // COLS
- cols = mid % COLS
Reason: COLS define the boundaries between each row interval

"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:


        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:

            m = (l + r) // 2

            if matrix[m // COLS][m % COLS] == target:
                return True
            elif matrix[m // COLS][m % COLS] < target:
                l = m + 1
            else:
                r = m - 1

        return False

    def searchMatrix_2_Binary_Searches(self, matrix: list[list[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1
        while l <= r:

            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        index = l - 1
        if index < 0:
            return False

        l = 0
        r = len(matrix[index]) - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    result = Solution().searchMatrix(matrix, target)