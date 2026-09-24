class Solution:
    def bfs(self, grid, vis, row, col) -> int:
        curMax = 1
        vis[row][col] = 1
        q = deque()
        q.append((row,col))
        n = len(grid)
        m = len(grid[0])
        
        while(len(q) != 0):
            row = q[0][0]
            col = q[0][1]
            q.popleft()

            for delR, delC in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nrow = row + delR
                ncol = col + delC
                if(nrow >= 0 and nrow<n and ncol >=0 and ncol<m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1):
                    curMax += 1
                    vis[nrow][ncol] = 1
                    q.append((nrow,ncol))
        return curMax
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])

        vis = [[0 for _ in range(c)] for _ in range(r)]

        maxi = 0
        for row in range(0,r):
            for col  in range(0,c):
                if(vis[row][col] == 0 and grid[row][col] == 1):
                    curMax = self.bfs(grid, vis, row, col)
                    maxi = max(maxi, curMax)
        
        return maxi
        