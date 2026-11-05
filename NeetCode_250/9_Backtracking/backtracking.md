General Backtracking Structure

def dfs(...):

    # Check whether the current choice is valid

    # Make a choice

    # Explore recursively

    # Undo the choice

Local State vs. Shared State

Integers and Strings are immutable, so changes do not affect the parent
- this is preferred vs. having a global variable

Local State: No restoration needed because each revursive call maintains its own variables

Shared State: Restore Changes when necessary so other branches start with the correct state


Subsets:
2 Decisions
- Include
- Exclude
Expect 2^n possibilities, if we must store or copy each subsset, account for the numer of elements in each one, giving O(n x 2^n)

Intuition: In Subsets, every decision advances the index because
each element can be used only once

Sometimes, instead of reconstructing information from the current path, you can maintain an accumulated state as you explore

LeetCode 1863: Sum of All Subset XOR Totals
dfs(index) n-> dfs(index, current_xor)
Combination Sum:
2 Decisions
- Include: Stay at the same index because repetition is allowed
- Skip: Advance the index because we're finished considering that candidate

Decision Structure:
Establish 4 things before coding
1. Choices: What can I decide at each step?
2. State: What information represents my current progress?
3. Base Case: When have I completed a valid possibility?
4. Restoration: What must I undo before exploring another choice?


2 Ways to think about backtracking

1. Binary Decision Approach

"Do I include this element or exclude it?"

dfs(index) # Include
dfs(index + 1) # Exclude

2. A for loop approach

"Which element should I choose next?"
def dfs(start, state):
    if valid_solution:
        save_solution()
        return

    for i in range(start, len(nums)):
        if invalid_choice:
            continue
        
        path.append(nums[i])
        dfs(...)
        path.pop()

this is especially intuitive when constructing combinations or permutations
- Each recursion level chooses the next element of the combination
- ALSO for loop handles edge case of index == len(numbers): return

1. Continue: skip the current candidate
    if total + candiates[i] > target:
        continue

    this skips the current iteration but continues checking other candidates

    use this when unsorted

2. break: stop the current loop

candidates.sort()
for i in range(index, len(candidates)):
    if total + candidates[i] > target:
        break

    since the candidates are already sorted, every subsequent candidate is also too large


3. return: exit the entire DFS call
this also works for when candidates are sorted


Main Difference between Subsets and Combinations
- Both explore a path, backtrack and undo decisions, both can also have limits

Subsets: Include or Exclude

path.append(nums[index])
dfs(index + 1)

path.pop()
dfs(index + 1)

We explicitly include and or exclude

Combinations: Choose the next element

for i in range(index, n + 1):
    path.append(i)
    dfs(i + 1)
    path.pop()

instead of explicitly decising whether to include or exclude each element, ask
- Which element should I choose next?

The loop explores every possible next choice

Permutations

Time: O(n x n!)
for n distinct numbers, there are n! possible permutations, each completed
permutation requires O(n) time to copy the result

for num in nums:
    if num in used:
        continue

    path.append(num)
    used.add(num)

    dfs()

    path.pop()
    used.remove(num)

In this case, Order MATTERS, the for loop tells us that the choices that remain valid after selecting an element are every element not already selected (in the used set)

Two Valid Approaches

1. Boolean Array

used = [False] * len(nums)

if used[i]:
    continue

used[i] = True
dfs()
used[i] = False

2. Set of indices

used = set()

if i in used:
    continue

used.add(i)
dfs()
used.remove(i)

Mental Models

1. Subsets: Pick or skip

    1. Include the curr element
    2. Exclude the curr element

    State: index

    - can also use the for i in range(index, len(nums)):

2. Combinations: choose from remaining candidates

    - Choose the next element from the candidates appearing after your current position

    State: start

3. Permutations: Choose from unused candidates

    - Here, we are not deciding whether to include an element
    - We are deciding which unused element should occupy the next position
        permutations are about filling positions, not deciding whether to include elements

    State: used

    used can be either a set of nums or in harder problems should be an array of indices 
    so that way when we are backtracking we keep track of indices rather than values (and avoid duplicates)


Am I selecting elements or arranging elements?
    - if selecting, think subsets or combinations
    - if arranging, think permutations

If there is duplicates, for loop is preferred as a way to perform any conditional statement in the same recursion depth


Backtracking Heuristic:

When the order of decisions does not affect correctness, consider processing the most restrictive choices first


- Subsets: For each element, decide whether to include it (no)
- Combinations: Choose which elements belong in a group
- Permutations: Choose which unused element comes next
- Matchsticks to Square: Every element must be used, so choose which group receives it
- N Queens: choose a column for each row, prune positions that violate col and diag constraints
- N Queens 2: no board, or result. We just count the occurances through sum
    - if we just wanted to find one occurance then 
        if dfs(row + 1):
            return True
    - and base case
        if row == n:
            return True
- Word Break 2
    - string partition, prune the serach by checking if a candidate substring is a valid dict word


DFS
Goal
Generate all solutions -> Save each solution and continue exploring
Count all solutions -> Increment a counter and continue exploring
Find any solution -> Return True immediately when one is found
