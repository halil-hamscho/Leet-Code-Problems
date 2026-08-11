'''
Will use a monotonically Decreasing Deque

Can use the import collections module from python


# we check if the number at r pointer is > the number to it's left
if so then we pop from the queue until the value to the left is > r
then we append that index

The tricky thing here is that we are storing indices in the queue not actual values

Dequeue is always going to be in decreasing order (index of nums)

Time Complexity: O(N)
Space Complexity: O(K)



'''


import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        l = r = 0
        q = collections.deque() # contain indices

        while r < len(nums):
            # while deque is true (non empty) and smaller values exist from our queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # after we have the largest at the leftmost
            q.append(r)

            # if the left value is out of bounds
            if l > q[0]:
                q.popleft()

            # Move the window once the right pointer 
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        return output
    

def main():
    print()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    test = Solution()
    print(test.maxSlidingWindow(nums,k))

if __name__ == "__main__":
    main()