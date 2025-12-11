# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution :
    def brute(self,nums) :
        n = len(nums)
        max_profit = 0
        for i in range(n-1) :
            bought = nums[i]
            sold = float('-inf')
            for j in range(i+1,n) :
                sold = max(sold,nums[j])
            if sold > bought :
                max_profit = max(max_profit,(sold-bought))
        return max_profit
    
    def maximise_profit(self, nums) :
        n = len(nums)
        min_price = nums[0]
        max_profit = 0
        for x in nums :
            if min_price < x :
                max_profit = max(max_profit, x-min_price)
            else : 
                min_price = x

        return max_profit





sol = Solution()
print(sol.maximise_profit([7,1,5,3,6,4]))
            
