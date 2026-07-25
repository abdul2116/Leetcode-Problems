class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return None
        m = len(matrix) #row
        n = len(matrix[0]) #column
    
        low = 0
        high = (m * n) - 1
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // n #dividing by no. of columns
            col = mid % n #getting reminder after dividing by number of columns
            element = matrix[row][col]

            if element == target:
                return True
            elif element < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        