from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row , col = len(grid) , len(grid[0])

        def helper(m , n) :

            bottom , right , ans = float('inf') , float('inf') , 0
            
            if m < row-1:
                bottom = helper(m+1,n)
            if n < col-1:
                right = helper(m,n+1)

            ans = min(bottom,right)
            
            if m == row-1 and n == col -1 :
                return grid[m][n]

            return grid[m][n] + ans
        
        return helper(0,0)
    
sol = Solution()
ans = sol.minPathSum([[1,2,3],[4,5,6]])
print(ans)
