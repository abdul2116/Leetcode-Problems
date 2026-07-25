class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]],rotation_count=0) -> bool:
        if mat == target:
            return True
    
        if rotation_count == 4:
            return False
        
        for i in range(len(mat)):
            for j in range(i,len(mat)):
                mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j] 
        for i in range(len(mat)):
            mat[i].reverse()

        return self.findRotation(mat, target, rotation_count + 1)  
        