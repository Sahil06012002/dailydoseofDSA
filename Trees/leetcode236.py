# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
# nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).


from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mapParents(self,root , parentMap)  :
        q = deque()
        q.append(root)
        parentMap[root] = None 

        while q :
            node : TreeNode = q.popleft()
            if node.left :
                parentMap[node.left] = node
                q.append(node.left)
            if node.right :
                parentMap[node.right] = node
                q.append(node.right)
        
                
    def find_path(self,root ,parentMap) :
        result = []
        while root  :
            result.append(root)
            root = parentMap[root]
        return result



    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentMap = dict()

        self.mapParents(root,parentMap)
        # list1 = self.find_path(p,parentMap)
        # list2 = self.find_path(q,parentMap)

        while p :
            while q :
                if p.val == q.val :
                    return p
                q = parentMap[q]
            p = parentMap[p]
        return None

        