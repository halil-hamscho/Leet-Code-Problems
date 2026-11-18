"""

2 separate responsibilities

1. Task Availability
2. Task Selection

    tasks
        - index
        - enqueueTime
        - processingTime

     hashmap that has
        - processing time : heap for min?

        when we do a task
        time += processing time
        so that we skip the idling of the CPU

    - populate first, then traverse heap?

tasks are NOT guranteed to be sorted by enqueue time


We utilized an event driven simulation

Rather than advancing time continously, we jump directly to the next meaningful event:
1. A task finishes processing
2. The next task arrives while the CPU is idle

This is a useful technique beyond heap problems

2 Structures
Sorted Array: Controls when tasks become eligible
Min Heap: Controls which eligible task gets executed

The heap does not need to contain every task in the input. It only needs to contain tasks that have already arrived and are waiting to execute

Main Pattern: Heap + Sorting + Simulation

Key Insight: sort by availability, prioritize processing time

Invariant: Before selecting a task, the heap contains all available, unprocessed tasks

Time: O(n log n) (sorting + algorithm)
Space: O(n) (heap, sorted_array, result)
"""
import heapq
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:

        sorted_tasks = []

        for i, (enqueue, processing) in enumerate(tasks):
            sorted_tasks.append((enqueue, processing, i))

        # (e, p, i)
        sorted_tasks.sort()

        result = []
        min_heap = []
        time = 0
        i = 0

        while i < len(sorted_tasks) or min_heap:

            # Add all available tasks
            while i < len(tasks) and sorted_tasks[i][0] <= time:
                enqueue, processing, index = sorted_tasks[i]

                heapq.heappush(min_heap, (processing, index))
                i += 1

            if min_heap:
                # Execute tasks
                small_p, small_i = heapq.heappop(min_heap)
                result.append(small_i)
                time += small_p

            else:
                # CPU is idle
                time = sorted_tasks[i][0]

        return result

if __name__ == "__main__":
    sol = Solution()
    tasks = [[1,2],[2,4],[3,2],[4,1], [10,1]]
    result = sol.getOrder(tasks)
            

            

            

            


            

