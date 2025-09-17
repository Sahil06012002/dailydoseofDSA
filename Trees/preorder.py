

from typing import List


class Preorder :

    def dfs(self, root, result) :
        if root == None :
            return 
        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)


    def inorder_traversal_itr(self, root) -> List[int]:

        # iterative
        result = []
        st = []
        curr = root


        while curr or st : 
            while curr :
                st.append(curr)
                curr = curr.left

            element = st.pop()
            result.append(element.val)
            curr = element.right


        return result
    
    def pre_order_traversal(root) :
        stack = []
        if root is not None :
            stack.append(root)
        result = []


        while stack :
            node = stack.pop(len(stack)-1)

            result.append(node.val)

            if node.right :
                stack.append(node.right)
            if node.left :
                stack.append(node.left)

        return result



    def postorder_traversal(root) :
        result = []
        def helper(root) :
            if root == None :
                return 
            helper(root.left)
            helper(root.right)
            result.append(root.val)
        helper(root)            
        return result



    def postorder_traversal_itr(root) :
        pass



            







    
