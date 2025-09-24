# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxAns = float('-inf')
        q = deque()
        q.append((root,1))
        while q :
            n = len(q)
            start = 0 
            end = 0
            width = float('-inf')
            for i in range(n) :
                node, currWid = q.popleft()
                
                if i == 0 :
                    start = currWid
                if i == n-1 :
                    end = currWid
                width = end - start + 1
                if node.left :
                    q.append((node.left , (((currWid-1)*2))+1))
                if node.right :
                    q.append((node.right, (((currWid-1)*2)+2)))
            maxAns = max(maxAns, width)
                
        return maxAns
        