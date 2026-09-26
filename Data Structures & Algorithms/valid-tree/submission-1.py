class Solution:
    def dfs(self, node, vis, adjL, parent):
        vis[node] = 1

        for it in adjL[node]:
            if not vis[it]:
                self.dfs(it, vis, adjL, node)
            elif it != parent:
                return True
        return False


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjL=[[] for _ in range(n)]
        vis = [0] * n
        #Create adj list
        for u,v in edges:
            adjL[u].append(v)
            adjL[v].append(u)
        #do dfs traversal and check if the graph is a single comp or not.
        comp = 0
        
        for i in range(0,n):
            if not vis[i]:
                comp += 1 #
                isCycle = self.dfs(i, vis, adjL, -1)
         
         #if a single comp and no cycles in the graph then it's a valid tree
        if comp == 1 and isCycle == False:
            return True
        return False
           


        
        