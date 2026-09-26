class Solution:
    def dfs(self,row, col, board):
        board[row][col] = "V"

        for delr, delc  in [(-1,0),(1,0),(0,-1), (0,1)]:
            nr = row + delr
            nc = col + delc
            if(nr >= 0 and nr < len(board) and nc >=0 and nc < len(board[0]) and board[nr][nc] == "O"):
                self.dfs(nr, nc, board)
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col =  len(board[0])

        for i in range(0,row):
            if(board[i][0] == "O"):
                self.dfs(i, 0, board)
            if(board[i][col-1] == "O"):
                self.dfs(i, col-1, board)
        for i in range(0, col):
            if(board[0][i] == "O"):
                self.dfs(0, i, board)
            if(board[row-1][i] == "O"):
                self.dfs(row-1, i,board)
        
        for i in range(0,row):
            for j in range(0,col):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(0,row):
            for j in range(0,col):
                if board[i][j] == "V":
                    board[i][j] = "O"
        