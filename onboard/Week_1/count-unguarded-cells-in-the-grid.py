class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i,j in guards:
            matrix[i][j]="g"
        for i,j in walls:
            matrix[i][j]="w"
        for i,j in guards:
            
            for dx,dy in ([[0,1],[0,-1],[1,0],[-1,0]]):
                new_dx,new_dy=i+dx,j+dy
                while 0<=new_dx<m and 0<=new_dy<n and matrix[new_dx][new_dy]!="g" and matrix[new_dx][new_dy]!="w":
                    matrix[new_dx][new_dy]="G"
                    new_dx+=dx
                    new_dy+=dy
        count = sum(row.count(0) for row in matrix)
        return count


        

        