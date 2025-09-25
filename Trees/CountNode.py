# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def nodeHeight(node,lr) :
            h = 0

            while node :
                if lr : 
                    node = node.left
                else :
                    node = node.right
                h+=1
            return h
        if root is None :
            return 0
        left_height =  nodeHeight(root,True)
        rightHeight = nodeHeight(root,False)
        print(left_height, rightHeight)
        if left_height == rightHeight :
            return (1 << left_height) - 1
        else :
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


root = TreeNode(2)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(2)


sol = Solution()
sol.countNodes(root)