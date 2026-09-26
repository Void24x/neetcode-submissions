class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        q = deque()
        for i in range(0,r):
            for j in range(0,c):
                if(grid[i][j] == 2):
                    q.append((i, j, 0))
        minT = 0
        while q:
            row, col, t = q.popleft()
            minT = max(minT,t)

            for delr, delc in [(-1,0),(1,0),(0,-1), (0,1)]:
                nr = row + delr
                nc = col + delc

                if(nr >=0 and nr < r and nc>=0 and nc < c and grid[nr][nc] != 2 and grid[nr][nc] != 0):
                    grid[nr][nc] = 2
                    q.append((nr,nc,t+1))
        
        for i in range(0,r):
            for j in range(0,c):
                if(grid[i][j] == 1):
                    return -1
        return minT
                

        