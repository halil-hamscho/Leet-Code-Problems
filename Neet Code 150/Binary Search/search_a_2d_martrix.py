'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Brainstorming:
okay so we are searching, and the best searching algorithm is Binary Search

- since it is a m * n matrix
- do a pointer on the starting points of each row

Brute Force:
double loop that looks for every single value

We can do better
- Since the 2D matrix is sorted we can use Binary Search
For one row, the binary search is log n
then we do this log n M times so m log n

We can do better
- since each row itself is sorted
- do a binary search on the first and last integers of the rows (smallest and greatestr)
we do log m + log n
'''


class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        toprow_pointer , bottomrow_pointer = 0, ROWS - 1
        while toprow_pointer <= bottomrow_pointer:
            # Compute the middle row
            row = (toprow_pointer + bottomrow_pointer) // 2
            if target > matrix[row][-1]: # is the target value larger than the largest value in the row
                toprow_pointer = row + 1
            elif target < matrix[row][0]: # if the target value is smaller than the smallest value 
                bottomrow_pointer = row - 1
            else:
                # this else means that the target falls within that row
                break
        # if not (toprow_pointer <= bottomrow_pointer):
        #     return False
        
        # now search through the row
        row = (toprow_pointer + bottomrow_pointer) // 2
        l, r = 0, COLS - 1
        while l <= r:
            middle_point = (l + r) // 2
            if target > matrix[row][middle_point]:
                # search towards the right
                l = middle_point + 1
            elif target < matrix[row][middle_point]:
                r = middle_point - 1
            else:
                return True
        return False # never found the target value 


def main():
    print()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    test = Solution()
    print(test.searchMatrix(matrix,target))

if __name__ == "__main__":
    main()