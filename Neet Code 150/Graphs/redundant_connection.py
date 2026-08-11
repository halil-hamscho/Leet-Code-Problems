
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        print(parent)
        size = [1] * (n + 1)

        def UnionFind(node):
            if node != parent[node]:
                parent[node] = UnionFind(parent[node]) # Path Compression
            return parent[node]

        def unionbySize(u, v):
            ulp_u = UnionFind(u)
            ulp_v = UnionFind(v)

            if(ulp_u == ulp_v): 
                return False
            if(size[ulp_u] < size[ulp_v]):
                parent[ulp_u] = ulp_v
                size[ulp_v] += size[ulp_u]
            else:
                parent[ulp_v] = ulp_u
                size[ulp_u] += size[ulp_v]
            return True
        
        for u, v in edges:
            if not unionbySize(u, v):
                return [u, v] # Return Redundant Edge
        return []

def main():
    result = Solution()
    print(result.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

if __name__ == "__main__":
    main()