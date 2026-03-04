package practice.SlidingWindow;

public class Kadane {
    int maxSubarraySum(int[] arr) {
        // Code here
        int maxSoFar = Integer.MIN_VALUE;
        int s = 0, e = 0, sum = 0;
        while (e < arr.length) {
            sum += arr[e];
            maxSoFar = Math.max(maxSoFar, sum);
            if (sum < 0) {
                sum = 0;
                s = e + 1;
            }
            e++;
        }
        return maxSoFar;

    }

    public static void main(String[] args) {
        Kadane obj = new Kadane();
        int ans = obj.maxSubarraySum(new int[] { -2, -4 });
        System.out.println(ans);
    }
}
