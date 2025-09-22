# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = [] 
        if root == None : 
            return result 
        q = []

        q.append(root)
        while q :
            n = len(q)
            for i in range(n) :
                node = q.pop(0)
                if i == 0 :
                    result.append(node.val)

                if node.right :
                    q.append(node.right)
                if node.left :
                    q.append(node.left)

        return result