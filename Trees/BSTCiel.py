from typing import Optional


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

        
class Solution:
    def findCeil(self,root, x):
        # code here
        result = 0
        while root :
            if root.val == x : 
                result = root.data
                return root
            elif root.data < x :
                root = root.right
            elif root.data > x :
                result = root.data
                root = root.left

        return result
    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_next_largest(node) :
            while node :
                if node.left == None :
                    node.left = None
                    return node.val
                node = node.left
            return None
        

        def searchNode(root,target) :
            while root :
                if root.val == target :
                    return root
                elif root.val > target :
                    root = root.left
                else :
                    root = root.right
            return None
        targetNode = searchNode(root,key)
        if targetNode.right :
            val = find_next_largest(targetNode.right)
            targetNode.val = val
