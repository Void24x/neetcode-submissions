class DisjointSet:
    def __init__(self, n):
        # Equivalent to rank.resize(n + 1, 0) and parent sizing
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))  # Sets parent[i] = i for i in range(n + 1)

    def findUPar(self, node):
        # Base case: if the node is its own parent, return it
        if node == self.parent[node]:
            return node
        
        # Path compression: point the node directly to the ultimate parent
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        # Find ultimate parents of u and v
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # If they already belong to the same set, do nothing
        if ulp_u == ulp_v:
            return

        # Attach smaller size tree under higher size tree
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        ds = DisjointSet(n+1)
        ans = []
        for u,v in edges:
            if ds.findUPar(u) != ds.findUPar(v):
                ds.unionBySize(u,v)
            else:
                ans.append(u)
                ans.append(v)
                break
        return ans
        
        
