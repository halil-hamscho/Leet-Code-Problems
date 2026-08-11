#include <vector>
#include <iostream>

using namespace std;
/*
A Disjoint-Set Data Structure is also called a union-find data structure. It basically stores a colelction
of disjoint (non-overlapping sets). It stores a partition of a set into disjoint subsets. It provides
operations for adding new sets, merging sets and finding a representative member of a set
*/

class DisjointSet {
    vector<int> rank, parent, size;
public:
    DisjointSet(int n) {
        rank.resize(n + 1, 0), // One based indexing graph
        parent.resize(n + 1);
        size.resize(n + 1);

        for(int i = 0; i<= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUPar(int node){
        if(node == parent[node]) // Ex. 1 = parent[1], Yes
            return node;
        return parent[node] = findUPar(parent[node]); // Ex. parent[5] = f(parent[4])
    }

    void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);

        if(ulp_u == ulp_v) return;
        if(rank[ulp_u] < rank[ulp_v]){
            parent[ulp_u] = ulp_v; // Attaching the smaller node with the larger
        }
        else if (rank[ulp_v] < rank[ulp_u]){
            parent[ulp_v] = ulp_u;
        }
        else {
            parent[ulp_v] = ulp_u;
            rank[ulp_u]++; // attaching it to u, so we increase it
        }
    }
    // Size is much more intuitive, rather than rank, Time complexity of O(4 alpha) roughly O(1)
    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);

        if(ulp_u == ulp_v) return;
        if(size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else { // no equal case
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};
int main() {
    DisjointSet ds(7);
    ds.unionByRank(1, 2);
    ds.unionByRank(2, 3);
    ds.unionByRank(4, 5);
    ds.unionByRank(6, 7);
    ds.unionByRank(5, 6);
    // if 3 and 7 are same or not
    if(ds.findUPar(3) == ds.findUPar(7)){
        cout << "Same\n";
    }
    else cout << "notSame \n";
    ds.unionByRank(3, 7);

    return 0;
}