# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

import json
from typing import List, Optional
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.append(root)
        s = ""
        while q :
            n = len(q)
            for i in range(n) :
                node = q.popleft()
                s += str(node.val)
                if node.left  :
                    q.append(node.left)
                else :
                    s += "N"
                if node.right :
                    q.append(node.right)
                else :
                    s += "N"
        print(s)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lvlOdr = json.loads(data)

        root = TreeNode(data[0])
        for levels in lvlOdr :
            for nodeVal in levels :
                pass
                
        pass



root = TreeNode(1)                  # root = 1
root.left = TreeNode(2)             # left child of root = 2
root.right = TreeNode(3)            # right child of root = 3
root.right.left = TreeNode(4)        # left child of node 2 = 4
root.right.right = TreeNode(5)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    [1,2,3,4,5]
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val = preorder[0]

        root = TreeNode(val)

        def helper(node , preorder, inorder) :
            if len(preorder) == 0 :
                return None
            
            val = preorder[0]

            rootIdx = -1
            for i in range(len(inorder)) :
                if inorder[i] == val :
                    rootIdx = i

            currNode = TreeNode(val)


            node.left = helper(currNode,preorder[1:rootIdx+1],inorder[0:rootIdx])

            node.right = helper(currNode,preorder[rootIdx+1,len(preorder)],inorder[rootIdx+1,len(inorder)])

            return currNode
        result = helper(root , preorder, inorder)
        return result
        







cod = Codec()
cod.serialize(root)