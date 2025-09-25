# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None



class Solution:
    def isSumProperty(self, root):
        ans = True
        def helper(node) :
            nonlocal ans
            if root == None :
                return 
            sum = 0
            if node.left :
                sum += node.left.val
            if node.right :
                sum += node.left.val
            if sum != node.val :
                ans = False
        helper(root)
        return ans
