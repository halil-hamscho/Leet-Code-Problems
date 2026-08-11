'''
THis is very similar to the number of islands
the only thing is that we are accounting for area
so in every single island, we have to start an iterative variable that is going to track how many islands are there which
equals the area

'''

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        # BFS Way
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            temp_area = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        temp_area += 1
            return temp_area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    temp_area = bfs(r,c)
                    max_area = max(max_area,temp_area)
        return max_area

def main():
    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]] 
    
    result = Solution()
    print(result.maxAreaOfIsland(grid))

if __name__ == "__main__":
    main()