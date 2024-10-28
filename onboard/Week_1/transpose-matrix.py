class Solution(object):
    def transpose(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        ans=[]
        for i in range(col):
            temp=[]
            for j in range(row):
                temp.append(matrix[j][i])
            ans.append(temp)
        return ans


        
        