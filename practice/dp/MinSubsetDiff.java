package practice.dp;

public class MinSubsetDiff {
    int minDiff = 0;

    public boolean[][] subset(int[] arr, int target, int n, boolean[][] dp) {
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < target + 1; j++) {
                if (arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp;
    }

    public int minSubDiff(boolean[][] dp, int sum, int n) {
        int min = Integer.MAX_VALUE;
        for (int i = 0; i <= sum / 2; i++) {
            if (dp[n][i]) {
                min = Math.min(min, sum - 2 * i);

            }
        }
        return min;
    }

    public static void main(String[] args) {
        MinSubsetDiff obj = new MinSubsetDiff();
        int[] arr = new int[] { 1, 2, 3, 4 };
        int n = arr.length;
        int sum = 0;
        for (int element : arr) {
            sum += element;
        }
        boolean[][] dp = new boolean[n + 1][sum + 1];
        for (int i = 0; i < n + 1; i++) {
            dp[i][0] = true;
        }
        dp = obj.subset(arr, sum, n, dp);

        int ans = obj.minSubDiff(dp, sum, n);
        System.out.println(ans);
    }
}
