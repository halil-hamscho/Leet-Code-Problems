"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, 
and a number n. 
Each CPU interval can be idle or allow the completion of one task. 
Tasks can be completed in any order, but there's a constraint: 
there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Ideation:
    - have some sort of clock
        - when we append or use a task, we need some way of keeping track 

        - priority, value?

do we do a stack of len n?

Can we select numbers based on some priority

At any given moment, we have two categories

Available Tasks:
A: 5 remaining
B: 3 remaining
C: 2 remaining

Cooling Down:
D: available at time 7
E: available at time 9


The heap should only contain tasks that are currently available for execution

Max Heap -> select available task with highest freuqency
Queue -> store tasks waiting for cooldown
Clock -> current scheduling interval

available_time = time + n + 1

Edge Cases for heap and queue:

1. Heap Empty and Queue
    - if queue[0][0] > time:
        continue
    - if queue[0][0] <= time

2. Heap and no Queue:
    1. 

"""
import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        counts = Counter(tasks)

        max_heap = []
        for task, count in counts.items():
            max_heap.append((-count, task))

        heapq.heapify(max_heap)

        queue = deque()
        time = 0

        while max_heap or queue:

            # Empty Heap
            if not max_heap:
                if queue[0][0] > time:
                    time += 1
                    continue

            if queue and queue[0][0] <= time:
                _, val = queue.popleft()

                heapq.heappush(max_heap, val)

            # Nodes in Heap
            count, letter = heapq.heappop(max_heap)

            available_time = time + n + 1 

            if count + 1 < 0:
                queue.append((available_time, (count + 1, letter)))

            time += 1

        return time

if __name__ == "__main__":
    tasks = ["B","C","D","A","A","A","A","G"]
    n = 1
    sol = Solution()
    result = sol.leastInterval(tasks, n)