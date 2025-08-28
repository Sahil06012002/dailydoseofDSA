from typing import List


class Solution :
    # max sum subarray of given size
    def maxSum(self, arr , size) :
        i=0,j=0,maxSum = float('-inf')
        currSum = 0
        while(i < len(arr) and j < len(arr)) :
            currSum += arr[j]
            if((j-i+1) < size) :
                j +=1
            elif((j-i+1) == size) :
                maxSum  = max(maxSum , currSum)
                currSum = currSum - arr[i]
                i +=1
                j+=1

        return maxSum
    
    # max sum subarray in an array
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        j=0
        currSum = 0
        maxSum = float('-inf')
        while(i < len(nums) and j < len(nums)) :
            currSum = currSum + nums[j]
            maxSum  = max(maxSum, currSum)

            if(currSum < 0) :
                currSum = 0
                i = j+1
            j+=1
        return maxSum

 

