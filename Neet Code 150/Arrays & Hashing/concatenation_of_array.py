'''

Given an integer array nums of length n
you want to create an array ans of length 2n where 
ans[i] == nums[i] and ans[i + n] == nums[i] for 0<= i < n

specificaly, ans is hte concatenation fo two nums array

return array ans

Brainstorm:

we are basically duplicating the array twice
'''


class Solution:
    def getConcatenation(self, number_list):
        # loop through nums
        length = len(number_list)
        for i in range(length):
            number_list.append(number_list[i])
        return number_list

    '''
    or you can just do :
    return nums + nums

    or 
    return nums * 2
    '''
def main():
    nums = [1,2,1]
    test = Solution()
    print(test.getConcatenation(nums))

if __name__ == '__main__':
    main()
