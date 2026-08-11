import statistics

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # Easy Solution
        # return statistics.median(sorted(nums1 + nums2))

        # Time Complexity is the log of the minimum
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True: # guranteed a median
            # middle of array A
            i = (l + r) // 2
            # pointer for B
            j = half - i - 2 # get the left index partition of B, need to subtract by 2 bcz of index starts at 0

            # A lot of these indeces can be out of bounds
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity") # adjacent
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Left partition for both are correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright,Bright) # Ex. min(4,infinity) 
                # even
                return max(Aleft, Bleft) + min(Aright, Bright) / 2
            elif Aleft > Bright: # a left is too big, too many
                r = i - 1 # reduce the size of the left partition
            else:
                l = i + 1
            
def main():
    print()
    test = Solution()
    nums1 = [1,3]
    nums2 = [2]
    print(test.findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()