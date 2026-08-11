'''
At a high level
- have two sets
- first iterate through the first row (pac) and last row (atl)
 run df on these and make a pac set that has all the values that reach from pac to atl and vise versa

 Now iterate throuhg the first colum (pac) and last column (atl)
 run dfs on these and also add these to the pac and atl set respectively

 Now that we have both of these
 iteratet rhough the entire matrix
 if the current r, c in both sets then we append them because they tell us
 that this specific square can go to both the pacific and the atlantic
'''

class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                heights[r][c] < prevHeight or
                (r,c) in visit):
                return
            # found a fresh height
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            # for every col
            # top
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            # need leftmost
            dfs(r, 0, pac, heights[r][0])
            # rightmost
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result

def main():
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = Solution()
    print(result.pacificAtlantic(heights))

if __name__ == "__main__":
    main()