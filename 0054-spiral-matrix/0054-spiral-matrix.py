class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m-1
        left = 0
        right = n - 1
        while top <= bottom and left <= right:
            for j in range(left,right+1):
                result.append(matrix[top][j])
            top+=1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right-=1
            
            if top <= bottom and left <= right:
                for j in range(right, left-1, -1):
                    result.append(matrix[bottom][j])
                bottom-=1
                
                for i in range(bottom , top-1, -1):
                    result.append(matrix[i][left])
                left+=1
        return result
        
        