from typing import List
# Given a m x n grid filled with non-negative numbers, find a path from top left to 
# bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])

        def helper(m , n) :

            if m == row-1 and n == col -1 :
                return grid[m][n]

            bottom , right , ans = float('inf') , float('inf') , 0
            
            if m < row-1:
                bottom = helper(m+1,n)
            if n < col-1:
                right = helper(m,n+1)

            ans = min(bottom,right)
            
            return grid[m][n] + ans
        
        return helper(0,0)
    
    def minPathSumDP(self, grid: List[List[int]]) -> int:
        row , col = len(grid),  len(grid[0])
        memo = [[None] * col for _ in range(row)]
        memo[0][0] = grid[0][0]

        for i in range(1, row) :
            memo[i][0] = memo[i-1][0] + grid[i][0]

        for j in range(1,col) :
            memo[0][j] = memo[0][j-1] + grid[0][j]

        print(memo)

        for i in range(1,row) :
            for j in range(1, col) :
                memo[i][j] =  grid[i][j] + min(memo[i-1][j], memo[i][j-1])

        return memo[row-1][col-1]
    
sol = Solution()
ans = sol.minPathSumDP([[1,3,1],[1,5,1],[4,2,1]])
print(ans)
