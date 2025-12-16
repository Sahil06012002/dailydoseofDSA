# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution :
    def test(self, height) :
        n = len(height)
        leftMax = [0] * n
        leftMax[0] = height[0]
        rightMax = [0] * n
        rightMax[n-1] = height[n-1]
        
        for i in range(1,n): 
            leftMax[i] = max(height[i-1],leftMax[i-1])

        for i in range(n-2,-1,-1) :
            rightMax[i] = max(height[i+1], rightMax[i+1])

        result = 0

        for i in range(1,n-1) :
            if height[i] < leftMax[i] and height[i] < rightMax[i] :
                result += min(leftMax[i], rightMax[i]) - height[i]

        return result



sol = Solution()
sol.test([0,1,0,2,1,0,1,3,2,1,2,1])
        

