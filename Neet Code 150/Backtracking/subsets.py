








class Solution:
    def subsets(self, nums):
        res = []
        subset = [] 

        # index resets back to previous index once we return 3 -> 2 and so on, using dfs
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # need copy since append just references
                return
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
def main():
    result = Solution()
    print(result.subsets([1,2,3]))

if __name__ == "__main__":
    main()
