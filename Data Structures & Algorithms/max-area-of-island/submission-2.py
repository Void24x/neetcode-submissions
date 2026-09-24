class Solution:
    ##DFS Version
    def dfs(self, grid, vis, row, col) -> int:
        vis[row][col] = 1
        n = len(grid)
        m = len(grid[0])

        area = 1
        
        for delR, delC in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow = row + delR
            ncol = col + delC
            if(nrow >= 0 and nrow<n and ncol >=0 and ncol<m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1):
                area += self.dfs(grid,vis,nrow,ncol)
        return area
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])

        vis = [[0 for _ in range(c)] for _ in range(r)]

        maxi = 0
        for row in range(0,r):
            for col  in range(0,c):
                if(vis[row][col] == 0 and grid[row][col] == 1):
                    maxi = max(maxi,self.dfs(grid,vis,row,col))
        
        return maxi
        