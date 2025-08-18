# There is a robot on an m x n grid. The robot is initially located 
# at the top-left corner (i.e., grid[0][0]). The robot tries to move 
# to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can 
# only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique 
# paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


class Solution :
    def uniquePaths(self, m: int, n: int) -> int:
        row, col  = m , n
        def helper(m, n) :
            if m >= row or n >= col :
                return 0
            if m == row-1 and n == col -1 :
                return 1
            return helper(m+1, n) + helper(m , n+1)

        return helper(0,0)
    
    def uniquePathsDP(self, m: int, n: int) -> int:
        row, col  = m , n
        dp = [[None] * (col + 1) for _ in range(row+1)]
        dp[0] = [1] * (col+1)
        for i in range(row+1) :
            dp[i][0] = 1
        # print(dp)
        for i in range(1,row+1) :
            for j in range(1,col+1):
                if dp[i][j] is not None :
                    return dp[i][j]
                dp[i][j] = dp[i-1][j] + dp[i][j-1]


        return dp[row-1][col-1]
    

    # go through this solution as well
    def uniquePathsOptimisedDP(self, m: int, n: int) -> int:
        dp = [1] * n  # first row is all 1s
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]  # update in-place
        return dp[-1]
    


sol = Solution()
ans = sol.uniquePathsDP(3,7)
print(ans)