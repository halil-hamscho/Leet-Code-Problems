"""
or

nums1[m:] = nums2
nums1.sort()

i = largest remaining nums1
j = largest remaining nums2
k = everything to the right of k is already sorted
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:

            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
                continue

            if nums2[j] > nums1[i]:

                nums1[k] = nums2[j]

                j -= 1
                k -= 1

                continue

            nums1[k] = nums1[i]
            i -= 1
            k -= 1





if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    result = Solution().merge(nums1, m, nums2, n)