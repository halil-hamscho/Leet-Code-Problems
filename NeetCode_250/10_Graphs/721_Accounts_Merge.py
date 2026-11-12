"""

Main Algorithm
    - First Consolidate if there is any duplicate names
    - once we have a consolidated list, we just sort each second part


Note: With Union Find
Since we make the account index be the key, we never use the 
name to determine which accounts belong together

Union Find: assigning every connected group a representative

- Initially every node represents itself
- as we discover connections, we merge groups
- at the end, nodes with the same root belong to the same group

Pattern: Connected Components using Union Find

- Observation: Accounts sharing an email belong to the same person, even if the connection is indirect

Connected Components Problem

Represent each account index as a node, not the name or email

Parent array: Stores relationships between account indices
Email Dictionary: helps discover which accounts should be united
Union Find: Tracks connectivity but does not collect emails
Grouping Dictionary: collects emails belonging to each component

Complexity:
N = number of accounts
M = total number of email occurences

Time: O(M log M)
- sorting dominates

Space: O(N + M)
parent and size array require O(N)
email dictionary: O(M)

Distinguish 3 Things
1. Finding connections: email_to_account
2. Maintaining connects components: parent, size, find(), union()
3. Collecting the actual answer: groups[root]

Union Find determines WHO belongs together. A separate grouping step determines WHAT belongs in the final result
"""
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        email_to_account = {} # email to account
        parent = list(range(len(accounts)))
        size = [1] * len(accounts)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b): 
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return
            
            if size[rootA] < size[rootB]:
                parent[rootA] = rootB
                size[rootB] += size[rootA]
            else:
                parent[rootB] = rootA
                size[rootA] += size[rootB]

            return


        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email in email_to_account:
                    union(i, email_to_account[email])

                else:
                    email_to_account[email] = i

        groups = defaultdict(set)

        for i in range(len(accounts)):
            root = find(i)

            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                groups[root].add(email)

        result = []
        for root in groups:
            l = sorted(groups[root])

            name = [accounts[root][0]]

            result.append(name + l)

        return result
        
if __name__ == "__main__":
    sol = Solution()
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    result = sol.accountsMerge(accounts)