from functools import lru_cache
class Solution:
    def isScramble(self,S1: str, S2: str):
        @lru_cache(maxsize = None)
        def helper(S1,S2) :
            n = len(S1)
            m = len(S2)
            if n != m :
                return False
            if S1 == S2 :
                return True
            if len(S1) == 1 or len(S2) == 1 :
                return False
            ans = True
            for i in range(1,len(S1)) :
                swapped = helper(S1[0:i],S2[m-i:m]) and helper(S1[i:n],S2[0:m-i])
                not_swapped = helper(S1[0:i],S2[0:i]) and helper(S1[i:n],S2[i:m])
                ans = swapped or not_swapped
                if ans : 
                    break
            return ans
        return helper(S1,S2)
    
    def isScrambleMemo(self,S1: str, S2: str):
        dict = {}
        def helper(S1,S2) :
            n = len(S1)
            m = len(S2)
            if n != m :
                return False
            if S1 == S2 :
                return True
            if len(S1) == 1 or len(S2) == 1 :
                return False
            if (S1,S2) in dict :
                return dict[(S1,S2)]
            ans = True
            for i in range(1,len(S1)) :
                swapped = helper(S1[0:i],S2[m-i:m]) and helper(S1[i:n],S2[0:m-i])
                not_swapped = helper(S1[0:i],S2[0:i]) and helper(S1[i:n],S2[i:m])
                ans = swapped or not_swapped
                if ans : 
                    break
            dict[(S1,S2)] = ans
            return ans
        return helper(S1,S2)