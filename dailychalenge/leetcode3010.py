from typing import List

# brute force approach
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f_element = nums[0]
        min_ans = float('inf')

        for i in range (1,len(nums)) :
            for j in range(i+1, len(nums)) :
                min_ans = min(min_ans,(f_element+nums[i]+nums[j]))

        return min_ans        





# optimised (initial intuition)
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f_element = nums[0]
        s_element = float('inf')
        smallest_index = 0

        for i in range (1,len(nums)) :
            if nums[i] < s_element :
                s_element = nums[i]
                smallest_index = i
        t_element = float('inf')
        for i in range(1,smallest_index) :
            t_element = min(t_element, nums[i])
        for i in range(smallest_index+1, len(nums)) :
            t_element = min(t_element, nums[i])
        

        return f_element + s_element + t_element
    

    def two_min(nums) :
        f_smallest = nums[0]
        f_index = 0
        s_smallest = nums[0]

        for i in range(1,len(nums)) :
            if nums[i] < f_smallest :
                f_smallest = nums[i]
                f_index = i

            if nums[i] < s_smallest and f_index != i :
                s_smallest = nums[i]
        return f_smallest, s_smallest 


# Ideal Pattern Approach 
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        f_element = nums[0]
        f_smallest = float('inf')
        s_smallest = float('inf')

        for i in range(1,len(nums)) :
            if nums[i] <= f_smallest :
                s_smallest = f_smallest
                f_smallest = nums[i]
            else :
                s_smallest = min(s_smallest, nums[i])
        
        return f_element + f_smallest + s_smallest