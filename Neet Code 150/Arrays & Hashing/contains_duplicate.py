'''
Given an integer array 'nums' return true if any value
appears at least twice in the array and return false if 
every element is distinct
true = element appears twice
false = every number is distinct


My immediate thoughts:
- use a hash table
- store every single number
- then if the number is greater than 1 then it is true

'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_table = {}
        for number in nums:
            # if the number is IN THE TABLE, this already tells me it is a duplicate
            if number in num_table:
                return True
            else:
                num_table[number] = 1
        return False
    # theoretically, if all the numbers are distinct, then all of them
    # will have a 1 as a value
    
def main():
    test_case_one = [1,2,3,1]
    one = Solution()
    result = one.containsDuplicate(test_case_one)
    print()
    print(result)

if __name__ == '__main__':
    main()