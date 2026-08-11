'''
Graph Problem
We are given an adjacency matrix
we need to traverse this matrix
An island is surrounded by water
and is formed by connecting adjacent lands
ONLY HORRIZONTALLY OR VERTICALLY

'''
from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0 # no islands
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() # will be a tuple (row, col)
        islands = 0 # count the number of islands visited

        def bfs(r,c):
            q = deque()
            visit.add((r,c)) # just visited a 1
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]] # north south east west
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

def main():
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
    ]
    result = Solution()
    print(result.numIslands(grid))
if __name__ == "__main__":
    main()

