package practice.dp.UnboundedKnapsack;

public class RodCutting {

    public int helper(int[] price, int[] length, int maxLen, int position) {
        if (maxLen == 0 || position == 0) {
            return 0;
        }
        if (length[position - 1] <= maxLen) {
            return Math.max(price[position - 1] + helper(price, length, maxLen - length[position - 1], position),
                    helper(price, length, maxLen, position - 1));
        } else {
            return helper(price, length, maxLen, position - 1);
        }
    }

    public int cutRod(int[] price) {
        // code here
        int n = price.length;
        int[] length = new int[n];

        for (int i = 1; i <= n; i++) {
            length[i - 1] = i;
        }
        return helper(price, length, n, n);

    }

    public int cutRodDP(int[] price, int[] length, int maxLen, int position, int[][] dp) {
        for (int i = 1; i < position + 1; i++) {
            for (int j = 1; j < maxLen + 1; j++) {
                if (length[i - 1] <= j) {
                    dp[i][j] = Math.max(price[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[position][maxLen];
    }

    public int rodCut(int[] prices, int len, int n) {
        if (n == 0 || len == 0) {
            return 0;
        }
        if (n <= len) {
            return Math.max(prices[n - 1] + rodCut(prices, len - n, n), rodCut(prices, len, n - 1));
        } else {
            return rodCut(prices, len, n - 1);
        }

    }

    public static void main(String[] args) {
        int[] price = new int[] { 3, 5, 1, 9 };
        int n = price.length;
        int[] length = new int[n];
        for (int i = 0; i < n; i++) {
            length[i] = i + 1;
        }
        int[][] dp = new int[n + 1][n + 1];
        RodCutting rc = new RodCutting();
        // int ans = rc.cutRodDP(price, length, n, n, dp);
        int ans = rc.rodCut(price, n, n);
        // int ans = rc.cutRod(price);

        System.out.println(ans);

    }

}
