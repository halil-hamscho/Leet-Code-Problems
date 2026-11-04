"""
Pattern: Backtracking with group/partitions 

This problem is a generalization of 473 Matchsticks to Square
instead of 4 groups, we have k groups so

target = total / k

Every number is assigned once, and no group's sum exceeds the target

1. Choice:

2. State:

3. Base Case:

4. Restoration

Time Complexity: O(k^n)
since we have k choices n times

Sorting adds O(n log n), but the exponential dominates

Space: O(n + k)

stack: O(n)
groups array: O(k)
seen set: O(k) per active recursion
sorting O(n) worst case

3 Optimizations
1. Sort Descending: Place larger numbers first to expose invalid assignments earlier
2. Prune: never allow a group to exceed target
3. Symmetry elimination: avoid assigning the same number to groups that have identical sums

The seen set tracks group sums, not indices. Two groups with the same sum are interchangeable at that recursion level

Recognition Clue:
- Assign every element to one of several groups while satisfying capacity constraints
"""


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        if max(nums) > target:
            return False
        
        groups = [0] * k
        nums.sort(reverse=True)

        def dfs(index):
            if index == len(nums):
                return True

            seen = set()
            for i in range(k):
                if groups[i] + nums[index] > target:
                    continue
                if groups[i] in seen:
                    continue

                seen.add(groups[i])

                # Choose
                groups[i] += nums[index]

                # Explore
                if dfs(index + 1):
                    return True

                # Return
                groups[i] -= nums[index] 

            return False

        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    result = sol.canPartitionKSubsets(nums=[4,3,2,3,5,2,1], k=4)
    print(result)