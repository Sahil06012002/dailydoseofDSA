# You are given an integer array nums of 2 * n integers. 
# You need to partition nums into two arrays of length n to 
# minimize the absolute difference of the sums of the arrays. 
# To partition nums, put each element of nums into one of the two arrays.

# Return the minimum possible absolute difference.

# Examples -------------

# Input: nums = [3,9,7,3]
# Output: 2
# Explanation: One optimal partition is: [3,9] and [7,3].
# The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.


# Input: nums = [-36,36]
# Output: 72
# Explanation: One optimal partition is: [-36] and [36].
# The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.


from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        total_sum = sum(nums)
        memo = {}
        def helper(sum,len,n) :
            if len == N/2 :
                sum2 = total_sum - sum
                diff  = abs(sum-sum2)
                return diff
                
            if n >= N :
                return float('inf')  
            if (sum,len,n) in memo : 
                return memo[(sum,len,n)]
            
            taken = helper(sum + nums[n],len + 1, n+1)
            not_taken = helper(sum , len , n+1)
            ans = min(taken,not_taken)
            memo[(sum,len,n)] = ans
            return ans


        # def helperRefined() :

        #     pass
        
        # helper(0,0,0)

        # return result
    
sol = Solution()
ans = sol.minimumDifference([7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694])
print(ans)

