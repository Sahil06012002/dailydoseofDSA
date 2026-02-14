package practice.dp;

public class SubsetSum {
    public boolean subset(int[] arr, int target, int n) {
        if (target == 0)
            return true;

        if (n == 0)
            return false;

        if (arr[n - 1] <= target) {
            return subset(arr, target - arr[n - 1], n - 1) || subset(arr, target, n - 1);
        } else {
            return subset(arr, target, n - 1);
        }
    }

    static Boolean isSubsetSum(int arr[], int sum) {
        // code here
        int n = arr.length;

        boolean[][] dp = new boolean[n + 1][sum + 1];

        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < sum + 1; j++) {
                if (i == 0)
                    dp[i][j] = false;
                if (j == 0)
                    dp[i][j] = true;
            }
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < sum + 1; j++) {
                if (arr[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n][sum];
    }

    public static void main(String[] args) {
        SubsetSum sol = new SubsetSum();
        int[] arr = new int[] { 2, 7, 8, 10 };
        int target = 11;
        boolean ans = sol.subset(arr, target, arr.length);
        System.out.println(ans);
    }
}
