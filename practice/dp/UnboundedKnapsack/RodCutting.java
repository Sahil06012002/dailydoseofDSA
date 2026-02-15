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

    public static void main(String[] args) {
        int[] price = new int[] { 1, 5, 8, 9, 10, 17, 17, 20 };
        int n = price.length;
        int[] length = new int[n];
        int[][] dp = new int[n + 1][n + 1];

    }

}
