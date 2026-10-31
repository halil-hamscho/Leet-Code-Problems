class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []
        path = []
        def dfs(index, total):

            if total == target:
                result.append(path.copy())
                return

            for i in range(index, len(candidates)):

                if total + candidates[i] > target:
                    continue
                
                path.append(candidates[i])

                dfs(i, total + candidates[i])

                path.pop()


        dfs(0,0)
        return result

if __name__ == "__main__":        
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    result = sol.combinationSum(candidates, target)
    print(result)