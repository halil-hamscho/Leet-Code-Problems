"""

read finds a value that is not val
copy it into nums[write]
everything before write is already valid and should remain

- write only advances when we want to keep an element that we want to keep
- next avalable index is the number of items stored

Everything before write is a value worth keeping

read, write = 0, 0
while read < len(nums):
    read_element = nums[read]

    if read_element != val:
        nums[write] = read_element
        read += 1
        write += 1
        continue

    read += 1
return write
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read, write = 0, 0
        while read < len(nums):
            read_element = nums[read]

            if read_element != val:
                nums[write] = read_element
                read += 1
                write += 1
                continue

            read += 1
        return write

        

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    output = 2
    result = Solution().removeElement(nums, val)
    if result != output:
        print(f"bad")
