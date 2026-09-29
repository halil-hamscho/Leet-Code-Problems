"""
2 Sum: hashmap
2 Sum Sorted: two pointers
3 Sum: Sort, Fix a,  Two Pointers
4 Sum: Sort, Fix a, Fix b, two pointers


fix a
    fix b
        move l and r

duplicate handling

# skips first fixed values
if a > 0 and index[a] == index[a - 1]:
    a += 1
    continue

# skips second fixed values 
if b > a + 1 and index[b] == index[b - 1]:
    b += 1 
    continue
    
a move through n values
    b can move through n values for each a
        l and r move together

Time: O(n^3)
Space: O(1)
Space:

O(1) auxiliary for the algorithm itself

O(n) worst case because Python sorting may use extra memory

O(k) for the output, where k is the number of quadruplets

"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        result = []
        a = 0
        n = len(nums)
        nums.sort()

        if len(nums) < 4: # impossible quadruplets
            return []

        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]

        while a < n - 3:

            if a > 0 and nums[a] == nums[a - 1]:
                a += 1
                continue

            b = a + 1

            while b < n - 2:

                l = b + 1
                r = len(nums) - 1

                if b > a + 1 and nums[b] == nums[b - 1]:
                    b += 1
                    continue

                while l < r:

                    calculation = nums[a] + nums[b] + nums[l] + nums[r]

                    if calculation > target:
                        r -= 1
                        continue

                    if calculation < target:
                        l += 1
                        continue
                    
                    if calculation == target:

                        result.append([nums[a], nums[b], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l + 1]:
                            l += 1

                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1

                b += 1

            a += 1

        return result

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
    result = Solution().fourSum(nums, target)