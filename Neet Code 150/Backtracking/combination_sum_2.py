'''
Given a collection of candidate numbers
(candidates) and a target number (target) find all
unique combinations in candidates where the candidate
numbers sum to target

Each numb in candidates may only be used once in combination

Combinations -> numbers can only be used once in a combination


In the previous Combination Sum, the numbers were not sorted


Sorting is always an observation you should think of when encountering any problem
THe problem statement could require to get rid of a duplicate

When O(N) solution is not possible

Each Number in C can only be used once in the combinations
Must not contain duplicate combinations

The intuition is that we must sort before hand

for example, a combination example is 1,1,6 

Okay so basically 
- sort the candidates
- our recursion trick is the following

we skip duplicate combinations by not acting on recursion leaf nodes that have the same number as the previous lead node
also stop calling recursion when we know the recursion call will never be a valid combination as the next number is greater than 

Whenver the target 0 is called, then it is carrying a combination

If target < next value -> not valid recursion call

Starting at a tree level
from left to right
see if the node on the left has the value that you will append on the current node
if so, then skip


Initialy starting with 
f(index, target, [] <- datastructure)

at the 0 index, can we pick the 0 index to the end?
when we are in the first, we go from 1st to last
when ....... 

looping from index to n -1
Whenever 
- possible, add comb to 
ds.add(candidates[i])
f(i + 1, target - candiates[i], ds, ans)

whatevever we added, we need to remove
ds.remove(candidates[i])

if I am looping and some case, the candidates[i] > target, we just return


Base case:
if target is 0:
    add to ans[ds]

if we pick 0th index and it has one
and the next index also has a one, we skip
only pick the FIRST TIME number 

N unique elements Total Combinations 2 ^ N for recursion
TC - > 2^N x K
assuming SC k x x
'''

class Solution:
    def __init__(self):
        self.ans = [] # initializing the answer

    def find_combinations(self, index, target, array, ds):
        # base case
        if target == 0:
            self.ans.append(ds.copy())
            return # go back to root node
        for i in range(index, len(array)): # Ex. from 0 to 5 not inclusive
            if (i > index and array[i] == array[i-1]):
                continue # skip the current iteration of the loop by avoiding if the current element is the same as the previous one
            if (array[i] > target):
                break # this is a faulty combination, break entirely
            ds.append(array[i])
            self.find_combinations(i+1, target - array[i], array, ds)
            ds.pop() # this helps us backtrack

    # This method is in charge of actually calling the functionality    
    def combinationSum2(self, candidates, target):
        candidates.sort() # we need to sort first
        self.find_combinations(0, target, candidates, [])
        return self.ans

def main():
    res = Solution().combinationSum2([10,1,1,1,2,2],4)
    print(res)

if __name__ == "__main__":
    main()