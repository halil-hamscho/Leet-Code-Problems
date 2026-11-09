"""

- We can start BFS from multiple locations

multisource BFS
"""
from collections import deque
def test(grid):

    ROWS = len(grid)
    COLS = len(grid[0])

    # Initialize queue with all starting sources
    queue = deque([(start_row, start_col)])
    visited = {(start_row, start_col)}

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, col = queue.popleft()

        # Process current cell

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            # Check Boundaries
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue

            # Check whether already visited
            if (nr, nc) in visited:
                continue

            # Mark
            visited.add((nr, nc))

            # Explore
            queue.append((nr, nc))

"""
2 Common Ways to Track Distances in BFS

Approach A: Store the distance with each node

queue = deque([(start_row, start_col, 0)])

while queue:
    row, col, distance = queue.popleft()

    - when discovering a new neighbor its distance + 1

Approach B: Process BFS one level at a time

distance = 0
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()

        # Process Node and enqueue neighbors

    distance += 1

    
Note:
- when asked to find the shortest distance from many cells to their nearest source,
consider starting BFS from all sources simultaneously

Mental Rule: Mark a node as visited when you enqueue it, nto when you dequeue it
"""