# Given an array of integers nums and an integer k, return the total number 
# of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


from typing import List


class Solution:

        #  nums contains only positive elements 
    def LongestSubarraySum(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        lenMax = 0
        currSum = 0
        while(j < len(nums)) :
            currSum += nums[j]
            if(currSum < k) :
                j+=1
            elif(currSum == k) :
                lenMax = max(lenMax , (j-i+1))
                j+=1
            elif(currSum > k) :
                while(currSum > k) :
                    currSum -= nums[i]
                    i+=1
                j+=1

        return lenMax
    

    # contains negetive values as well
    def subarraySum(self, nums: List[int], k: int) -> int:
        tempDict = {}
        currSum =0
        count = 0
        for i in range(len(nums)) : 
            currSum += nums[i]
            if(currSum == k) :
                count += 1
            if((currSum - k) in tempDict) : 
                    count += tempDict[currSum - k]
            if(currSum in tempDict) :
                tempDict[currSum] += 1
            elif(currSum not in tempDict) :
                tempDict[currSum] = 1

        return count




        

    
