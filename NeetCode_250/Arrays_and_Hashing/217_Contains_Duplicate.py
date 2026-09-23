from typing import List

"""
remmeber that the key lookup for dictionaries is O(1) basically, so
if you want uniqueness use the key to your advantage

if n not in hashMap.values():
                hashMap[i] = n


now lets try using a set
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for i, n in enumerate(nums):
            if n in seen:
                return True
            seen.add(n)
        return False

if __name__ == "__main__":
    input = [1,2,3,1]
    output = True
    result = Solution().containsDuplicate(input)
    if result != output:
        print(f"Bad Job")
        print(f"Output: {output}, Result: {result}")
    else:
        print("Good Job")
        print(f"Output: {output}, Result: {result}")
