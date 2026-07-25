class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat

        reshaped = [[0]*c for i in range(r)]
        row_ptr = 0
        col_ptr = 0 
        for i in range(m):
            for j in range(n):
                reshaped[row_ptr][col_ptr] = mat[i][j]
                col_ptr += 1
                if col_ptr == c:
                    col_ptr = 0
                    row_ptr +=1
        return reshaped
        