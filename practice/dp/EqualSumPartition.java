package practice.dp;

public class EqualSumPartition {
    public boolean equalParts(int[] arr, int currSum, int totalSum, int n) {
        if (n == 0)
            return false;
        int newCurrSum = currSum + arr[n - 1];
        if (newCurrSum == totalSum - newCurrSum) {
            return true;
        }
        boolean take = equalParts(arr, newCurrSum, totalSum, n - 1);
        boolean leave = equalParts(arr, currSum, totalSum, n - 1);
        return take || leave;

    }

    public static void main(String[] args) {

        int arr[] = new int[] { 1, 11, 5 };
        int n = arr.length;
        int totalSum = 0;
        for (int element : arr) {
            totalSum += element;
        }
        EqualSumPartition obj = new EqualSumPartition();
        boolean ans = obj.equalParts(arr, 0, totalSum, n);
        System.out.println(ans);

    }
}
