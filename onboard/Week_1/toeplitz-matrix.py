class Solution(object):
    def isToeplitzMatrix(self, matrix):
        if len(matrix)==1:
            return True
        
        for i in range(1,len(matrix)):
            for j in range(len(matrix[i])-1,-1,-1):
                if j==0:
                    continue
                else:
                   if  matrix[i][j]!=matrix[i-1][j-1]:
                       return False
        return True



        

       
        