Binary Search Cheat Sheet

• Use binary search when the search space is ordered or when a condition changes monotonically.

• Standard target search usually uses:

while l <= r:

• Boundary or convergence search often uses:

while l < r:

• Always ask: what does mid tell me, and which half can I safely eliminate?

• For ascending arrays:

mid < target  → move left pointer right
mid > target  → move right pointer left

• For descending arrays, reverse those decisions.

• For answer space problems, binary search the possible answer, not the array.

Examples: minimum capacity, minimum speed, maximum allowed sum.

• Good answer space bounds are usually:

smallest possible valid answer
largest guaranteed valid answer

• For rotated or mountain arrays, first identify the structural boundary, then binary search the sorted region.

• If mid might still be the answer, keep it:

r = mid

If it definitely cannot be the answer, discard it:

r = mid - 1

• Core invariant:

The answer remains inside the current search space.

• Complexity is usually:

O(log n)

or for answer space problems:

O(n log range)

• Mental question to remember:

What property lets me eliminate half of the remaining possibilities?