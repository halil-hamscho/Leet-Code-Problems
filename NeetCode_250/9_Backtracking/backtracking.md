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
