"""
Pattern: Binary Search with Condition
- find the minimum capacity, it is also monotonic in the sense
if capacity C works, every capacity C greater should work

l = max(weights) since the smallest possible capacity needs to carry the package
r = sum(weights) guranteed to work because everything could be shipped in one day

- Find the boundaries
- Understand the search space and the condition
-> Perform Binary Search

Time: O(n log (S))
Where S = sum(weights) - max(weights)
we are doing a search in the boundaries, n times

"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        l = max(weights) # smallest capacity that could work
        r = sum(weights) # guranteed upper bound

        result = r

        while l <= r:

            capacity = (l + r) // 2

            current_weight = 0
            days_used = 1
            for w in weights:

                if current_weight + w > capacity:
                    days_used += 1
                    current_weight = w
                else:
                    current_weight += w

                if days_used > days:
                    break

            if days_used > days:
                # capacity small
                l = capacity + 1
            else:
                result = min(result, capacity)
                r = capacity - 1

        return result
                
    
if __name__ == "__main__":
    weights = [3,3,3,3,3,3]
    days = 2
    result = Solution().shipWithinDays(weights, days)
