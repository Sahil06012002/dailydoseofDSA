# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self) :
        parentMap = {} 
        result = []
        targetNode = None

    def buildGraph(self,node, target) :
        queue = deque()
        queue.append(node)
        n = len(queue)
        for i in range(n) :
            node = queue.popleft()
            if node.val == target :
                self.targetNode = node
            if node.left :
                self.parentMap[node.left] = node
            if node.right :
                self.parentMap[node.right] = node

                
    def traverseGraph(self, startNode : TreeNode, k : int, currentDist : int) :
        if startNode == None :
            return 
        if currentDist == k :
            self.result.append(startNode.val)
        self.traverseGraph(self.parentMap[startNode],k,currentDist+1)
        self.traverseGraph(startNode.left , k , currentDist+1)
        self.traverseGraph(startNode.right, k, currentDist+1)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None :
            return []
        self.buildGraph(root, target)
        self.traverseGraph(self.targetNode,k,0)

        return self.result

        



        