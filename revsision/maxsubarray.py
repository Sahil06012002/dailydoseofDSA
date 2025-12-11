# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


from typing import List


class Solution:
    # brute force
    def maxSubArrayBrute(self, nums: List[int]) -> int:
        n = len(nums)

        max_sum = 0
        for i in range(n) :
            sum = 0
            for j in range(i,n) :
                sum += nums[j]
                max_sum = max(max_sum, sum)
        print(max_sum)
        return max_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        curr_sum = 0
        max_sum = float('-inf')

        while end < n :
            curr_sum += nums[end]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0 :
                curr_sum = 0
            end += 1
        print(max_sum)
        return max_sum  









    
sol  = Solution()
sol.maxSubArray([5,4,-1,7,8])



        