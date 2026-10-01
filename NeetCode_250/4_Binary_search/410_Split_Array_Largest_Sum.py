"""
Pattern: Binary Search on the answer (searching the smallest numeric value that makes some condition feastible)

Time: O(n log(s)) where s is sum(nums) - max(nums)
Space O(1)

Recognition Heuristic:
Optimization over a number -> find natural lower and upper bounds -> imagine a candidate answer -> write a yes or no
feasibility check -> verify monotonicity -> binary search the first feasible value

"""

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)

        result = r

        while l <= r:

            candidate_max = (l + r) // 2 # sum capacity

            current_sum = 0
            current_sub_arrays = 1
            for n in nums:

                if current_sum + n > candidate_max:
                    current_sub_arrays += 1
                    current_sum = n
                else:
                    current_sum += n

                if current_sub_arrays > k:
                    break

            if current_sub_arrays > k:
                # too many sub arrays
                l = candidate_max + 1
            else:
                result = min(result, candidate_max)
                r = candidate_max - 1

        return result

if __name__ == "__main__":
    nums = [7,2,5,10,8]
    k = 2
    result = Solution().splitArray(nums, k)