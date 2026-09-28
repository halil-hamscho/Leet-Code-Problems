"""

Pattern: 
- Sort
- Greedy (if calc > limit, heaviest gets a boat, move r -= 1)
- two pointer approach

Time: O(n log n) due to sorting
Space: O(1)

"""


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0

        while l <= r:

            calc = people[r] + people[l]

            if calc > limit:
                r -= 1
                boats += 1
                continue
            else:
                l += 1
                r -= 1
                boats += 1

        return boats
                

if __name__ == "__main__":
    people = [3,5,3,4]
    limit = 5
    result = Solution().numRescueBoats(people, limit)