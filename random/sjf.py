from typing import List


class Solution :

    def sjf(self,jobs : List[int]) :
        time = []
        time .append(0)
        jobs.sort()
        currSum = jobs[0]
        for i in range(1,len(jobs)) :
            time.append(currSum)
            currSum += jobs[i]

        return sum(time)/len(time)
    
sol = Solution()
ans = sol.sjf([4,3,7,1,2])
print(ans)
