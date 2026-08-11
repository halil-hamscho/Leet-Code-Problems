class Solution:
    def subsetsWithDup(self, nums):
        res = []
        subset = [] 
        #Make subsets, and because there is duplicates simply check with res

        print("Starting DFS Algorithm")
        # In order to avoid duplicate work what cowe must do is we must sort the nums list
        # the reason we do that for example in [4,4,4,1,4] we would get much more values
        nums.sort()
        print(f"nums {nums}")
        def dfs(index):
            print(f"index {index}")
            if subset in res:
                print(f"subset {subset} in {res}")
                return
            
            if index >= len(nums):
                res.append(subset.copy()) # once we reach the max of the index 
                print(f"result {res}")
                return
            
            subset.append(nums[index])
            print(f"subset {subset}")
            dfs(index + 1)

            subset.pop() # we simulating just adding an empty list to the subset Ex. instead opf [1,2,2] its [1,2, [] ]
            dfs(index + 1)
        dfs(0)
        return res
def main():
    result = Solution()
    nums = [4,4,4,1,4]
    print(result.subsetsWithDup(nums))

if __name__ == "__main__":
    main()
        

