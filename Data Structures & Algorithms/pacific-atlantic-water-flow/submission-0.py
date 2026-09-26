class Solution:
    def dfs(self, row, col, heights, vis):
        vis[row][col] = True

        for delr, delc in [(-1,0),(1,0),(0,-1), (0,1)]:
            nr = row + delr
            nc = col + delc

            if(nr>=0 and nr<len(heights) and nc>=0 and nc < len(heights[0]) and heights[nr][nc] >= heights[row][col] and vis[nr][nc] == False):
                self.dfs(nr, nc, heights, vis)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        pacific = [[False for _ in range(c)] for _ in range(r)]       
        atlantic = [[False for _ in range(c)] for _ in range(r)]   

        for i in range(0,r):
            self.dfs(i, 0, heights, pacific)
            self.dfs(i,c-1, heights, atlantic)
        for i in range(0,c):
            self.dfs(0, i,heights, pacific)   
            self.dfs(r-1, i,heights, atlantic)

        ans = []
        for i in range (0,r):
            for j in range(0,c):
                if(pacific[i][j] == True and atlantic[i][j] == True):
                    ans.append([i,j])
        return ans  