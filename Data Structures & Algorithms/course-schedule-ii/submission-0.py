class Solution:
    def topoSort(self,adjL, n):
        indegree = [0] * n
        
        for i in range(0,n):
            for l in adjL[i]:
                indegree[l] +=1

        q = deque()

        for i in range(0,n):
            if(indegree[i] == 0):
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for l in adjL[node]:
                indegree[l] -= 1
                if(indegree[l] == 0): q.append(l)
    
        if len(topo) == n: return topo
        return []
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjL = [[] for _ in range(numCourses)]
        for el in prerequisites:
            adjL[el[1]].append(el[0])
        
        return self.topoSort(adjL, numCourses )
        
