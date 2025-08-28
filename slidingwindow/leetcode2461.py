# 2461. Maximum Sum of Distinct Subarrays With Length K

# You are given an integer array nums and an integer k. 
# Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. 
# If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        tempSet = set()
        i =0
        j =0
        currSum = 0
        maxSum = 0

        while(i < len(nums) and j < len(nums)) :
            print(currSum)
            print(tempSet)
            print(maxSum)

            while nums[j] in tempSet:
                tempSet.remove(nums[i])
                currSum -= nums[i]
                i += 1

            currSum = currSum + nums[j]
            tempSet.add(nums[j])

            if((j-i + 1) < k) :
                j+=1

            elif((j-i + 1) == k ) :
                maxSum = max(maxSum,currSum)
                tempSet.discard(nums[i])
                currSum -= nums[i]
                i+=1
                j+=1

        return maxSum
    

sol = Solution()
ans = sol.maximumSubarraySum([1,5,4,2,9,9,9],3)
print(ans)


