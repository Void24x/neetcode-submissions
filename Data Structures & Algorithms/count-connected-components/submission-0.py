class Solution:
    def dfs(self,node, adj,vis):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it,adj,vis)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [0] * n
        adjL = [[] for _ in range(n)]

        for u,v in edges:
            adjL[u].append(v)
            adjL[v].append(u)
        comp = 0
        for i in range(0,n):
            if not vis[i]:
                comp +=1
                self.dfs(i,adjL,vis)
        return comp
