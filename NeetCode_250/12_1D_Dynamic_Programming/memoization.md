Approach:

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
