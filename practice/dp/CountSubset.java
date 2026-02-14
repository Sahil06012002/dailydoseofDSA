package practice.dp;

public class CountSubset {
    int ans = 0;

    public int count(int[] arr, int target, int n) {
        if (n == 0) {
            return (target == 0) ? 1 : 0;
        }
        return count(arr, target - arr[n - 1], n - 1) + count(arr, target, n - 1);

    }

    public static void main(String[] args) {

    }
}
