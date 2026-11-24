Dynamic Programming
    technique to store solutions to smaller problems so they can be reused

    Recognize repeated computation and determine what information we need to remember

Property 1: overlapping subproblems
Property 2: optimal structure

State:
    what does dp[i] represent

    "What question would I want dp[i] to answer?"

Recurrense Relation

    After defining the state, we need to determine how states relate
    to one another

    "What information do I need to calculate the answer at position i?"

    How do smaller answers combine into a larger answer

Approach A: Top Down (Memoization)

    Starting Point: original problem
    Main Mechanism: recursion
    Storage: dictionary or cached function
    Computation: only states reached by recursion
    Recursion Stack: yes
    often easier for: discovering recursive relationships

    Time: O(n)
    Space: O(n) store n answers and use recursion stack of depth n

Approach B: Bottom Up (Tabulation)

    Starting Point: smallest subproblems/known answers
    Main Mechanism: Iteration
    Storage: array
    Computation: usually all states in the table
    Recursion Stack: no
    Often easier for: optimizing space and execution

    Time: O(n) iterate through the array once and maintain an array of size n + 1
    Space: O(n) 

    Space Optimization: 
    Recurrence tells us how much previous information must be retained
    - however this optimization doesn't always apply

4 Questions

Q1: What does the state represent?

    dp[i] = minimum cost to reach position i

Q2: What choices are available?

Q3: How do we combine previous answers?

    If I already knew the anwers to the smaller problems, how would I calculate the current answer?

Q4: What are the base cases?

How to recogize DP in an interview?

- count the number of ways
- find a minimum or maximum
- determine whether something is possible
- make a sequence of decisions
- recursion repeatedly reaches identical states

DP is especially useful when the future only needs a compact summary of the past

DP vs. Greedy Algorithms
- a greedy algorithm commits to a locally attractive choice when we can prove that doing so is safe

- DP often considers multiple possible choices and combines their resulting answers

One Dimensional vs. Two Dimensional DP

- One Dimensional
    dp[i]

- Two Dimensional
    dp[i][j]

Dimension comes from how much information is needed to uniquely identify a subproblem

Mental Model

Original Problem
    |
    v
What decisions can I make?
    |
    v
What smaller problems result?
    |
    v
What information identifies each smaller problem?
    |
    v
Can the same smaller problem occur again?
    |
    v
Define the DP state
    |
    v
Derive the recurrence
    |
    v
Establish base cases
    |
    v
Implement memoization or tabulation
    |
    v
Analyze time and space
    |
    v
Optimize Space if possible


Memoization Approach:

1. Hashmap
memo = {}

Example:
def dfs(i):
    if i in memo:
        return memo[i]

    memo[i] = extra
    return extra

2. Python Decorator
@cache

3 
@lru_cache(None) or @lru_cache(maxsize=N)
- limits memory usage


