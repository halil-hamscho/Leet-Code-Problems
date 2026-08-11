class Solution:
    def combinationSum(self, candidates, target):
        res = [] # global variable

        def dfs(index, curr, total): # index of candiates Ex. [2,3,6,7]. curr so [2,2,2] and total is Ex. 7 fgrom 2 + 2 + 3
            if total == target:
                res.append(curr.copy()) # need to do copy since we will be modifying curr
                return
            if index >= len(candidates) or total > target:
                return
            
            # first left branch, so including the number
            curr.append(candidates[index]) # Ex. appending [2]
            dfs(index, curr, total + candidates[index])

            # right branch without including number
            curr.pop() # delete [2] from that part so it's empty
            dfs(index + 1, curr, total)
        dfs(0, [], 0)
        return res        