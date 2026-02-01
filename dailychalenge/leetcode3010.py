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