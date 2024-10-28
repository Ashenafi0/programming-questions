class Solution:
    def maxSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        sum_hourglass = float('-inf') 

        for i in range(m - 2):  
            for j in range(n - 2):  
                temp = 0
                temp += sum(grid[i][j:j + 3])  # Top row
                temp += grid[i + 1][j + 1]  # Middle element
                temp += sum(grid[i + 2][j:j + 3])  # Bottom row

                
                sum_hourglass = max(sum_hourglass, temp)

        return sum_hourglass
