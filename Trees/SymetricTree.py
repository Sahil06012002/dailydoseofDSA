# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:

        def helper(tree1 , tree2 ):
            if tree1 == None and tree2 == None :
                return True
            
            if tree1 == None or tree2 == None or tree1.val != tree2.val :
                return False
            
            left = helper(tree1.left, tree2.right)
            right = helper(tree1.right , tree2.left)

            return left and right

            
        if root == None:
            return True
        

        

        
        return helper(root.left , root.right)
        



        