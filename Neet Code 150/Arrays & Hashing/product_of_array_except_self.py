'''
given an integer array nums, return
an array answer such that
answer[i] is equal to the product of all
the elements of nums except nums[i]
Write the algorothms that runs O(n)
without using the division operation


input a list
and then return a list
'''



class Solution:
    def productExceptSelf(self, nums):
        answer = [] 
        for index, value in enumerate(nums):
            



        return answer

def main():
    nums = [1,2,3,4]
    test_case_one = Solution()
    result = test_case_one.productExceptSelf(nums)
    print(result)

if __name__ == '__main__':
    main()
