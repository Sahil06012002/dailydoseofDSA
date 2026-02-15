package practice.dp;

public class CountSubset {
    int ans = 0;

    public int count(int[] arr, int target, int n) {
        if (n == 0) {
            return (target == 0) ? 1 : 0;
        }
        return count(arr, target - arr[n - 1], n - 1) + count(arr, target, n - 1);

    }

    public int countItr(int[] arr, int target, int n) {
        int[][] dp = new int[n + 1][target + 1];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < target + 1; j++) {
                if (i == 0)
                    dp[i][j] = 0;
                if (j == 0)
                    dp[i][j] = 1;
            }
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < target + 1; j++) {
                if (arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n][target];

    }

    public static void main(String[] args) {
        CountSubset obj = new CountSubset();
        int[] arr = new int[] { 5, 2, 3, 10, 6, 8 };
        int target = 10;
        int n = arr.length;
        int ans = obj.countItr(arr, target, n);
        System.out.println(ans);
    }
}
