# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[None] * (amount+ 1) for _ in range(len(coins)+1)]
        memo[0] = [float('inf')] * (amount +1)
        for i in range(len(coins)+1) :
            memo[i][0] = 0
        
        for i in range(1,len(coins)+1) :
            for j in range(1,(amount+1)) :
                if coins[i-1] > j :
                    memo[i][j] = memo[i-1][j] 
                else :
                    memo[i][j] = min(1+memo[i][j-coins[i-1]], memo[i-1][j] )
        return memo[len(coins)][amount]


        # def helper(n, sum ):
        #     # print(n , sum)
        #     if sum == 0 :
        #         return 0
        #     if n == 0:
        #         return float('inf')
        #     if coins[n-1] > sum :
        #         return helper(n-1,sum)
        #     else :
        #         take = 1 + helper(n, sum - coins[n-1])
        #         leave = helper(n-1,sum)
        #         return min(take, leave)
        # ans = helper(len(coins), amount)
        # return ans if ans != float('inf') else -1
sol = Solution()
ans = sol.coinChange([1,2,5], 11) 
print(ans)