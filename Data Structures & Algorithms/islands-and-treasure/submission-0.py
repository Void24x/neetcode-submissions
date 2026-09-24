class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Multi source BFS traversal
        row,col = len(grid), len(grid[0])

        q = deque()

        for i in range ( row):
            for j in range( col):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:

            r , c = q.popleft()

            for delR, delC in [(-1,0),(1,0),(0,-1), (0,1)]:
                nrow = r + delR
                ncol = c +  delC

                if(nrow >=0 and nrow < row and ncol>=0 and ncol < col and grid[nrow][ncol] == 2147483647):
                     grid[nrow][ncol] = grid[r][c]+1
                     q.append((nrow, ncol))