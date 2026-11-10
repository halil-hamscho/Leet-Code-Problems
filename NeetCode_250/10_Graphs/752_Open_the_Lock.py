"""

1. Choices:
    - forward, backward by one position

2. State:
    - lock number

3. Base Case:
    - reached deadend
    - index of lock? 0, 1, 2, 3
    - 

Pattern: BFS -> shortest path 

Recognition: We wanted the minimum number of moves, with each move having equal cost

KEy Insight:
- each lock combination is a node, rotating one wheel creates and edge. BFS gurantees shortest path


10 Digits
4 Positions
8 neighbors per state

10^N possible states
    10^4 = 10,000 states 

10,000 * 8 = 80,000 checks

Time: O(1), fixed number of possible states
Sapce: O(1) fixed number of possible states
                
Python:
    - set() for membership checks
    - deque for BFS
    - % 10 to handle digit wrapping
"""
from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        deads = set(deadends)

        if "0000" in deads:
            return -1 

        if target == "0000":
            return 0
        
        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            lock, distance = queue.popleft()

            # Explore all positions
            for i in range(4):

                # Try moving Forward and Backward
                for val in [1, -1]:
                    copy = list(lock)
                    num = (int(copy[i]) + val) % 10

                    copy[i] = str(num)
                    new_lock = "".join(copy)

                    if new_lock in visited:
                        continue

                    if new_lock in deads:
                        continue

                    if new_lock == target:
                        return distance + 1

                    visited.add(new_lock)
                    queue.append((new_lock, distance + 1))

        return -1

if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    sol = Solution()
    result = sol.openLock(deadends, target)