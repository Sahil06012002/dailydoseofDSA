package practice.SlidingWindow;

import java.util.HashSet;

public class MaxSumSubarray {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        HashSet<Integer> set = new HashSet<>();
        int s = 0, e = 0;
        long sum = 0, ans = 0;
        while (e < n) {
            while (set.contains(nums[e]) && s < e) {
                sum -= nums[s];
                set.remove(nums[s]);
                s++;
                continue;
            }
            set.add(nums[e]);
            sum += nums[e];
            if (e - s + 1 == k) {
                ans = Math.max(sum, ans);
                sum -= nums[s];
                set.remove(nums[s]);
                s++;
            }
            e++;
        }
        return ans;
    }

    public static void main(String[] args) {
        MaxSumSubarray obj = new MaxSumSubarray();
        System.out.println(obj.maxmaximumSubarraySum(new int[]{1,5,4,2,9,9,9}, k));
    }
}
