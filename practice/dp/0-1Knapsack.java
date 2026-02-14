package practice.dp;

import java.util.Arrays;

class Main {
    // given a array of items and its weight and the price. We have a bag in which
    // we can place these
    // items. The bag have a maximmum capacity and we have to maximise the profit.
    // wt : [10,5, 2,9]
    // val: [5, 20,1,80]
    // W : 20

    public static int[][] t = new int[4][8];

    public int findMax(int[] wt, int[] val, int index, int maxCapacity) {
        if (maxCapacity < 0 || index == wt.length) {
            return 0;
        }
        System.out.println("max cap--->" + maxCapacity);
        System.out.println();
        if (wt[index] > maxCapacity) {
            return findMax(wt, val, index + 1, maxCapacity);
        } else {
            return Math.max(val[index] + findMax(wt, val, index + 1, maxCapacity - wt[index]),
                    findMax(wt, val, index + 1, maxCapacity));
        }

    }

    public int findMaxAlt(int[] wt, int[] val, int maxCapacity, int position) {
        System.out.println("max cap--->" + maxCapacity);

        if (maxCapacity <= 0 || position == 0) {
            return 0;
        }

        if (wt[position - 1] > maxCapacity) {
            return findMaxAlt(wt, val, maxCapacity, position - 1);
        } else {
            return Math.max(val[position - 1] + findMaxAlt(wt, val, maxCapacity - wt[position - 1], position - 1),
                    findMaxAlt(wt, val, maxCapacity, position - 1));
        }
    }

    public int findMaxMemo(int[] wt, int[] val, int W, int n, int[][] dp) {

        if (W <= 0 || n == 0) {
            return 0;
        }
        if (dp[n][W] != -1) {
            return dp[n][W];
        }

        if (wt[n - 1] <= W) {
            int ans = Math.max(val[n - 1] + findMaxMemo(wt, val, W - wt[n - 1], n - 1, dp),
                    findMaxMemo(wt, val, W, n - 1, dp));
            dp[n][W] = ans;
            return ans;
        } else {
            int ans = findMaxMemo(wt, val, W, n - 1, dp);

            dp[n][W] = ans;
            return ans;
        }

    }

    public int findMaxIterative(int[] wt, int[] val, int W) {
        int n = val.length;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < W + 1; j++) {
                if (wt[i - 1] <= j) {
                    t[i][j] = Math.max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j]);
                } else {
                    t[i][j] = t[i - 1][j];
                }

            }
        }
        return t[n][W];
    }

    public static void main(String[] args) {
        int W = 7;
        Main obj = new Main();

        // int ans = obj.findMaxAlt(new int[] { 1, 3, 4 }, new int[] { 1, 4, 5 }, 7, 3);
        int[] wt = new int[] { 1, 3, 4 };
        int[] val = new int[] { 1, 4, 5 };
        int n = wt.length;
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < W + 1; j++) {
                if (i == 0 || j == 0)
                    t[i][j] = 0;
            }
        }
        for (int i = 0; i < n + 1; i++) {
            System.out.println(Arrays.toString(t[i]));
            System.out.println();
        }
        int ans = obj.findMaxIterative(wt, val, W);
        System.out.println(ans);

    }
}