'''
There is to ways to solve this problem
1. Recursive Solution where
- Pick up as a root
    - Calculate Left Subtree G(i - 1)
    - Calculate Right Subtree G(n - i)
Thus, G(n) = Sum from i = 1 to n -> G(i - 1) * G(n - i)
^ The Number of BST for n
Time Complexity: We Run through every Node as a Root, then calculate calculate its numTrees 
Think of it as N branches and N depth. O(n^2)
Space: Storing Intermediate Solutions through a cache O(N)

2. Catalan Number Induction
C(0) = 1
C(n + 1) = [( 2 * (2n + 1) ) / n + 2 ] * C(n)
Time Complexity: O(N) since it is only 1 for loop
Space: O(1) Solution 


'''
class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        # We already know f(0) = 1, f(1) = 1
        for nodes in range(2, n + 1):
            total = 0
            for i in range(1, nodes + 1):
                left = i - 1
                right = nodes - i
                total += numTree[left] * numTree[right]
            numTree[nodes] = total # add to cache
        return numTree[n]

    def numTrees_recursive(self, n):
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        # Iterating Through the rest of n's Ex. if n = 3, we just need 2, 3
        for i in range(2, n + 1):
            # Iterating through i 
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]


def main():
    result = Solution()
    print(result.numTrees(3))

if __name__ == "__main__":
    main()
    