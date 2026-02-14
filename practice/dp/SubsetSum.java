package practice.dp;

public class SubsetSum {
    public boolean subset(int[] arr, int target, int n) {
        if (target == 0)
            return true;

        if (n == 0)
            return false;

        boolean take = false;
        if (arr[n - 1] <= target) {
            take = subset(arr, target - arr[n - 1], n - 1);
        }
        boolean leave = subset(arr, target, n - 1);
        return take || leave;

    }

    public static void main(String[] args) {
        SubsetSum sol = new SubsetSum();
        int[] arr = new int[] { 2, 7, 8, 10 };
        int target = 11;
        boolean ans = sol.subset(arr, target, arr.length);
        System.out.println(ans);
    }
}
