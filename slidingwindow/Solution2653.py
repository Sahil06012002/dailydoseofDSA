from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        i=0
        j=0
        size = 50
        arr = [0] * size
        result = []

        while(i< len(nums) and j < len(nums)) :
            if(nums[j] < 0) :
                arr[nums[j]+50] += 1  
            
            if((j-i+1) < k) :
                j+=1

            elif((j-i+1) == k) :
                print(i,j)
                print(arr)
                count = 0
                beauty = 0
                for idx in range(size):
                    if arr[idx] > 0:
                        count += arr[idx]
                        if count >= x: 
                            beauty = idx - 50
                            break
                result.append(beauty)


                if(nums[i] < 0) :
                    arr[nums[i]+50] -= 1
                i+=1
                j+=1

        return result
    
sol = Solution()
ans = sol.getSubarrayBeauty([-46,-34,-46], 3 ,3)
print(ans)

        