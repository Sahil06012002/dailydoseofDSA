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
    
    def eggDropOptimised(self, n, k):
        memo = {}

        def solve(e: int, f: int):
            if f <= 1 or e == 1:
                return f

            if (e, f) in memo:
                return memo[(e, f)]

            ans = float('inf')
            low, high = 1, f

            while low <= high:
                mid = (low + high) // 2

                if (e-1, mid-1) in memo:
                    broken = memo[(e-1, mid-1)]
                else:
                    memo[(e-1, mid-1)] = broken = solve(e-1, mid-1)

                if (e, f-mid) in memo:
                    not_broken = memo[(e, f-mid)]
                else:
                    memo[(e, f-mid)] = not_broken = solve(e, f-mid)

                temp = 1 + max(broken, not_broken)
                ans = min(ans, temp)

                if broken > not_broken:
                    high = mid - 1
                else:
                    low = mid + 1

            memo[(e, f)] = ans
            return ans

        return solve(n, k)
