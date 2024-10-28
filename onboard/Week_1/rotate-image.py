class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # s, e= 0, len(matrix)-1
        for i in range(len(matrix)):
            s = 0
            e = len(matrix)-1
            while s < e:
                matrix[i][s], matrix[i][e] = matrix[i][e], matrix[i][s]
                s += 1
                e -= 1
        