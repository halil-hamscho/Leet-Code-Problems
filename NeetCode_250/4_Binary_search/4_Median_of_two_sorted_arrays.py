"""

Intuition: binary search the partition position in the smaller array

Once we choose i in A, the partition B is forced -> j = half - i
and we only need to search one dimension

Searching smaller array gives O(log(min(m,n)))

Deeper Idea is that we are not trying to locate the median directly. We are trying to locate
the correct split, and once the split is correct, the median is determined by the four values
touching that split

Partition Correct when

A_left <= B_right and B_left <= A_right

Move Direction
- A_left > B_right:
    too much from A, move left r = i - 1

- B_left > A_right:
    too much from B, move right l = i + 1

i is the count, not the index

Python Trick when avoid special casing boundaries

float("inf") and float("-inf")
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        A , B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A)

        while l <= r:

            i = (l + r) // 2
            j = half - i

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < len(A) else float("inf")

            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                # correct partition
                if total % 2 != 0: # odd
                    return min(A_right, B_right)
  
                return (max(A_left, B_left) + min(A_right, B_right)) / 2 # even

            if A_left > B_right:
                # partition is too big
                r = i - 1

            elif B_left > A_right:
                # partition too small
                l = i + 1
        



if __name__ == "__main__":
    nums1 = [1, 4, 7]
    nums2 = [2, 3, 8]

    solution = Solution()
    result = solution.findMedianSortedArrays(nums1, nums2)

    print(result)