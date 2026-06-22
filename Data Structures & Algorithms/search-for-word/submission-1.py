class Solution:
    def dfs(self,board,word,i,j,let):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[let]:
            return False
        if let==len(word)-1 and board[i][j]==word[let]:
            return True
        temp = board[i][j]
        board[i][j] = "#"
        found = (
        self.dfs(board,word,i+1,j,let+1) or
        self.dfs(board,word,i,j+1,let+1) or
        self.dfs(board,word,i-1,j,let+1) or
        self.dfs(board,word,i,j-1,let+1)
        )
        board[i][j] = temp
        return found
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.dfs(board,word,i,j,0):
                        return True
        return False
        