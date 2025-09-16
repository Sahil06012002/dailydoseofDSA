

from typing import List


class Preorder :

    def dfs(self, root, result) :
        if root == None :
            return 
        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)


    def preorderTraversal(self, root) -> List[int]:

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




    
