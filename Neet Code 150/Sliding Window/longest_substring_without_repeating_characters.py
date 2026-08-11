'''
What is sliding window

A sliding window algoriothm is a problem-solving technique used in computer science
and signal processing to efficiently solve problems involving arrays, string 

It involves selecting a fixed-sise subset or "window" from a larger dataset

moivng teh window throguh the dataset in a step-wise fashion and performing some operation on the elements
within the window at each step

Summary:
- A method for finding a subset of elements that satisfy a certain condition in issues


Steps:
1. Determine Window Size
2. Initialize and Process
3. Slide the window
4. Update and Evaluate
5. Continue Sliding
6. Return result


Fixed vs. Variable Size


Intuition:

Generally, questions involving sliding window techniques often
inquire about the number of subarrays or subtrings that satisfy
specific conditions


'''
# output the length of the longest substring

class Solution:
    def lengthOfLongestSubstring(self, s):
        # set allows us to have unique string logic
        character_set = set()
        l = 0
        res = 0

        # The right pointer represents the window
        for r in range(len(s)):
            # if we get to duplicate we update set and window
            while s[r] in character_set:
                character_set.remove(s[l])
                l += 1
            character_set.add(s[r])
            res = max(res, len(character_set))
        return res
    
def main():
    print()
    s = "abcabcbb"
    test = Solution()
    print(test.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()

    

