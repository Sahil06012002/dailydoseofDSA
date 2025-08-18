class Solution :
    def eggDrop(self, n, k):
        dict = {}
        def solve(e : int, f : int ) :
            if f <= 1 or e <=1:
                return f
            if (e,f) in dict :
                return dict[(e,f)]
            ans = float('inf')
            for k in range(1,f+1) :
                broken = solve(e-1,k-1)
                not_broken  = solve(e,f-k)
                temp = 1 + max (broken,not_broken)
                ans = min(ans,temp)
            dict[(e,f)] = ans
            return ans
        return solve(n,k)
