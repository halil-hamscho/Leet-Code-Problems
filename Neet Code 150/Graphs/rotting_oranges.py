from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        q = deque()
        time = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        # starting work, count the fresh and append rotten to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c]) # found rotten
                if grid[r][c] == 1:
                    fresh += 1 # found fresh orange
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # now that we have a full queue
        # run bfs
        while q and fresh > 0:
            for i in range(len(q)): # takes snapshot of current queue Ex. the first rotten orange in the grid
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row not in range(ROWS) or
                        col not in range(COLS) or
                        grid[row][col] != 1):
                        continue # did not find a fresh orange
                    # found fresh orange
                    # turn to rotten
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
                # finished exploring
            # finished the current snapshot
            time += 1
        return time if fresh == 0 else -1    


            


def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]

if __name__ == "__main__":
    main()