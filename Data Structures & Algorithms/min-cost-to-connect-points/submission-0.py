class Solution:
    def calcDist(self,xi,yi,xj,yj):
        return abs(xi-xj) + abs(yi-yj)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        pointArr = [] ## Store every point co-ordinate at an index, so that you can use the index iteslf as a node
        for i in range(0,n):
            pointArr.append(points[i])
        
        vis = [0]*n
        ## Create a dict to keep adjacent list of every node. Use pointArr defined above to create the key and value mapping eg: 
        ## 0-node : [(1-node,wt),(2-node, wt),(3-node, wt)...]
        ## Here 0-node means the point present in the 0th index of pointArr.
        adjL = {i:[] for i in range(n)}
        minsum = 0  
        for i in range(0, n):
            xi, yi = pointArr[i]
            for j in range(0, n):
                if i!=j:
                    xj,yj = pointArr[j]
                    dist = self.calcDist(xi,yi,xj,yj)
                    adjL[i].append((j, dist))
        pq = []
        heapq.heappush(pq,(0,0))

        while pq:
            dist,pointindex = heapq.heappop(pq)
            if (vis[pointindex] == 1): continue 
            vis[pointindex] = 1
            minsum += dist
            for adjNode in adjL[pointindex]:
                if vis[adjNode[0]] != 1:
                    heapq.heappush(pq,(adjNode[1], adjNode[0]))
        
        return minsum










        