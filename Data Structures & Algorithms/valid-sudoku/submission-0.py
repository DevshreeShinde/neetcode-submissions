class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def issafe(row,col,tmp):
            for num in range(9):
                if board[row][num]==tmp or board[num][col]==tmp:
                    return False
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3
            for i in range(startRow,startRow+2):
                for j in range(startCol,startCol+2):
                    if board[i][j]==tmp:
                        return False
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                tmp = board[i][j]
                board[i][j]='.'
                if not issafe(i,j,tmp):
                    return False
                board[i][j]=tmp
        return True