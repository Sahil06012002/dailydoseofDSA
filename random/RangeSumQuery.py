import sys


class Solution :
    
    def __init__(self, arr):
        self.arr = arr

    def sum_subarray(self):
        n = len(self.arr)
        ans = 0
        for i in range(n):
            ans += self.arr[i] * (i + 1) * (n - i)
        return ans
                

    
    
def main() :
    input = sys.stdin.readline
    
    n = int(input().strip())
    arr = list(map(int, input().split()))

    sol = Solution(arr)
    ans = []

    ans = sol.sum_subarray()

    print(ans)

if __name__ == "__main__":
    main()