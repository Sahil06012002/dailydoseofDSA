from typing import List

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows  = len(triangle) -1 
        # print(rows)
        def helper(i, j) :
            if i == rows :
                return triangle[i][j]
            ans = min(helper(i+1,j),helper(i+1,j+1))
            return ans + triangle[i][j]
        return helper(0,0)

sol = Solution()
ans = sol.minimumTotal([[-10]])
print(ans)