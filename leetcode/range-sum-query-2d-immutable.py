class NumMatrix(object):

    def __init__(self, matrix):
        row,col=len(matrix),len(matrix[0])
        self.matrix=[[0]*(col+1) for i in range(row +1)]
        for i in range(row):
            prefix=0
            for j in range(col):
                prefix+=matrix[i][j]
                above=self.matrix[i][j+1]
                self.matrix[i+1][j+1]=prefix + above

        
        
        

    def sumRegion(self, row1, col1, row2, col2):
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        aboveT=self.matrix[row1-1][col2]
        aboveL=self.matrix[row1-1][col1-1]
        left=self.matrix[row2][col1-1]
        total=self.matrix[row2][col2]
        return total-aboveT-left +aboveL
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)