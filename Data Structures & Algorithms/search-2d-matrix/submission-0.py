class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=0,0
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==target:
                    return True
        return False

        