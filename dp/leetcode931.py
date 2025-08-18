# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element
# in the next row that is either 
# directly below or diagonally left/right. 
# Specifically, the next element from position (row, col) 
# will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


from functools import lru_cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row , col = len(matrix), len(matrix[0])

        @lru_cache(maxsize = None)
        def helper(i,j) :
            if i == row-1 :
                return matrix[i][j]
            left , right = float('inf'),float('inf')
            if j > 0 :
                left = helper(i+1,j-1)
            center = helper(i+1,j)
            if j < col-1 :
                right = helper(i+1,j+1)
            ans = min(left,right)
            ans = min(ans,center)
            return ans + matrix[i][j]

        return min(helper(0, j) for j in range(col))

