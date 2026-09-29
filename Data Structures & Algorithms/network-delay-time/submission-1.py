class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vis = [0] * (n+1)
        adj = [[] for _ in range(n+1)]

        for u,v,t in times:
            adj[u].append((v,t))

        q = deque()

        dis = [float('inf')] * (n+1)

        dis[k] = 0
        tq = []
        heapq.heappush(tq,(0,k))
        while tq:
            curDist,node = heapq.heappop(tq)
            for v,dist in adj[node]:
                newdist = curDist + dist
                if newdist < dis[v]:
                    dis[v] = newdist
                    heapq.heappush(tq,(newdist,v))
        maxTime =  max(dis[1:]) ## Since 1 based vertices

        if maxTime == float('inf'): return -1

        return maxTime









        