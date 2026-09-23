'''
a school is trying to take an annual photo of all the students.
The students are asked to stand in a single file line in non decreasing order by height.
Let this ordering be represented by the integer array expected
where expected[i] is the expected height of the ith student in
line. 

You are given an integer aray heights representing the current
order that the students are standing. Each height[i] is the height of the 
ith student in line 

reutn the number of indeces where heights[i] != expected[i]

'''
# height is a list
# return an integer of number of indices
# expected is the sorted array

class Solution:
    def heightChecker(self, heights):
        result = 0
        expected = sorted(heights)
        for index, value in enumerate(heights):
            if expected[index] != heights[index]:
                result += 1
        return result 

def main():
    print()
    heights = [1,1,4,2,1,3]
    test = Solution()
    print(test.heightChecker(heights))

if __name__ == '__main__':
    main()


