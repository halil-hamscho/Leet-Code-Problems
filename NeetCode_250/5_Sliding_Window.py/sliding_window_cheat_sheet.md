Sliding Window: Chapter Takeaways

1. Recognition

Look for:

* Contiguous subarrays or substrings.
* Longest, shortest, maximum, or minimum window satisfying a condition.
* Overlapping windows where we can reuse information.

2. Two Main Types

* Fixed window: Size k is predetermined. Expand right, remove expired left.
* Variable window: Expand r, shrink l when necessary to satisfy a condition.

3. General Framework

1. Expand: Add nums[r] to the maintained state.
2. Validate: Check whether the window satisfies the condition.
3. Shrink: Move l and update the state when necessary.
4. Record: Update the answer at the appropriate moment.

4. What Information Should We Maintain?

* Sum: Running sum.
* Uniqueness: Set.
* Frequencies: Hash map.
* Maximum or minimum: Monotonic deque.
* Multiple requirements: Hash maps with a satisfied condition counter.

5. Key Invariants

* The maintained state accurately represents the current window.
* Window boundaries are correctly updated.
* Invalid windows are repaired before recording answers that require validity.

6. Complexity

Usually O(n) because each element enters and leaves the window at most once.

However, expensive operations inside the loop can increase complexity.

7. Most Important Interview Intuition

Ask yourself three questions:

1. What makes my window valid or invalid?
2. What information can I maintain instead of recalculating?
3. When should I shrink the window and record the answer?

Core takeaway: Sliding window is about exploiting overlap between contiguous ranges by maintaining reusable state instead of repeatedly scanning them.