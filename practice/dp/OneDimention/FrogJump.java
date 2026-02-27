package practice.dp.OneDimention;

class FrogJump {
    public int find(int[] height, int n) {
        if (n == 1) {
            return 0;
        }
        int left = find(height, n - 1) + Math.abs(height[n - 1] - height[n - 2]);
        int right = 0;
        if (n >= 3)
            right = find(height, n - 2) + Math.abs(height[n - 1] - height[n - 3]);
        return Math.min(left, right);
    }

    public boolean canCross(int[] stones) {
        boolean[][] dp = new boolean[stones[stones.length - 1] + 1][stones[stones.length - 1] + 1];
        for (int i = 0; i < stones[stones.length - 1] + 1; i++) {
            for (int j = 0; j < stones[stones.length - 1] + 1; j++) {
                if (j == 0 || i == 0) {
                    dp[i][j] = false;
                }

                if (i == 0 && j == 1) {
                    dp[i][j] = true;
                }

            }
        }

        for (int i = 0; i < stones[stones.length - 1] + 1; i++) {
            for (int j = 0; j < stones[stones.length - 1] + 1; j++) {
                for (int step : new int[] { j - 1, j, j + 1 }) {
                    if (step <= 0)
                        continue;
                    if (positionExistes(stones, i)) {
                        dp[i][j] = dp[i + step][step];
                    }
                }
            }
        }

        return dp[stones[stones.length - 1]][stones[stones.length - 1]];

    }

    public boolean canJump(int[] stones, int position, int jump) {
        if (position == stones[stones.length - 1]) {
            return true;
        }
        for (int step : new int[] { jump - 1, jump, jump + 1 }) {
            if (step <= 0)
                continue;
            if (positionExistes(stones, position)) {
                if (canJump(stones, position + step, step)) {
                    return true;
                }

            }
        }
        return false;

    }

    public boolean canJump1(int[] stones, int position, int jump) {
        if (position == stones[stones.length - 1]) {
            return true;
        }
        for (int step : new int[] { jump - 1, jump, jump + 1 }) {
            if (step > 0) {
                if (positionExistes(stones, position + step)) {

                    if (canJump1(stones, position + step, step)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean positionExistes(int[] stones, int position) {
        // TODO Auto-generated method stub
        int s = 0, e = stones.length - 1;
        while (s <= e) {
            int mid = s + (e - s) / 2;
            if (stones[mid] == position) {
                return true;
            } else if (stones[mid] < position) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] stones = new int[] { 0, 2, 5 };
        FrogJump obj = new FrogJump();
        System.out.println(obj.canJump1(stones, stones[0], 1));
    }
}
