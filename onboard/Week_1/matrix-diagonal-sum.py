class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        right_sum=0
        left_sum=0      
        if n%2!=0:
            for i in range(n):
                for j in range(n):
                    if i-j==0:
                        right_sum+=mat[i][j]
                    if i+j==n-1:
                        left_sum+=mat[i][j]
            return left_sum + right_sum - mat[(n-1)//2][(n-1)//2]
        else:
            for i in range(n):
                for j in range(n):
                    if i-j==0:
                        right_sum+=mat[i][j]
                    if i+j==n-1:
                        left_sum+=mat[i][j]
            return left_sum + right_sum


        