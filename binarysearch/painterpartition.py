class Solution:
    
    
    def minTime (self, arr, k):
        min_val = max(arr)
        max_val = sum(arr)
        # code here
        def isPossible(maxTime,k) :
            if maxTime < min_val :
                return False
                
            currSum = 0
            painter = 1
            for length in arr :

                
                if currSum + length <= maxTime :
                    currSum += length
                else :
                   currSum = length
                   painter += 1
                   
            return painter <= k
            
            
        result = 0
        s = min_val
        e = max_val
        while(s<= e) :
            mid = (s+e)//2
            
            if isPossible(mid,k) :
                result = mid
                e = mid-1
            else :
                s = mid+1
        return result
                
            